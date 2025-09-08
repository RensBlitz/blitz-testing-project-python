import pytest
from unittest.mock import create_autospec

from dependent.notifications.email_service import EmailService
from dependent.notifications.smtp_client import SmtpClient
from dependent.notifications.template_renderer import TemplateRenderer


class TestEmailService:
    def setup_method(self) -> None:
        self.template_renderer = create_autospec(TemplateRenderer)
        self.smtp_client = create_autospec(SmtpClient)
        self.email_service = EmailService(self.template_renderer, self.smtp_client)

    def test_send_order_confirmation_with_valid_input_should_render_template_and_send_email(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "rendered"
        self.smtp_client.send.return_value = "msg-123"

        # Act
        result = self.email_service.send_order_confirmation("ORD123", "user@example.com")

        # Assert
        assert result == "msg-123"
        self.template_renderer.render.assert_called_once()
        args, kwargs = self.template_renderer.render.call_args
        assert args[0] == "order_confirmation"
        assert args[1]["orderId"] == "ORD123"
        self.smtp_client.send.assert_called_once_with(
            "user@example.com", "Your order ORD123 is confirmed", "rendered"
        )

    def test_send_order_confirmation_with_different_order_id_should_use_correct_order_id_in_template(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "R"
        self.smtp_client.send.return_value = "msg-1"

        # Act
        self.email_service.send_order_confirmation("ORD999", "a@b.com")

        # Assert
        args, kwargs = self.template_renderer.render.call_args
        assert args[0] == "order_confirmation"
        assert args[1]["orderId"] == "ORD999"

    def test_send_order_confirmation_when_template_rendering_fails_should_propagate_exception(self) -> None:
        # Arrange
        self.template_renderer.render.side_effect = RuntimeError("boom")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.email_service.send_order_confirmation("ORD1", "to@example.com")
        self.smtp_client.send.assert_not_called()

    def test_send_order_confirmation_when_smtp_sending_fails_should_propagate_exception(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "rendered"
        self.smtp_client.send.side_effect = RuntimeError("smtp down")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.email_service.send_order_confirmation("ORD1", "to@example.com")

    def test_send_password_reset_with_valid_input_should_render_template_and_send_email(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "rendered"
        self.smtp_client.send.return_value = "msg-abc"

        # Act
        result = self.email_service.send_password_reset("token-123", "user@example.com")

        # Assert
        assert result == "msg-abc"
        self.template_renderer.render.assert_called_once()
        args, kwargs = self.template_renderer.render.call_args
        assert args[0] == "password_reset"
        assert args[1]["token"] == "token-123"
        self.smtp_client.send.assert_called_once_with(
            "user@example.com", "Password reset instructions", "rendered"
        )

    def test_send_password_reset_with_different_token_should_use_correct_token_in_template(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "R"
        self.smtp_client.send.return_value = "msg-1"

        # Act
        self.email_service.send_password_reset("tok-xyz", "a@b.com")

        # Assert
        args, kwargs = self.template_renderer.render.call_args
        assert args[0] == "password_reset"
        assert args[1]["token"] == "tok-xyz"

    def test_send_password_reset_when_template_rendering_fails_should_propagate_exception(self) -> None:
        # Arrange
        self.template_renderer.render.side_effect = RuntimeError("boom")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.email_service.send_password_reset("t", "to@example.com")
        self.smtp_client.send.assert_not_called()

    def test_send_password_reset_when_smtp_sending_fails_should_propagate_exception(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "rendered"
        self.smtp_client.send.side_effect = RuntimeError("smtp down")

        # Act & Assert
        with pytest.raises(RuntimeError):
            self.email_service.send_password_reset("t", "to@example.com")

    def test_multiple_emails_sent_should_call_dependencies_correctly(self) -> None:
        # Arrange
        self.template_renderer.render.return_value = "rendered"
        self.smtp_client.send.side_effect = ["m1", "m2", "m3"]

        # Act
        r1 = self.email_service.send_order_confirmation("O1", "a@b.com")
        r2 = self.email_service.send_password_reset("T2", "a@b.com")
        r3 = self.email_service.send_order_confirmation("O3", "a@b.com")

        # Assert
        assert [r1, r2, r3] == ["m1", "m2", "m3"]
        assert self.template_renderer.render.call_count == 3
        assert self.smtp_client.send.call_count == 3
