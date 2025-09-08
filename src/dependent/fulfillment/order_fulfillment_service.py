from .inventory_service import InventoryService
from .shipping_service import ShippingService
from .fulfillment_result import FulfillmentResult
from .order import Order


class OrderFulfillmentService:
    def __init__(self, inventory_service: InventoryService, shipping_service: ShippingService) -> None:
        self._inventory_service = inventory_service
        self._shipping_service = shipping_service

    def fulfill(self, order: Order) -> FulfillmentResult:
        reservation_id = self._inventory_service.reserve(order.product_id, order.quantity)
        tracking_id = self._shipping_service.create_shipment(order.order_id, order.address)
        return FulfillmentResult(reservation_id, tracking_id)
