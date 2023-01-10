class Error(Exception):
    pass


class MissingRequiredFieldError(Error):
    def __init__(self, message="Missing required field", data=None):
        self.message = message
        self.data = data
        super().__init__(self.message)
