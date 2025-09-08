package org.example.dependent.notifications;

public class SmtpClient {
    private final String host;
    private final int port;

    public SmtpClient(String host, int port) {
        if (host == null || host.isEmpty()) {
            throw new IllegalArgumentException("SMTP host must be provided");
        }
        if (port <= 0) {
            throw new IllegalArgumentException("SMTP port must be positive");
        }
        this.host = host;
        this.port = port;
    }

    public String send(String to, String subject, String body) {
        if (to == null || to.isEmpty()) {
            throw new IllegalArgumentException("Recipient must be provided");
        }
        if (subject == null) {
            throw new IllegalArgumentException("Subject cannot be null");
        }
        if (body == null) {
            throw new IllegalArgumentException("Body cannot be null");
        }
        return "msg-" + Math.abs((to + subject + body + host + port).hashCode());
    }
}


