# -*- coding: utf-8 -*-
__author__ = 'Boris'

import logging
import config as settings

#
# Конфигурируем объект для логирования
#
logger = logging.getLogger("worker_log")
logger.setLevel(logging.INFO)

# File Handler
fh = logging.FileHandler(settings.LOG_PATH)
fh.setLevel(logging.INFO)

# Console Handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)


def error(method, ex):
    logger.info(u'===============================================\n')
    logger.error(u'\nMethod: {0}()\nType: Error\nMessage: {1}\n'.format(method, ex))