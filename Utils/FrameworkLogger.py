import logging


class FrameworkLogger:
    """Class representing the logging functionality for the Framework"""

    LOG_FILE_PATH = ".\\Logs\\FrameworkLog.log"
    LOG_LEVEL = logging.INFO
    LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"

    def get_framework_logger(self):
        """ returns the logger for logging """
        logging.basicConfig(filename=self.LOG_FILE_PATH,
                            filemode='w',
                            level=self.LOG_LEVEL,
                            format=self.LOG_FORMAT,
                            force=True)
        framework_logger = logging.getLogger("FrameworkLogger")
        return framework_logger
