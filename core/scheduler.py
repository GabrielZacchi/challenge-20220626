import subprocess
import schedule
import time

def run_crawl_command():
    subprocess.call(['poetry', 'run', 'python', 'core/manage.py', 'crawl'])

schedule.every().day.at("20:06").do(run_crawl_command)

while True:
    schedule.run_pending()
    time.sleep(1)
