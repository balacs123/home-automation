class AppException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class CLIBaseException(Exception):
    """
    CLIBaseException
    """
    def __init__(self, message):
        """
        :param message: error message
        """
        self.message = message
        super(CLIBaseException, self).__init__()
