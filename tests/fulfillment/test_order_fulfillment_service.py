import pytest
from unittest.mock import create_autospec

from dependent.fulfillment.inventory_service import InventoryService
from dependent.fulfillment.shipping_service import ShippingService
from dependent.fulfillment.order_fulfillment_service import OrderFulfillmentService
from dependent.fulfillment.order import Order
from dependent.fulfillment.address import Address


class TestOrderFulfillmentService:
    def setup_method(self) -> None:
        self.inventory_service = create_autospec(InventoryService)
        self.shipping_service = create_autospec(ShippingService)
        self.service = OrderFulfillmentService(self.inventory_service, self.shipping_service)

    def test_fulfill_with_valid_order_should_reserve_and_create_shipment(self) -> None:
        # Arrange
        order = Order("OID1", "PID1", 2, Address("s", "c", "x"))
        self.inventory_service.reserve.return_value = "res-1"
        self.shipping_service.create_shipment.return_value = "trk-1"

        # Act
        result = self.service.fulfill(order)

        # Assert
        assert result.reservation_id == "res-1"
        assert result.tracking_id == "trk-1"
        self.inventory_service.reserve.assert_called_once_with("PID1", 2)
        self.shipping_service.create_shipment.assert_called_once_with("OID1", order.address)

    def test_fulfill_when_inventory_reservation_fails_should_propagate_exception(self) -> None:
        # Arrange
        order = Order("OID1", "PID1", 2, Address("s", "c", "x"))
        self.inventory_service.reserve.side_effect = RuntimeError("inv fail")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.service.fulfill(order)
        self.shipping_service.create_shipment.assert_not_called()

    def test_fulfill_when_shipping_creation_fails_should_propagate_exception(self) -> None:
        # Arrange
        order = Order("OID1", "PID1", 2, Address("s", "c", "x"))
        self.inventory_service.reserve.return_value = "res-1"
        self.shipping_service.create_shipment.side_effect = RuntimeError("ship fail")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.service.fulfill(order)

    def test_fulfill_with_different_addresses_should_pass_correct_address_to_shipping(self) -> None:
        # Arrange
        a1 = Address("s1", "c1", "x1")
        a2 = Address("s2", "c2", "x2")
        o1 = Order("OID1", "PID1", 1, a1)
        o2 = Order("OID2", "PID2", 3, a2)
        self.inventory_service.reserve.side_effect = ["res-1", "res-2"]
        self.shipping_service.create_shipment.side_effect = ["trk-1", "trk-2"]

        # Act
        r1 = self.service.fulfill(o1)
        r2 = self.service.fulfill(o2)

        # Assert
        assert (r1.reservation_id, r1.tracking_id) == ("res-1", "trk-1")
        assert (r2.reservation_id, r2.tracking_id) == ("res-2", "trk-2")
        self.shipping_service.create_shipment.assert_any_call("OID1", a1)
        self.shipping_service.create_shipment.assert_any_call("OID2", a2)

    def test_fulfill_multiple_orders_should_interact_with_dependencies_each_time(self) -> None:
        # Arrange
        orders = [
            Order("OID1", "PID1", 1, Address("s1", "c1", "x1")),
            Order("OID2", "PID2", 2, Address("s2", "c2", "x2")),
            Order("OID3", "PID3", 3, Address("s3", "c3", "x3")),
        ]
        self.inventory_service.reserve.side_effect = ["res-1", "res-2", "res-3"]
        self.shipping_service.create_shipment.side_effect = ["trk-1", "trk-2", "trk-3"]

        # Act
        results = [self.service.fulfill(o) for o in orders]

        # Assert
        assert [r.reservation_id for r in results] == ["res-1", "res-2", "res-3"]
        assert [r.tracking_id for r in results] == ["trk-1", "trk-2", "trk-3"]
        assert self.inventory_service.reserve.call_count == 3
        assert self.shipping_service.create_shipment.call_count == 3
