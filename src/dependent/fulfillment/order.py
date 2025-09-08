from .address import Address


class Order:
    def __init__(self, order_id: str, product_id: str, quantity: int, address: Address) -> None:
        self._order_id = order_id
        self._product_id = product_id
        self._quantity = quantity
        self._address = address

    @property
    def order_id(self) -> str:
        return self._order_id

    @property
    def product_id(self) -> str:
        return self._product_id

    @property
    def quantity(self) -> int:
        return self._quantity

    @property
    def address(self) -> Address:
        return self._address
