import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, sender_email, receiver_email, smtp_server, smtp_port, smtp_username, smtp_password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def send_email(self, subject, message):
        # Create a MIMEText object to represent the email
        msg = MIMEMultipart()
        msg["From"] = self.sender_email
        msg["To"] = self.receiver_email
        msg["Subject"] = subject

        # Attach the message to the email
        msg.attach(MIMEText(message, "plain"))

        # Create an SMTP session to send the email
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure one (TLS)
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, self.receiver_email, msg.as_string())
