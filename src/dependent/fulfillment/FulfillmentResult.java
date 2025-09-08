package org.example.dependent.fulfillment;

public class FulfillmentResult {
    private final String reservationId;
    private final String trackingId;

    public FulfillmentResult(String reservationId, String trackingId) {
        this.reservationId = reservationId;
        this.trackingId = trackingId;
    }

    public String getReservationId() {
        return reservationId;
    }

    public String getTrackingId() {
        return trackingId;
    }
}


