import time

from services.logger_service import FILE_NAME


def run():
    from services.cron_service import CronService
    from services.excel_service import ExcelService
    from services.mail_service import MailService
    from services.myges_service import MyGESService
    from services.logger_service import LoggerService

    myges_service = MyGESService()
    excel_service = ExcelService(filename="grades.xlsx")
    logger = LoggerService(FILE_NAME)
    mail_service = MailService(logger=logger)
    cron_service = CronService(
        myges_service=myges_service,
        excel_service=excel_service,
        mail_service=mail_service,
    )

    # Ajouter une tâche pour récupérer les notes toutes les 5 secondes
    cron_service.add_job(cron_service.crontab_get_marks, interval_sec=5)

    # Démarrer le service cron
    cron_service.start()

    # Garder le script en cours d'exécution
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        cron_service.stop()


if __name__ == "__main__":
    run()
