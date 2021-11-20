from huawei import HuaWei
from huawei.amodel import A
from huawei.bmodel import B
import logging.config
import json


if __name__ == '__main__':
    # 启动项目先初始化日志
    with open("configs/logconfig.json5") as f:
        logging.config.dictConfig(json.load(f))

    # 项目运行
    huawei = HuaWei()
    # logger`huawei.A` 的parent是 `huawei`, 冒泡(propagate)打开的话`huawei.A`的日志也会经过`huawei`的处理
    # `huawei`的parent是root
    a = A()
    b = B()

    huawei.run()
    a.run()
    b.run()
