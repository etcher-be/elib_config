# coding=utf-8
"""
Exceptions for the value package
"""
import typing

# noinspection PyProtectedMember
from elib_config._exc import ELIBConfigError


class _ConfigValueError(ELIBConfigError):
    """Base class for all config values errors"""

    def __init__(self, value_name: str, msg: str) -> None:
        self.value_name = value_name
        self.msg = msg
        super(_ConfigValueError, self).__init__(
            f'{value_name}: {msg}'
        )


class DuplicateConfigValueError(_ConfigValueError):
    """Raised when another config value has the same path"""

    def __init__(self, value_name: str) -> None:
        super(DuplicateConfigValueError, self).__init__(
            value_name,
            'another configuration value has been defined with the same name'
        )


class ConfigMissingValueError(_ConfigValueError):
    """Raised when a config value is missing"""


class ConfigValueError(_ConfigValueError):
    """Raised when a given value is invalid"""


class PathMustExistError(ConfigValueError):
    """Raised a file/folder is not present"""

    def __init__(self, value_name: str) -> None:
        super(PathMustExistError, self).__init__(
            value_name,
            'file/folder not found'
        )


class NotAFileError(ConfigValueError):
    """Raised when a given path is not a file"""

    def __init__(self, value_name: str) -> None:
        super(NotAFileError, self).__init__(
            value_name,
            'not a file'
        )


class NotAFolderError(ConfigValueError):
    """Raised when a given path is not a file"""

    def __init__(self, value_name: str) -> None:
        super(NotAFolderError, self).__init__(
            value_name,
            'not a folder'
        )


class ConfigTypeError(_ConfigValueError):
    """Raised when the given value config is of an invalid type"""


class OutOfBoundError(_ConfigValueError):
    """Raised when a given integer is outside of the given limits"""

    def __init__(self, value_name: str, value: int, min_: typing.Optional[int], max_: typing.Optional[int]) -> None:
        msg = f'integer out of bound: "{value}"; limits are: minima: {min_}, maxima: {max_}'
        super(OutOfBoundError, self).__init__(value_name, msg)
