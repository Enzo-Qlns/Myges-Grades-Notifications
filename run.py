import time

from config import settings

from services.telegram_service import TelegramService
from services.cron_service import CronService
from services.csv_service import CSVManager
from services.myges_service import MyGESService
from services.logger_service import LoggerService


def run():

    myges_service = MyGESService()
    csv_service = CSVManager(filename="grades.csv")
    logger = LoggerService()
    telegram_service = TelegramService(
        token=settings.TELEGRAM_BOT_TOKEN,
        channel_id=settings.TELEGRAM_CHANNEL_ID,
        logger=logger
    )
    cron_service = CronService(
        myges_service=myges_service,
        csv_service=csv_service,
        telegram_service=telegram_service,
    )

    # Add a task to get the grades every 5 seconds
    cron_service.add_job(cron_service.crontab_get_marks, interval_sec=1)

    # Add cron job
    cron_service.start()

    # Keep the script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cron_service.stop()


if __name__ == "__main__":
    print("Starting the script...")
    run()
