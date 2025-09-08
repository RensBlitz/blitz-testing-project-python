from typing import Any, Dict

from .template_renderer import TemplateRenderer
from .smtp_client import SmtpClient


class EmailService:
    def __init__(self, template_renderer: TemplateRenderer, smtp_client: SmtpClient) -> None:
        self._template_renderer = template_renderer
        self._smtp_client = smtp_client

    def send_order_confirmation(self, order_id: str, to_email: str) -> str:
        data: Dict[str, Any] = {"orderId": order_id}
        subject = f"Your order {order_id} is confirmed"
        body = self._template_renderer.render("order_confirmation", data)
        return self._smtp_client.send(to_email, subject, body)

    def send_password_reset(self, token: str, to_email: str) -> str:
        data: Dict[str, Any] = {"token": token}
        subject = "Password reset instructions"
        body = self._template_renderer.render("password_reset", data)
        return self._smtp_client.send(to_email, subject, body)
