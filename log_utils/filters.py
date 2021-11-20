from logging import Filter
import logging


class NormalFilter(Filter):

    def filter(self, record):
        if record.levelno <= logging.WARNING:
            # 儿童场所最多消费30
            return True
        return False


class ErrorFilter(Filter):
    def filter(self, record):
        if record.levelno > logging.WARNING:
            # 成人场所消费门槛至少30起步
            return True
        return False
