from requests import Response


class MiroException(Exception):

    def __init__(self, status: int, details: str = ''):
        self.status = status
        self.details = details

    def __init__(self, cause: Exception):
        super(MiroException, self).__init__(cause)


class InvalidCredentialsException(MiroException):
    """An authentication error occurred because of bad credentials."""


class ObjectNotFoundException(MiroException):
    """The requested object was not found."""


class UnexpectedResponseException(MiroException):
    """The response has an unexpected code or data"""


class InsufficientPermissions(MiroException):
    """Not enough permissions to perform a certain action"""


def get_json_or_raise_exception(response: Response) -> dict:
    if is_2xx_status_code(response.status_code):
        return response.json()

    if response.status_code == 401:
        raise InvalidCredentialsException(response.status_code, response.text)

    if response.status_code == 403:
        raise InsufficientPermissions(response.status_code, response.text)

    if response.status_code == 404:
        raise ObjectNotFoundException(response.status_code, response.text)

    if is_5xx_status_code(response.status_code):
        raise MiroException(response.status_code, response.text)

    raise UnexpectedResponseException(response.status_code, response.text)


def is_2xx_status_code(status_code: int) -> bool:
    return str(status_code).startswith('2')


def is_5xx_status_code(status_code: int) -> bool:
    return str(status_code).startswith('5')
