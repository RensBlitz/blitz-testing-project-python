package org.example.dependent.payments;

import java.math.BigDecimal;

public class ReceiptGenerator {
    public Receipt generate(String paymentId, Cart cart, BigDecimal totalWithTax) {
        return new Receipt(paymentId, cart.getReference(), totalWithTax);
    }
}


