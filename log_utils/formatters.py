from logging import Formatter


class ColorFormatter(Formatter):
    fmt = "{asctime}:{name}:{pathname}:{funcName}:{lineno}:{threadName}:{levelname} | {message}"
    datefmt = '%Y-%m-%d %H:%M:%S'
    log_colors = {
        'CRITICAL': '\033[0;31m',
        'ERROR': '\033[0;33m',
        'WARNING': '\033[0;35m',
        'INFO': '\033[0;32m',
        'DEBUG': '\033[0;00m',
    }

    def __init__(self, style='{', validate=True):
        super().__init__(fmt=self.fmt, datefmt=self.datefmt, style=style, validate=validate)

    def format(self, record):
        s = super().format(record)
        level_name = record.levelname
        if level_name not in self.log_colors:
            return s
        return self.log_colors[level_name] + s + '\033[0m'


class OrdinaryFormatter(Formatter):
    fmt = "{asctime}:{name}:{pathname}:{funcName}:{lineno}:{threadName}:{location}:{levelname} | {message}"
    datefmt = '%Y-%m-%d %H:%M:%S'

    def __init__(self, style='{', validate=True):
        super().__init__(fmt=self.fmt, datefmt=self.datefmt, style=style, validate=validate)

