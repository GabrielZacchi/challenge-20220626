import subprocess
import psutil

def kill_process_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if process_name.lower() in proc.info['name'].lower():
            print(f'Process kill {proc.info["name"]} (PID: {proc.info["pid"]})')
            proc.kill()

kill_process_by_name('python manage.py runserver')

kill_process_by_name('python scheduler.py')

subprocess.Popen(['poetry', 'run', 'python', 'core/manage.py', 'runserver'])

subprocess.call(['poetry', 'run', 'python', 'core/scheduler.py'])
