import logging
from logging.handlers import RotatingFileHandler

FILE_NAME = 'app.log'
MAX_BYTES = 5 * 1024 * 1024  # 5 MB
BACKUP_COUNT = 5  # Nombre de fichiers de sauvegarde


class LoggerService:
    def __init__(self):
        """
        Initialize the LoggerService with a log file.
        """
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
        Log a message with a specific type.
        :param log_type: The type of the log message.
        :param message: The message to log.
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
        else:
            raise ValueError(f"Unknown log type: {log_type}")

    def debug(self, message: str):
        self.log('debug', message)

    def info(self, message: str):
        self.log('info', message)

    def warning(self, message: str):
        self.log('warning', message)

    def error(self, message: str):
        self.log('error', message)

    def critical(self, message: str):
        self.log('critical', message)
