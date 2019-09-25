# -*- coding: utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler


#设置日志
#NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL

class LogManager(object):
    logFormat = '[%(asctime)s][%(filename)s][pid:%(process)d][tid:%(thread)d][func:%(funcName)s][line:%(lineno)d][%(levelname)s] %(message)s'

    @classmethod
    def getRollLog(cls, fileName, logName, backupCount=9, isConsole=False):

        logger = logging.getLogger(logName)

        formatter = logging.Formatter(cls.logFormat)
        handler = RotatingFileHandler(fileName, maxBytes=16*1024*1024, backupCount=backupCount)
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        if isConsole:
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            logger.addHandler(console)

        #默认设置为INFO, 返回后可自己行设置
        logger.setLevel(logging.INFO)

        return logger

    @classmethod
    def getDayLog(cls, fileName, logName, isConsole=False):

        logger = logging.getLogger(logName)

        formatter = logging.Formatter(cls.logFormat)
        handler = TimedRotatingFileHandler(fileName, when="d")
        handler.setFormatter(formatter)

        logger.addHandler(handler)

        if isConsole:
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            logger.addHandler(console)

        # 默认设置为INFO, 返回后可自己行设置
        logger.setLevel(logging.INFO)

        return logger


roll_log = LogManager.getRollLog(fileName="ner_extract.log", logName="ner_extract", isConsole=True)

