import subprocess
import schedule
import time
import logging
from environment.environment import env
from emailSender import EmailSender

def run_crawl_command():
    try:
        subprocess.call(['poetry', 'run', 'python', 'core/manage.py', 'crawl'])
    except Exception as e:
        # Log the exception
        logger = logging.getLogger(__name__)
        logger.error(f"An error occurred during the crawl command execution: {e}")

        # Send an email alert
        if (bool(eval(env('ENABLE_EMAIL_LOG')))):
            try:
                subject = "Scheduler Error Alert"
                message = f"An error occurred during the crawl command execution: {e}"
                email_sender = EmailSender(
                    env('SENDER_EMAIL'), 
                    env('RECEIVER_EMAIL'),
                    env('SMTP_SERVER'), 
                    env('SMTP_PORT'), 
                    env('SENDER_EMAIL_USERNAME'), 
                    env('SENDER_EMAIL_PASSWORD')
                )
                email_sender.send_email(subject, message)
            except Exception as e:
                # Log the exception
                logger = logging.getLogger(__name__)
                logger.error(f"An error occurred during send an email alert: {e}")

schedule.every().day.at(env('RUN_TIME')).do(run_crawl_command)

if __name__ == "__main__":
    logging.basicConfig(filename="scheduler.log", level=logging.ERROR)
    while True:
        schedule.run_pending()
        time.sleep(1)
