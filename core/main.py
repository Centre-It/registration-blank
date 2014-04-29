# -*- coding: utf-8 -*-
__author__ = 'bglebov'

import config

from notificator import EmailNotify
from logger import logger


def process_data(data):
    try:
        logger.info(data)

        for to in config.EMAILS:
            EmailNotify.send_registration_notify(to, data)

        return True
    except Exception as ex:
        logger.error(ex)
        return False