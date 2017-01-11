# -*- coding:utf-8 -*-


class ValidationError(Exception):

    def __init__(self, message):
        self.message = message
