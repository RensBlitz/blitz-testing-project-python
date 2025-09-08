from decimal import Decimal

from .cart import Cart
from .receipt import Receipt


class ReceiptGenerator:
    def generate(self, payment_id: str, cart: Cart, total_with_tax: Decimal) -> Receipt:
        return Receipt(payment_id, cart.reference, total_with_tax)
