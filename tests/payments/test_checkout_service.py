import pytest
from unittest.mock import create_autospec

from dependent.payments.checkout_service import CheckoutService
from dependent.payments.tax_calculator import TaxCalculator
from dependent.payments.payment_gateway_client import PaymentGatewayClient
from dependent.payments.receipt_generator import ReceiptGenerator


class TestCheckoutService:
    def setup_method(self) -> None:
        self.tax_calculator = create_autospec(TaxCalculator)
        self.payment_gateway_client = create_autospec(PaymentGatewayClient)
        self.receipt_generator = create_autospec(ReceiptGenerator)
        self.checkout_service = CheckoutService(self.tax_calculator, self.payment_gateway_client, self.receipt_generator)

    def test_process_checkout_with_valid_input_should_call_collaborators_and_return_receipt(self) -> None:
        # Arrange
        # Act
        # Assert
        pass

    def test_process_checkout_when_tax_calculator_throws_should_propagate(self) -> None:
        # Arrange
        # Act & Assert
        pass

    def test_process_checkout_when_payment_gateway_throws_should_propagate(self) -> None:
        # Arrange
        # Act & Assert
        pass

    def test_process_checkout_with_different_currency_should_pass_currency_along(self) -> None:
        # Arrange
        # Act
        # Assert
        pass

    def test_process_checkout_multiple_checkouts_should_interact_with_dependencies_each_time(self) -> None:
        # Arrange
        # Act
        # Assert
        pass
