#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import coloredlogs


# 日志初始化
def init_log(filename):
    """
    :param filename  日志保存位置
    :return logger
    文件日志级别为info，前端日志级别为debug
    """
    formattler = '%(asctime)ss %(pathname)-8s:%(lineno)d %(levelname)-8s %(message)s'
    fmt = logging.Formatter(formattler)
    logger = logging.getLogger()
    coloredlogs.install(level=logging.DEBUG, fmt=formattler)
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
    try:
        logging.getLogger("scapy").setLevel(logging.WARNING)
        logging.getLogger("matplotlib").setLevel(logging.WARNING)
    except Exception as e:
        pass
    return logger
