import logging
import time
from logging import handlers
# from logging import StreamHandler

# logger = logging.getLogger(__name__)
logger = logging.getLogger("TEST")
# print(logger)

# 定义文件名
log_file = "rotate.log"

# 定义文件存储 10字节，最多备份3个文件，多余自动删除
# fh = handlers.RotatingFileHandler(filename=log_file,maxBytes=10,backupCount=3)

#按照时间分隔文件         when秒s可换成midnight 就是每天凌晨        间隔时间   保留3个文件
fh = handlers.TimedRotatingFileHandler(filename=log_file,when='S',interval=3,backupCount=3,encoding="utf-8")

formatter = logging.Formatter(' %(asctime)s - %(message)s')  # 定义日期格式
#

fh.setFormatter(formatter)  # 设置日志输出日期格式

logger.addHandler(fh)

logger.warning("test1")
time.sleep(2)
logger.warning("test2")
time.sleep(2)
logger.warning("test3")
time.sleep(2)
logger.warning("test4")
