'''This module does HTTP requests settings and error handling.'''

from functools import wraps
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry
from fastapi import status

from helpers.api_exceptions import ResponseValidationError


DEFAULT_TIMEOUT = 5  # seconds
DEFAULT_RETRIES = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    method_whitelist=['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS']
)


class TimeoutHTTPAdapter(HTTPAdapter):
    '''Set up HTTP requests timeouts and retries.'''

    def __init__(self, *args, **kwargs):
        self.timeout = DEFAULT_TIMEOUT
        self.max_retries = DEFAULT_RETRIES

        if 'timeout' in kwargs:
            self.timeout = kwargs['timeout']
            del kwargs['timeout']

        if 'max_retries' in kwargs:
            self.max_retries = kwargs['max_retries']
            del kwargs['max_retries']

        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get('timeout')

        if timeout is None:
            kwargs['timeout'] = self.timeout

        return super().send(request, **kwargs)


def error_handler(func):
    '''Decorator that displays try/except errors from the HTTP requests.'''

    @wraps(func)
    def wrapper(*args, **kwargs):  # pylint: disable=[R1710]
        try:
            return func(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            return ResponseValidationError(
                status_code=status.HTTP_400_BAD_REQUEST,
                message=str(e)
            )
        except requests.exceptions.ConnectionError as e:
            return ResponseValidationError(
                status_code=status.HTTP_404_NOT_FOUND,
                message=str(e)
            )
        except requests.exceptions.Timeout as e:
            return ResponseValidationError(
                status_code=status.HTTP_408_REQUEST_TIMEOUT,
                message=str(e)
            )
        except requests.exceptions.RetryError as e:
            return ResponseValidationError(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                message=str(e)
            )
        except requests.exceptions.RequestException as e:
            return ResponseValidationError(
                status_code=status.HTTP_400_BAD_REQUEST,
                message=str(e)
            )
    return wrapper
