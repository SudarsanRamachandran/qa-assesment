import psutil
import logging

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

def check_cpu_usage(threshold=80):
    usage = psutil.cpu_percent()
    if usage > threshold:
        logging.warning(f"CPU usage is {usage}%, which exceeds the threshold of {threshold}%.")

def check_memory_usage(threshold=80):
    memory = psutil.virtual_memory()
    if memory.percent > threshold:
        logging.warning(f"Memory usage is {memory.percent}%, which exceeds the threshold of {threshold}%.")

def check_disk_usage(threshold=90):
    disk = psutil.disk_usage('/')
    if disk.percent > threshold:
        logging.warning(f"Disk usage is {disk.percent}%, which exceeds the threshold of {threshold}%.")

def check_running_processes():
    processes = len(psutil.pids())
    logging.info(f"Number of running processes: {processes}")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
