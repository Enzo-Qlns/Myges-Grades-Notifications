import threading
import time
from datetime import datetime, timedelta

from core import marks_utils
from exceptions import ErrorResponse


class CronService:
    def __init__(self, myges_service, excel_service, mail_service) -> None:
        self.thread = None
        self.jobs = []
        self.running = False
        self.myges_service = myges_service
        self.excel_service = excel_service
        self.mail_service = mail_service
        self.lock = threading.Lock()  # Verrou pour éviter les exécutions concurrentes

    def add_job(self, func, interval_sec, *args, **kwargs):
        """
        Ajoute une nouvelle tâche au cron service.
        :param func: La fonction à exécuter.
        :param interval_sec: L'intervalle de temps en secondes entre chaque exécution.
        :param args: Les arguments de la fonction.
        :param kwargs: Les arguments nommés de la fonction.
        :return: None
        """
        job = {
            "func": func,
            "interval": timedelta(seconds=interval_sec),
            "next_run": datetime.now() + timedelta(seconds=interval_sec),
            "args": args,
            "kwargs": kwargs
        }
        self.jobs.append(job)

    def _run_jobs(self):
        """
        Méthode pour exécuter les tâches à intervalles réguliers.
        :return: None
        """
        while self.running:
            now = datetime.now()
            for job in self.jobs:
                if now >= job['next_run']:
                    # Lancer les tâches dans des threads séparés
                    threading.Thread(target=self._run_job, args=(job['func'], job['args'], job['kwargs'])).start()
                    job['next_run'] = now + job['interval']
            time.sleep(1)  # Petite pause pour éviter une boucle infinie trop rapide

    def _run_job(self, func, args, kwargs):
        """
        Méthode pour exécuter une tâche avec un verrouillage.
        :param func: La fonction à exécuter.
        :param args: Les arguments de la fonction.
        :param kwargs: Les arguments nommés de la fonction.
        :return: None
        """
        with self.lock:
            func(*args, **kwargs)

    def start(self):
        """
        Démarre le service cron pour exécuter les tâches à intervalles réguliers.
        :return: None
        """
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run_jobs, daemon=True)
            self.thread.start()

    def stop(self):
        """
        Arrête le service cron.
        :return: None
        """
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()

    def remove_job(self, func):
        """
        Supprime une tâche du cron service.
        :param func: La fonction à supprimer.
        :return: None
        """
        self.jobs = [job for job in self.jobs if job['func'] != func]

    def crontab_get_marks(self):
        """
        Fonction pour récuperer les notes.
        :return:
        """
        year = datetime.now().year

        # Récupérer les notes depuis MyGES
        grades = self.myges_service.get_grades(year=year)

        # Récupérer les anciennes notes depuis le fichier Excel
        old_grades = self.excel_service.get_grades()

        # Comparer les notes pour vérifier s'il y a des nouvelles notes
        differences_grades = marks_utils.compare_grades(grades, old_grades)

        # Comparer les notes pour vérifier s'il y a des nouvelles notes
        if differences_grades:
            # Supprimer toutes les notes du fichier Excel
            self.excel_service.delete_all_grades()
            time.sleep(1)

            # Enregistrer les nouvelles notes dans le fichier Excel
            self.excel_service.save_grades(grades)

            # Envoyer un e-mail avec les nouvelles notes
            try:
                self.mail_service.template_message(grades=differences_grades)
                print("E-mail envoyé avec succès !")
            except Exception as e:
                raise ErrorResponse(f"Erreur lors de l'envoi du message : {str(e)}")
        else:
            # Supprimer toutes les notes du fichier Excel
            self.excel_service.delete_all_grades()
            time.sleep(1)

            # Enregistrer les nouvelles notes dans le fichier Excel
            self.excel_service.save_grades(grades)
            current_date = datetime.now().strftime("%H:%M:%S")
            raise ErrorResponse(f"Pas de nouvelles notes à {str(current_date)}")