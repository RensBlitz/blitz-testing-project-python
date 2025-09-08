from .address import Address


class ShippingService:
    def create_shipment(self, order_id: str, address: Address) -> str:
        if order_id is None or order_id == "":
            raise ValueError("orderId must be provided")
        if address is None:
            raise ValueError("address must be provided")
        return "trk-" + str(abs(hash(order_id + str(address))))
