from purity_fb import PurityFb
import os
import urllib3

# See https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
urllib3.disable_warnings()

# REST server hostname/IP
HOST = os.environ.get('REST_TEST_HOST', 'localhost')
# pureuser
API_TOKEN = os.environ.get('REST_TEST_API_TOKEN', 'T-9709078c-6c05-495f-af2c-9318888097f1')
# ir
INTERNAL_API_TOKEN = os.environ.get('REST_TEST_INTERNAL_API_TOKEN', 'T-9709078c-6c05-495f-af2c-9318888097f1')
VERSIONS = ['1.0', '1.1', '1.2']

def get_test_versions(host):
    array = PurityFb(host)
    array.disable_verify_ssl()
    rest_versions = array.list_versions()
    return [v for v in rest_versions if v in VERSIONS]
