from decimal import Decimal


class Receipt:
    def __init__(self, payment_id: str, reference: str, total: Decimal) -> None:
        self._payment_id = payment_id
        self._reference = reference
        self._total = total

    @property
    def payment_id(self) -> str:
        return self._payment_id

    @property
    def reference(self) -> str:
        return self._reference

    @property
    def total(self) -> Decimal:
        return self._total
