package org.example.dependent.notifications;

import java.util.Map;

public class TemplateRenderer {
    public String render(String templateName, Map<String, Object> data) {
        StringBuilder builder = new StringBuilder();
        builder.append("TEMPLATE[").append(templateName).append("]:");
        for (Map.Entry<String, Object> entry : data.entrySet()) {
            builder.append(entry.getKey()).append("=").append(String.valueOf(entry.getValue())).append(";");
        }
        return builder.toString();
    }
}


