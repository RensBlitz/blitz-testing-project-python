package org.example.dependent.notifications;

import java.util.HashMap;
import java.util.Map;

public class EmailService {
    private final TemplateRenderer templateRenderer;
    private final SmtpClient smtpClient;

    public EmailService(TemplateRenderer templateRenderer, SmtpClient smtpClient) {
        this.templateRenderer = templateRenderer;
        this.smtpClient = smtpClient;
    }

    public String sendOrderConfirmation(String orderId, String toEmail) {
        Map<String, Object> data = new HashMap<>();
        data.put("orderId", orderId);

        String subject = "Your order " + orderId + " is confirmed";
        String body = templateRenderer.render("order_confirmation", data);
        return smtpClient.send(toEmail, subject, body);
    }

    public String sendPasswordReset(String token, String toEmail) {
        Map<String, Object> data = new HashMap<>();
        data.put("token", token);

        String subject = "Password reset instructions";
        String body = templateRenderer.render("password_reset", data);
        return smtpClient.send(toEmail, subject, body);
    }
}


