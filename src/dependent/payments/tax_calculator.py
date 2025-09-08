from decimal import Decimal

from .cart import Cart


class TaxCalculator:
    def calculate_total_with_tax(self, cart: Cart, currency: str) -> Decimal:
        if cart is None:
            raise ValueError("Cart cannot be null")
        subtotal = cart.subtotal
        tax_rate = Decimal("0.20")
        tax = subtotal * tax_rate
        return subtotal + tax
