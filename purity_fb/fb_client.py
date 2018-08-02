import ssl
import urllib3
import inspect
import re
from distutils.version import LooseVersion

from .api_client.api_client import ApiClient
from .api_client.version_api import VersionApi
from .api_client import rest

from . import purity_fb_1dot0
from . import purity_fb_1dot1
from . import purity_fb_1dot2
from . import purity_fb_1dot3
from . import purity_fb_1dot4

SUPPORTED_VERSIONS = ['1.0', '1.1', '1.2', '1.3', '1.4']

version_module_dict = {
    '1.0': purity_fb_1dot0,
    '1.1': purity_fb_1dot1,
    '1.2': purity_fb_1dot2,
    '1.3': purity_fb_1dot3,
    '1.4': purity_fb_1dot4
}


class PurityFb:
    DEFAULT_READ_TIMEOUT = 30.0
    DEFAULT_CONN_TIMEOUT = 10.0
    DEFAULT_RETRIES = 5

    def __init__(self, host, version=None, api_token=None):
        self._api_client = ApiClient(host='https://{}/api'.format(host))
        self.request_timeout = urllib3.Timeout(
            connect=PurityFb.DEFAULT_CONN_TIMEOUT,
            read=PurityFb.DEFAULT_READ_TIMEOUT)
        self.retries = urllib3.Retry(total=PurityFb.DEFAULT_RETRIES)
        self.api_version = VersionApi(self._api_client)
        self.disable_verify_ssl()

        if version:
            self._version = self._check_rest_version(version)
        else:
            self._version = self._choose_rest_version()

        # Take the latest REST API version which is the client version as user agent version
        self._api_client.user_agent = 'Purity_FB_Python_Client/' + str(SUPPORTED_VERSIONS[-1])

        purity_fb_version_module = version_module_dict.get(str(self._version))
        # This setting is needed for the _api_client to be able to deserialize response
        self._api_client.set_models(purity_fb_version_module.models)

        # Expose specific version's object model to user so user can use accurate model version
        self.models = purity_fb_version_module.models

        clsmembers = inspect.getmembers(purity_fb_version_module, inspect.isclass)
        for member in clsmembers:
            if len(member) != 2:
                continue
            if member[0].endswith("Api"):
                self.__dict__[self.camel_to_snake(member[0])[:-4]] = member[1](self._api_client)

        if api_token:
            self.login(api_token)

    def _class_name(self, api, version):
        return api + str(version).replace('.', 'dot') + 'Api'

    def list_versions(self):
        try:
            return self.api_version.list_versions().versions
        except rest.ApiException:
            return ['1.0']

    def login(self, api_token):
        try:
            self.logout()
        except rest.ApiException:
            pass
        res = self.authentication.login_with_http_info(api_token=api_token)
        self._api_client.default_headers['x-auth-token'] = res[2]['x-auth-token']
        return res[1]

    def logout(self):
        return self.authentication.logout_with_http_info()[1]

    def disable_verify_ssl(self):
        self._api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = ssl.CERT_NONE

    def enable_verify_ssl(self):
        self._api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = ssl.CERT_REQUIRED

    @property
    def request_timeout(self):
        return self._api_client.rest_client.pool_manager.connection_pool_kw['timeout']

    @request_timeout.setter
    def request_timeout(self, value):
        self._api_client.rest_client.pool_manager.connection_pool_kw['timeout'] = value

    @property
    def request_retry(self):
        return self._api_client.rest_client.pool_manager.connection_pool_kw['retries']

    @request_retry.setter
    def request_retry(self, value):
        self._api_client.rest_client.pool_manager.connection_pool_kw['retries'] = value

    @staticmethod
    def camel_to_snake(name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    @staticmethod
    def version_to_module(version):
        if version not in SUPPORTED_VERSIONS:
            msg = "Library is incompatible with REST API version {0}"
            raise ValueError(msg.format(version))

        return "purity_fb_"

    def _check_rest_version(self, version):
        """Validate a REST API version is supported by the library and target array."""
        version = str(version)

        if version not in SUPPORTED_VERSIONS:
            msg = "Library is incompatible with REST API version {0}"
            raise ValueError(msg.format(version))

        array_rest_versions = self.list_versions()
        if version not in array_rest_versions:
            msg = "Array is incompatible with REST API version {0}"
            raise ValueError(msg.format(version))

        return LooseVersion(version)

    def _choose_rest_version(self):
        """Return the newest REST API version supported by target array."""
        versions = self.list_versions()
        versions = [LooseVersion(x) for x in versions if x in SUPPORTED_VERSIONS]
        if versions:
            return max(versions)
        else:
            raise RuntimeError(
                "Library is incompatible with all REST API versions supported"
                "by the target array.")
