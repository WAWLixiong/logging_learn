import logging


class LoggerFactory:
    @classmethod
    def set_logger(cls, self, name):
        if hasattr(self, 'logger'):
            return getattr(self, 'logger')
        logger = logging.getLogger(name)
        logger.location = "<*****>"
        setattr(self, 'logger', logger)


class LogMixin:
    def debug(self, msg):
        self.logger.debug(msg, extra={"location": self.logger.location}, stacklevel=2)

    def info(self, msg):
        self.logger.info(msg, extra={"location": self.logger.location}, stacklevel=2)

    def warning(self, msg):
        self.logger.warning(msg, extra={"location": self.logger.location}, stacklevel=2)

    def error(self, msg):
        self.logger.error(msg, extra={"location": self.logger.location}, exc_info=1, stacklevel=2)

    def critical(self, msg):
        self.logger.critical(msg, extra={"location": self.logger.location}, stacklevel=2)

