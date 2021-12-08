import logging
from logging import (
    FileHandler,
    StreamHandler,
)
import sys


from log_utils.formatters import ColorFormatter
from log_utils.filters import (
    NormalFilter,
    ErrorFilter,
)


def test1():
    # root的level是warning
    logging.info("hello")


def test2():
    # 先检查你消费的有没有满足你爸爸的要求
    # 再检查你消费的是不是满足消费场所的要求
    logger = logging.getLogger(__name__)  # 爸爸今天不管你花多少钱
    logger.setLevel(20)  # 爸爸说你出去最低给我花20
    handler = StreamHandler(sys.stderr)  # 超市默认不设置最低消费
    handler.setLevel(30)  # 设置场所消费门槛30块起步
    logger.addHandler(handler)
    logger.error("hello world")  # 你出去消费40元
    logger.warning("how are you ")  # 你出去消费30元
    logger.info("hi")  # 你出去消费20元
    logger.debug("niu")  # 你出去消费10元, 不满足要求


def test3():
    logger = logging.getLogger(__name__)
    logger.setLevel(20)

    normal_file_handler = FileHandler('normal.log')
    normal_file_handler.setLevel(20)
    normal_filter = NormalFilter()
    normal_file_handler.addFilter(normal_filter)
    normal_file_handler.setFormatter(ColorFormatter())

    logger.addHandler(normal_file_handler)

    error_file_handler = FileHandler('error.log')
    error_file_handler.setLevel(20)
    error_filter = ErrorFilter()
    error_file_handler.addFilter(error_filter)
    error_file_handler.setFormatter(ColorFormatter())

    logger.addHandler(error_file_handler)

    logger.debug("nonono")
    logger.info("hello")
    logger.warning("world")
    logger.error("error occurs")


def test4():
    """配置形式参考：https://blog.csdn.net/qq_35556064/article/details/103995651"""


if __name__ == '__main__':
    test2()
