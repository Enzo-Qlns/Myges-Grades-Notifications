from services.logger_service import LoggerService, FILE_NAME

logger = LoggerService(FILE_NAME)


class BaseResponse(Exception):
    def __init__(self, message: str = None):
        self.message = message


class ErrorResponse(BaseResponse):
    def __init__(self, message: str = None):
        super().__init__(message)

        logger.error(f"{self.message}")
