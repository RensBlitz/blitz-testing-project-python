package org.example.dependent.payments;

import java.math.BigDecimal;

public class Cart {
    private final BigDecimal subtotal;
    private final String reference;

    public Cart(BigDecimal subtotal, String reference) {
        if (subtotal == null) {
            throw new IllegalArgumentException("Subtotal cannot be null");
        }
        if (subtotal.compareTo(BigDecimal.ZERO) < 0) {
            throw new IllegalArgumentException("Subtotal cannot be negative");
        }
        this.subtotal = subtotal;
        this.reference = reference == null ? "" : reference;
    }

    public BigDecimal getSubtotal() {
        return subtotal;
    }

    public String getReference() {
        return reference;
    }
}


