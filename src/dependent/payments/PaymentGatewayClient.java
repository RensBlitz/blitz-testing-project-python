package org.example.dependent.payments;

import java.math.BigDecimal;

public class PaymentGatewayClient {
    public String charge(BigDecimal amount, String currency, String reference) {
        if (amount == null || amount.compareTo(BigDecimal.ZERO) <= 0) {
            throw new IllegalArgumentException("Amount must be positive");
        }
        if (currency == null || currency.isEmpty()) {
            throw new IllegalArgumentException("Currency must be provided");
        }
        return "pay_" + Math.abs((amount.toPlainString() + currency + reference).hashCode());
    }
}


