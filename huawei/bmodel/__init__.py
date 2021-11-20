from log_utils import LoggerFactory, LogMixin


class Base:
    """"""


class B(Base, LogMixin):

    def __init__(self):
        LoggerFactory.set_logger(self, 'huawei.B')

    def run(self):
        self.debug("B is debug")
        self.info("B is run")
        self.warning("B is warning")
        try:
            1 / 0
        except Exception as e:
            self.error("B is error")
