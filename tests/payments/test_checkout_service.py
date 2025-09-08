import pytest
from unittest.mock import create_autospec
from decimal import Decimal

from dependent.payments.checkout_service import CheckoutService
from dependent.payments.tax_calculator import TaxCalculator
from dependent.payments.payment_gateway_client import PaymentGatewayClient
from dependent.payments.receipt_generator import ReceiptGenerator
from dependent.payments.cart import Cart
from dependent.payments.receipt import Receipt


class TestCheckoutService:
    def setup_method(self) -> None:
        self.tax_calculator = create_autospec(TaxCalculator)
        self.payment_gateway_client = create_autospec(PaymentGatewayClient)
        self.receipt_generator = create_autospec(ReceiptGenerator)
        self.service = CheckoutService(self.tax_calculator, self.payment_gateway_client, self.receipt_generator)

    def test_process_checkout_with_valid_input_should_call_collaborators_and_return_receipt(self) -> None:
        # Arrange
        cart = Cart(Decimal("100.00"), "ref-1")
        self.tax_calculator.calculate_total_with_tax.return_value = Decimal("120.00")
        self.payment_gateway_client.charge.return_value = "pay_1"
        receipt = Receipt("pay_1", "ref-1", Decimal("120.00"))
        self.receipt_generator.generate.return_value = receipt

        # Act
        result = self.service.process_checkout(cart, "EUR")

        # Assert
        assert result is receipt
        self.tax_calculator.calculate_total_with_tax.assert_called_once_with(cart, "EUR")
        self.payment_gateway_client.charge.assert_called_once_with(Decimal("120.00"), "EUR", "ref-1")
        self.receipt_generator.generate.assert_called_once_with("pay_1", cart, Decimal("120.00"))

    def test_process_checkout_when_tax_calculator_throws_should_propagate(self) -> None:
        # Arrange
        cart = Cart(Decimal("10.00"), "r")
        self.tax_calculator.calculate_total_with_tax.side_effect = RuntimeError("tax fail")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.service.process_checkout(cart, "USD")
        self.payment_gateway_client.charge.assert_not_called()
        self.receipt_generator.generate.assert_not_called()

    def test_process_checkout_when_payment_gateway_throws_should_propagate(self) -> None:
        # Arrange
        cart = Cart(Decimal("10.00"), "r")
        self.tax_calculator.calculate_total_with_tax.return_value = Decimal("12.00")
        self.payment_gateway_client.charge.side_effect = RuntimeError("gateway down")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.service.process_checkout(cart, "USD")
        self.receipt_generator.generate.assert_not_called()

    def test_process_checkout_with_different_currency_should_pass_currency_along(self) -> None:
        # Arrange
        cart = Cart(Decimal("50.00"), "R2")
        self.tax_calculator.calculate_total_with_tax.return_value = Decimal("60.00")
        self.payment_gateway_client.charge.return_value = "pay_2"
        self.receipt_generator.generate.return_value = Receipt("pay_2", "R2", Decimal("60.00"))

        # Act
        self.service.process_checkout(cart, "GBP")

        # Assert
        self.tax_calculator.calculate_total_with_tax.assert_called_once_with(cart, "GBP")
        self.payment_gateway_client.charge.assert_called_once_with(Decimal("60.00"), "GBP", "R2")

    def test_process_checkout_multiple_checkouts_should_interact_with_dependencies_each_time(self) -> None:
        # Arrange
        carts = [
            Cart(Decimal("10.00"), "A"),
            Cart(Decimal("20.00"), "B"),
            Cart(Decimal("30.00"), "C"),
        ]
        totals = [Decimal("12.00"), Decimal("24.00"), Decimal("36.00")]
        pays = ["p1", "p2", "p3"]
        self.tax_calculator.calculate_total_with_tax.side_effect = totals
        self.payment_gateway_client.charge.side_effect = pays
        self.receipt_generator.generate.side_effect = [
            Receipt("p1", "A", Decimal("12.00")),
            Receipt("p2", "B", Decimal("24.00")),
            Receipt("p3", "C", Decimal("36.00")),
        ]

        # Act
        results = [self.service.process_checkout(c, "USD") for c in carts]

        # Assert
        assert [r.payment_id for r in results] == pays
        assert self.tax_calculator.calculate_total_with_tax.call_count == 3
        assert self.payment_gateway_client.charge.call_count == 3
        assert self.receipt_generator.generate.call_count == 3
