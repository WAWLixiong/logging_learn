from log_utils import LogMixin, LoggerFactory


class MyException(Exception):
    def __str__(self):
        return "my exception"

    __repr__ = __str__


class HuaWei(LogMixin):
    def __init__(self):
        LoggerFactory.set_logger(self, 'huawei')

    def run(self):
        self.debug("huawei is debug")
        self.info("huawei is run")
        self.warning("huawei is warning")
        try:
            raise MyException()
        except MyException:
            self.error("huawei")
