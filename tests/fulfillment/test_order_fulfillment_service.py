import pytest
from unittest.mock import create_autospec

from dependent.fulfillment.inventory_service import InventoryService
from dependent.fulfillment.shipping_service import ShippingService
from dependent.fulfillment.order_fulfillment_service import OrderFulfillmentService


class TestOrderFulfillmentService:
    def setup_method(self) -> None:
        self.inventory_service = create_autospec(InventoryService)
        self.shipping_service = create_autospec(ShippingService)
        self.order_fulfillment_service = OrderFulfillmentService(self.inventory_service, self.shipping_service)

    def test_fulfill_with_valid_order_should_reserve_and_create_shipment(self) -> None:
        # Arrange
        # Act
        # Assert
        pass

    def test_fulfill_when_inventory_reservation_fails_should_propagate_exception(self) -> None:
        # Arrange
        # Act & Assert
        pass

    def test_fulfill_when_shipping_creation_fails_should_propagate_exception(self) -> None:
        # Arrange
        # Act & Assert
        pass

    def test_fulfill_with_different_addresses_should_pass_correct_address_to_shipping(self) -> None:
        # Arrange
        # Act
        # Assert
        pass

    def test_fulfill_multiple_orders_should_interact_with_dependencies_each_time(self) -> None:
        # Arrange
        # Act
        # Assert
        pass
