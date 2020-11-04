import os
import sys
import logbook
from logbook import Logger, StreamHandler, FileHandler, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


def log_type(record, handle):
    log = "[{date}] [{level}] [{filename}] [{func_name}] [{lineno}] {msg}".format(
        date=record.time,
        level=record.level_name,
        filename=os.path.split(record.filename)[-1],
        func_name=record.func_name,
        lineno=record.lineno,
        msg=record.message
    )
    return log
#日志存放
LOG_DIR=os.path.join("Log")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
#日志打印到屏幕
log_std=ColorizedStderrHandler(bubble=True)
log_std.formatter=log_type
#日志打印到文件
log_file=TimedRotatingFileHandler(
    os.path.join(LOG_DIR,'%s.log' % 'log'),date_format='%Y-%m-%d',bubble=True,encoding='utf-8')
log_file.formatter=log_type
#脚本日志
run_log=Logger("script_log")
def init_logger():
    logbook.set_datetime_format("local")
    run_log.handlers=[]
    run_log.handlers.append(log_file)
    run_log.handlers.append(log_std)

#实例化，默认使用
logger=init_logger()
logger.info("测试log")