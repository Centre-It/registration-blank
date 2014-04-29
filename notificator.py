# -*- coding: utf-8 -*-
__author__ = 'bglebov'

import smtplib
import os

from flask import request
from email.mime.text import MIMEText
from jinja2 import Template
from logger import error


class EmailNotify:
    def __init__(self, host, port, you, username, password, is_auth=True):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.you = you
        self.is_auth = is_auth

    def send_msg(self, to, subject, message):
        letter = MIMEText(message, 'html', 'UTF-8')

        letter['Subject'] = subject
        letter['From'] = self.you
        letter['To'] = to.encode('idna')

        s = smtplib.SMTP(self.host, self.port)

        try:
            if self.is_auth:
                s.login(self.username, self.password)

            s.sendmail(self.username, [letter['To']], letter.as_string())
        except Exception as ex:
            from logger import error
            error(u'send_msg', ex)
        finally:
            s.quit()

    @staticmethod
    def send_registration_notify(to, person):
        smtp = EmailNotify.default()

        template = EmailNotify._load_template(u'signup_form.html')

        try:
            smtp.send_msg(to, u'Регистрация на конференцию', template.render(person=person))
        except Exception as ex:
            error('send_change_email_notify', ex)

    @staticmethod
    def u(unicode_str):
        return unicode_str.encode('utf-8')

    @staticmethod
    def _load_template(template_name):
        current_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))

        with open(u'{0}\\emails\\{1}'.format(current_path, template_name)) as f:
            template_str = u'{0}'.format(unicode(f.read(), 'utf8'))

            return Template(template_str)

    @staticmethod
    def default():
        import config

        return EmailNotify(config.SMTP['host'],
                           config.SMTP['port'],
                           config.SMTP['from'],
                           config.SMTP['username'],
                           config.SMTP['password'],
                           False)


if __name__ == '__main__':

    EmailNotify.send_registration_notify(u'Boris.Glebov@centre-it.com', u'Иван Факов')

    print 'send email'