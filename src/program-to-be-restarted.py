import logging
import os
from crontab import CronTab
from datetime import datetime, timedelta

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_cron():
    cron = CronTab(user='<user>')

    now = datetime.now() 
    kill_time = now + timedelta(seconds=70)
    run_time = now + timedelta(seconds=131)

    kill_job = cron.new(command='bash <path-to-killer.sh>/killer.sh')
    kill_job.day.every(1)
    kill_job.hour.on(kill_time.hour)
    kill_job.minute.on(kill_time.minute)
    cron.write()

    run_job = cron.new(command='bash <path-to-runner.sh>/runner.sh')
    run_job.day.every(1)
    run_job.hour.on(run_time.hour)
    run_job.minute.on(run_time.minute)
    cron.write()

    
def clear_cron():
    "clears all crons. If you have more crontabs running dont do this."
    cron = CronTab(user='<user>')
    cron.remove_all()
    cron.write()

    
if __name__ == '__main__':
    clear_cron()
    while True:
      if input("Enter RESET if you need to") == "RESET":
        create_cron()
        logger.info("Cronjob created. Restarting...")
      else:
        print("Running...")
