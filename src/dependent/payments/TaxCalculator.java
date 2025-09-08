package org.example.dependent.payments;

import java.math.BigDecimal;

public class TaxCalculator {
    public BigDecimal calculateTotalWithTax(Cart cart, String currency) {
        if (cart == null) {
            throw new IllegalArgumentException("Cart cannot be null");
        }
        BigDecimal subtotal = cart.getSubtotal();
        BigDecimal taxRate = new BigDecimal("0.20");
        BigDecimal tax = subtotal.multiply(taxRate);
        return subtotal.add(tax);
    }
}


