package org.example.dependent.fulfillment;

public class ShippingService {
    public String createShipment(String orderId, Address address) {
        if (orderId == null || orderId.isEmpty()) {
            throw new IllegalArgumentException("orderId must be provided");
        }
        if (address == null) {
            throw new IllegalArgumentException("address must be provided");
        }
        return "trk-" + Math.abs((orderId + address.toString()).hashCode());
    }
}


