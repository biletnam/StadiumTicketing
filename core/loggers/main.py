import logging


class MyLogger(object):
    def __init__(self, name):
        self.logger = logging.Logger(name)
        self.logger.setLevel(logging.DEBUG)

        logger_handler = logging.FileHandler("app_log.log")
        logger_handler.setLevel(logging.DEBUG)

        logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logger_handler.setFormatter(logger_formatter)

        logger_stream = logging.StreamHandler()
        logger_stream.setLevel(logging.DEBUG)

        self.logger.addHandler(logger_handler)
        self.logger.addHandler(logger_stream)
