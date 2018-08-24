# coding=utf-8
"""
elib_config package configuration
"""

# noinspection PyProtectedMember
from elib_config._exc import IncompleteSetupError


class ELIBConfig:
    """
    Dummy class that contains settings for the elib_config package
    """
    __slots__: list = []
    app_version: str = 'not_set'
    app_name: str = 'not_set'
    config_file_path: str = 'not_set'
    config_sep_str: str = 'not_set'

    @classmethod
    def check(cls):
        """
        Verifies that all necessary values for the package to be used have been provided

        :raises: `elib_config._exc.IncompleteSetupError`
        """
        attribs = [
            'app_version',
            'app_name',
            'config_file_path',
            'config_sep_str',
        ]
        for attrib in attribs:
            if getattr(cls, attrib) == 'not_set':
                raise IncompleteSetupError(f'elib_config setup is incomplete; missing: {attrib}')

    @classmethod
    def setup(
            cls,
            app_version: str,
            app_name: str,
            config_file_path: str,
            config_sep_str: str
    ):
        """
        Configures elib_config in one fell swoop

        :param app_version: version of the application
        :param app_name:name of the application
        :param config_file_path: path to the config file to use
        :param config_sep_str: separator for config values paths
        """
        cls.app_version = app_version
        cls.app_name = app_name
        cls.config_file_path = config_file_path
        cls.config_sep_str = config_sep_str
