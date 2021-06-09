class PrintfulException(Exception):
    pass


class PrintfulApiException(PrintfulException):
    pass


class InvalidResponse(PrintfulException):
    pass
