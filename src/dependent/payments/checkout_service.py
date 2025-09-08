from decimal import Decimal

from .tax_calculator import TaxCalculator
from .payment_gateway_client import PaymentGatewayClient
from .receipt_generator import ReceiptGenerator
from .cart import Cart
from .receipt import Receipt


class CheckoutService:
    def __init__(self, tax_calculator: TaxCalculator, payment_gateway_client: PaymentGatewayClient, receipt_generator: ReceiptGenerator) -> None:
        self._tax_calculator = tax_calculator
        self._payment_gateway_client = payment_gateway_client
        self._receipt_generator = receipt_generator

    def process_checkout(self, cart: Cart, currency: str) -> Receipt:
        total_with_tax: Decimal = self._tax_calculator.calculate_total_with_tax(cart, currency)
        payment_id: str = self._payment_gateway_client.charge(total_with_tax, currency, cart.reference)
        return self._receipt_generator.generate(payment_id, cart, total_with_tax)
