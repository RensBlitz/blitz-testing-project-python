package org.example.dependent.fulfillment;

public class InventoryService {
    public String reserve(String productId, int quantity) {
        if (productId == null || productId.isEmpty()) {
            throw new IllegalArgumentException("productId must be provided");
        }
        if (quantity <= 0) {
            throw new IllegalArgumentException("quantity must be positive");
        }
        return "res-" + Math.abs((productId + quantity).hashCode());
    }
}


