from decimal import Decimal


class Cart:
    def __init__(self, subtotal: Decimal, reference: str) -> None:
        if subtotal is None:
            raise ValueError("Subtotal cannot be null")
        if subtotal < Decimal("0"):
            raise ValueError("Subtotal cannot be negative")
        self._subtotal = subtotal
        self._reference = reference if reference is not None else ""

    @property
    def subtotal(self) -> Decimal:
        return self._subtotal

    @property
    def reference(self) -> str:
        return self._reference
