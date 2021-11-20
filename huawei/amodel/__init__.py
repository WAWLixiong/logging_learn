from log_utils import LoggerFactory, LogMixin


class Base:
    """"""


class A(Base, LogMixin):

    def __init__(self):
        LoggerFactory.set_logger(self, 'huawei.A')

    def run(self):
        self.debug("A is debug")
        self.info("A is run")
        self.warning("A is warning")
        try:
            1 / 0
        except Exception as e:
            self.error("A is error")
