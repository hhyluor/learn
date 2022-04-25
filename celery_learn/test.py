import logging

logging.basicConfig(
    filename="run.log", level=logging.DEBUG
)  # 实现了日志配置

logging.info("我是日志1")
logging.warning("我是日志2")
logging.error("我是日志3")
logging.debug("我是日志4")
