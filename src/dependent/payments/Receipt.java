package org.example.dependent.payments;

import java.math.BigDecimal;

public class Receipt {
    private final String paymentId;
    private final String reference;
    private final BigDecimal total;

    public Receipt(String paymentId, String reference, BigDecimal total) {
        this.paymentId = paymentId;
        this.reference = reference;
        this.total = total;
    }

    public String getPaymentId() {
        return paymentId;
    }

    public String getReference() {
        return reference;
    }

    public BigDecimal getTotal() {
        return total;
    }
}


