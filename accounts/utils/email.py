import resend
import os

# Set API key
resend.api_key = os.getenv("RESEND_API_KEY")

def send_resend_email(to, subject, html_body):
    try:
        params = {
            "from": "info@bnunited.com",  # must match verified domain
            "to": [to],
            "subject": subject,
            "html": html_body,
        }
        email = resend.Emails.send(params)
        return email  # contains id/status
    except Exception as e:
        import logging
        logging.error(f"Resend email failed: {e}")
        return None
