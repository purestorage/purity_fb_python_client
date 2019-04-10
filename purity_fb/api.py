from purity_fb.apis import *
from purity_fb.api_client import ApiClient
from purity_fb import rest

from distutils.version import LooseVersion
import ssl
import urllib3

FILE_SYSTEMS = 'FileSystems'
FILE_SYSTEM_SNAPSHOTS = 'FileSystemSnapshots'

SUPPORTED_VERSIONS = ['1.0', '1.1', '1.2']

class PurityFb:
    DEFAULT_READ_TIMEOUT = 30.0
    DEFAULT_CONN_TIMEOUT = 10.0
    DEFAULT_RETRIES = 5

    def __init__(self, host, version=None, api_token=None, ca_certs_file_path=None):
        self._api_client = ApiClient(host='https://{}/api'.format(host))
        self.request_timeout = urllib3.Timeout(
            connect=PurityFb.DEFAULT_CONN_TIMEOUT,
            read=PurityFb.DEFAULT_READ_TIMEOUT)
        self.retries = urllib3.Retry(total=PurityFb.DEFAULT_RETRIES)
        
        if not ca_certs_file_path:
            self.disable_verify_ssl()
        else:
            self.configure_ca_certificate_file(ca_certs_file_path)
            self.enable_verify_ssl()

        self._api_version = VersionApi(api_client=self._api_client)
        if version:
            self._version = self._check_rest_version(version)
        else:
            self._version = self._choose_rest_version()
        self._auth = AuthenticationApi(api_client=self._api_client)

        self._file_systems = globals()[self._class_name(FILE_SYSTEMS, self._version)](api_client=self._api_client)
        self._file_system_snapshots = globals()[self._class_name(FILE_SYSTEM_SNAPSHOTS, self._version)](
            api_client=self._api_client)

        if self._version >= LooseVersion('1.2'):
            self._admins = AdminsApi(api_client=self._api_client)
            self._alerts = AlertsApi(api_client=self._api_client)
            self._alert_watchers = AlertWatchersApi(api_client=self._api_client)
            self._arrays = ArraysApi(api_client=self._api_client)
            self._blade = BladeApi(api_client=self._api_client)
            self._certificates = CertificatesApi(api_client=self._api_client)
            self._dns = DnsApi(api_client=self._api_client)
            self._hardware = HardwareApi(api_client=self._api_client)

        if api_token:
            self.login(api_token)
        self.enable_verify_ssl()

    def _class_name(self, api, version):
        return api + str(version).replace('.', 'dot') + 'Api'

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

    def list_versions(self):
        try:
            return self._api_version.list_versions().versions
        except rest.ApiException:
            return ['1.0']

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

    def allow_verify_ssl(self, ca_certs_file_path=None):
        """ Change our certificate requirements so that a certificate is validated if provided,
        but a certificate is not required.
        Optionally, if a CA certificate(s) file path is provided, configure the client to use
        that CA certificate file.
        """
        if ca_certs_file_path:
            self.configure_ca_certificate_file(ca_certs_file_path)
        self._api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = ssl.CERT_OPTIONAL

    def disable_verify_ssl(self):
        """ Change our certificate requirements so that a certificate is validated if provided,
        but a certificate is not required.
        """
        self._api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = ssl.CERT_NONE

    def enable_verify_ssl(self, ca_certs_file_path=None):
        """ Change our certificate requirements so that a certificate is required and validated.
        Optionally, if a CA certificate(s) file path is provided, configure the client to use
        that CA certificate file.
        """
        if ca_certs_file_path:
            self.configure_ca_certificate_file(ca_certs_file_path)
        self._api_client.rest_client.pool_manager.connection_pool_kw['cert_reqs'] = ssl.CERT_REQUIRED

    def configure_ca_certificate_file(self, ca_certs_file_path):
        """"
        :param ca_certs_file_path: The path to the CA certificate(s) file to use.
        :return:
        """
        self._api_client.rest_client.pool_manager.connection_pool_kw['ca_certs'] = ca_certs_file_path

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
    def api_version(self):
        return self._api_version

    @property
    def authentication(self):
        return self._auth

    @property
    def admins(self):
        return self._admins

    @property
    def alerts(self):
        return self._alerts

    @property
    def alert_watchers(self):
        return self._alert_watchers

    @property
    def arrays(self):
        return self._arrays

    @property
    def blade(self):
        return self._blade

    @property
    def certificates(self):
        return self._certificates

    @property
    def dns(self):
        return self._dns

    @property
    def file_systems(self):
        return self._file_systems

    @property
    def file_system_snapshots(self):
        return self._file_system_snapshots

    @property
    def hardware(self):
        return self._hardware
