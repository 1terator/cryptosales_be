class BaseAuthorizationException(Exception):
    message = "Unknown authorization error"
    code = 500


class MessageDoesNotExist(BaseAuthorizationException):
    message = "Current message does not exist"
    code = 404


class SessionDoesNotExist(BaseAuthorizationException):
    message = "Current session does not exist"
