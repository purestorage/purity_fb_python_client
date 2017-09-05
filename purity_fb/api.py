from purity_fb.apis.authentication_api import AuthenticationApi
from purity_fb.apis.file_systems_api import FileSystemsApi
from purity_fb.apis.file_systems_beta_api import FileSystemsBetaApi
from purity_fb.apis.file_system_snapshots_api import FileSystemSnapshotsApi
from purity_fb.apis.file_system_snapshots_beta_api import FileSystemSnapshotsBetaApi
from purity_fb.api_client import ApiClient
from purity_fb import rest

import ssl
import urllib3


class PurityFb:
    DEFAULT_READ_TIMEOUT = 30.0
    DEFAULT_CONN_TIMEOUT = 10.0
    DEFAULT_RETRIES = 5

    def __init__(self, host, api_token=None):
        self._api_client = ApiClient(host="https://{}/api".format(host))
        self.request_timeout = urllib3.Timeout(
            connect=PurityFb.DEFAULT_CONN_TIMEOUT,
            read=PurityFb.DEFAULT_READ_TIMEOUT)
        self.retries = urllib3.Retry(total=PurityFb.DEFAULT_RETRIES)
        self._auth = AuthenticationApi(api_client=self._api_client)
        self._file_systems = FileSystemsApi(api_client=self._api_client)
        self._file_systems_beta = FileSystemsBetaApi(api_client=self._api_client)
        self._file_system_snapshots = FileSystemSnapshotsApi(api_client=self._api_client)
        self._file_system_snapshots_beta = FileSystemSnapshotsBetaApi(api_client=self._api_client)
        if api_token:
            self.login(api_token)

    def login(self, api_token):
        try:
            self.logout()
        except rest.ApiException:
            pass
        res = self._auth.login_with_http_info(api_token=api_token)
        self._api_client.default_headers['x-auth-token'] = res[2]['x-auth-token']
        return res[1]

    def logout(self):
        return self._auth.logout_with_http_info()[1]

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

    @property
    def authentication(self):
        return self._auth

    @property
    def file_systems(self):
        return self._file_systems

    @property
    def file_system_snapshots(self):
        return self._file_system_snapshots

    @property
    def file_systems_beta(self):
        return self._file_systems_beta

    @property
    def file_system_snapshots_beta(self):
        return self._file_system_snapshots_beta
