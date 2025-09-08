package org.example.dependent.payments;

import java.math.BigDecimal;

public class CheckoutService {
    private final TaxCalculator taxCalculator;
    private final PaymentGatewayClient paymentGatewayClient;
    private final ReceiptGenerator receiptGenerator;

    public CheckoutService(TaxCalculator taxCalculator,
                           PaymentGatewayClient paymentGatewayClient,
                           ReceiptGenerator receiptGenerator) {
        this.taxCalculator = taxCalculator;
        this.paymentGatewayClient = paymentGatewayClient;
        this.receiptGenerator = receiptGenerator;
    }

    public Receipt processCheckout(Cart cart, String currency) {
        BigDecimal totalWithTax = taxCalculator.calculateTotalWithTax(cart, currency);
        String paymentId = paymentGatewayClient.charge(totalWithTax, currency, cart.getReference());
        return receiptGenerator.generate(paymentId, cart, totalWithTax);
    }
}


