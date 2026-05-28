"""SMTP delivery with console fallback when SMTP_HOST is not set."""

import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from utils.config import settings

logger = logging.getLogger(__name__)


def send_email(to: str, subject: str, body: str) -> None:
    """Send plain-text email via SMTP or log when SMTP is disabled."""
    if not settings.smtp_enabled:
        logger.info("EMAIL (dev) to=%s subject=%s\n%s", to, subject, body)
        return

    msg = MIMEMultipart()
    msg["From"] = settings.SMTP_FROM
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
        if settings.SMTP_USE_TLS:
            server.starttls()
        if settings.SMTP_USER:
            server.login(settings.SMTP_USER, settings.SMTP_PASSWORD)
        server.sendmail(settings.SMTP_FROM, [to], msg.as_string())


def send_password_reset_email(to: str, token: str) -> None:
    """Link targets frontend route that calls POST /auth/reset-password."""
    link = f"{settings.FRONTEND_URL}/reset-password?token={token}"
    send_email(
        to,
        "LSWIS – Password reset",
        f"Use this link to reset your password (valid for {settings.RESET_TOKEN_EXPIRE_MINUTES} min):\n{link}",
    )


def send_registration_confirm_email(to: str, token: str, event_title: str) -> None:
    """Link targets frontend route that calls POST /registrations/confirm."""
    link = f"{settings.FRONTEND_URL}/confirm-registration?token={token}"
    send_email(
        to,
        f"LSWIS – Confirm signup: {event_title}",
        f"Confirm your registration for '{event_title}':\n{link}",
    )


def send_registration_cancelled_email(to: str, event_title: str) -> None:
    send_email(
        to,
        f"LSWIS – Registration cancelled: {event_title}",
        f"Your registration for '{event_title}' has been cancelled.",
    )


def send_new_signup_notify_organizer(to: str, event_title: str, volunteer_name: str) -> None:
    send_email(
        to,
        f"LSWIS – New signup: {event_title}",
        f"{volunteer_name} signed up for '{event_title}'.",
    )
