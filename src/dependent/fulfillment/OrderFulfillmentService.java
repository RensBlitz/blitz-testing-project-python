package org.example.dependent.fulfillment;

public class OrderFulfillmentService {
    private final InventoryService inventoryService;
    private final ShippingService shippingService;

    public OrderFulfillmentService(InventoryService inventoryService, ShippingService shippingService) {
        this.inventoryService = inventoryService;
        this.shippingService = shippingService;
    }

    public FulfillmentResult fulfill(Order order) {
        String reservationId = inventoryService.reserve(order.getProductId(), order.getQuantity());
        String trackingId = shippingService.createShipment(order.getOrderId(), order.getAddress());
        return new FulfillmentResult(reservationId, trackingId);
    }
}


