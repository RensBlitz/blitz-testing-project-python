package org.example.dependent.fulfillment;

public class Order {
    private final String orderId;
    private final String productId;
    private final int quantity;
    private final Address address;

    public Order(String orderId, String productId, int quantity, Address address) {
        this.orderId = orderId;
        this.productId = productId;
        this.quantity = quantity;
        this.address = address;
    }

    public String getOrderId() {
        return orderId;
    }

    public String getProductId() {
        return productId;
    }

    public int getQuantity() {
        return quantity;
    }

    public Address getAddress() {
        return address;
    }
}


