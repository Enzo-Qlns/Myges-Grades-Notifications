import logging
from logging.handlers import RotatingFileHandler

FILE_NAME = 'app.log'
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 5  # Number of backup files
MAX_LINES = 1000  # Maximum number of lines in the log file


class LoggerService:
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # Create rotating file handler which logs even debug messages
        fh = RotatingFileHandler(FILE_NAME, maxBytes=MAX_BYTES, backupCount=BACKUP_COUNT)
        fh.setLevel(logging.DEBUG)

        # Create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        # Create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def log(self, log_type: str, message: str):
        """
        Log un message avec le type de log spécifié.
        :param log_type: Le type de log (debug, info, warning, error, critical).
        :param message: Le message à log.
        :return: None
        """
        log_methods = {
            'debug': self.logger.debug,
            'info': self.logger.info,
            'warning': self.logger.warning,
            'error': self.logger.error,
            'critical': self.logger.critical
        }

        if log_type in log_methods:
            log_methods[log_type](message)
            self._truncate_log_file_if_needed()
        else:
            raise ValueError(f"Unknown log type: {log_type}")

    @staticmethod
    def _truncate_log_file_if_needed():
        """
        Truncate le fichier de log si le nombre de lignes dépasse MAX_LINES.
        """
        with open(FILE_NAME, 'r') as file:
            lines = file.readlines()

        if len(lines) > MAX_LINES:
            with open(FILE_NAME, 'w') as file:
                file.writelines(lines[-MAX_LINES:])

    def debug(self, message: str):
        """
        Log un message de debug.
        :param message: Le message à log
        :return:
        """
        self.log('debug', message)

    def info(self, message: str):
        """
        Log un message d'info.
        :param message: Le message à log
        :return:
        """
        self.log('info', message)

    def warning(self, message: str):
        """
        Log a warning message.
        :param message: Le message à log
        :return:
        """
        self.log('warning', message)

    def error(self, message: str):
        """
        Log un message d'erreur.
        :param message: Le message à log
        :return:
        """
        self.log('error', message)

    def critical(self, message: str):
        """
        Log un message critique.
        :param message: Le message à log
        :return:
        """
        self.log('critical', message)
