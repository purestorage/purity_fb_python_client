# purity_fb.CertificatesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_certificates**](CertificatesApi.md#list_certificates) | **GET** /1.3/certificates | 
[**update_certificates**](CertificatesApi.md#update_certificates) | **PATCH** /1.3/certificates | 


# **list_certificates**
> CertificateResponse list_certificates()



List certificates

### Example 
```python
from purity_fb import PurityFb, Certificate, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all certificates
        res = fb.certificates.list_certificates()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_certificates**
> CertificateResponse update_certificates(certificate, names=names)



Update certificates

### Example 
```python
from purity_fb import PurityFb, Certificate, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    certificate_text = "-----BEGIN CERTIFICATE-----\nMIIECzCCAvOgAwIBAgIJAMhDKlzTyOVhMA0GCSqGSIb3DQEBCwUAMIGbMQswCQYD\nVQQGEwJVUzETMBEGA1UECAwKdGVzdCBzdGF0ZTEWMBQGA1UEBwwNdGVzdCBsb2Nh\nbGl0eTERMA8GA1UECgwIdGVzdCBvcmcxFjAUBgNVBAsMDXRlc3Qgb3JnIHVuaXQx\nGTAXBgNVBAMMEHRlc3QgY29tbW9uIG5hbWUxGTAXBgkqhkiG9w0BCQEWCnRlc3Qg\nZW1haWwwHhcNMTcwOTI4MjMzMTQ0WhcNMTgwOTI4MjMzMTQ0WjCBmzELMAkGA1UE\nBhMCVVMxEzARBgNVBAgMCnRlc3Qgc3RhdGUxFjAUBgNVBAcMDXRlc3QgbG9jYWxp\ndHkxETAPBgNVBAoMCHRlc3Qgb3JnMRYwFAYDVQQLDA10ZXN0IG9yZyB1bml0MRkw\nFwYDVQQDDBB0ZXN0IGNvbW1vbiBuYW1lMRkwFwYJKoZIhvcNAQkBFgp0ZXN0IGVt\nYWlsMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqPjnK29WG0cGs2yE\nb/ijAVGKm8wQdUz4ussOcwM/1sY8CEcpRkRUsvZqIkFa8REHqIyJQuOq/wfMPCNi\nukyi17QHMlGPYuMazuvTQkuxx1K9KTt7zBCxksY4yRC0vhjV5K4/8sREyikE3ayv\nWw5hpWKXd8MFCZkBLn3/WTFtC04c23HCSwXFAmHhVxM24Dser6L6pC1h0KlFnAMk\ncZElOlPgpszQOZ4SkInJFDFj/OQ1FaDG/iAp72sbaEoN0Wk+4X7heqLvcpWmqTP5\nBj7vgr38+MoW2UR7SBbhNkS/o7g956Gvy6jr1jH/8uZarFynkepoepZouiFtHkya\nxGWuxwIDAQABo1AwTjAdBgNVHQ4EFgQULg+8tirCkm7if3QpIU5BXkMm1n8wHwYD\nVR0jBBgwFoAULg+8tirCkm7if3QpIU5BXkMm1n8wDAYDVR0TBAUwAwEB/zANBgkq\nhkiG9w0BAQsFAAOCAQEAS4RuhNixyIORfH4gN4lK27FGc3j+8uKBMOhmnX426bSD\n2BxugqjC9c9oT+erCXawfD+V2v3JFuMZ73vUOpZvTe6+LlVaofjKQk/VlSXcKB/X\nt93ZaoWd23D4TFymWf1sGqvzX0JOKI2Ht6oSwdZexNY9DJKNRwZL+voX2UZDeCWL\n9YU8iJFgn6mMp7js1SoZnAPtCO6AEfpUjiiYrc0JWOALjFYZimJmpBPkZtH+XlZH\n4iwYmvt4veHIgoBl9/91SIYodZFFq9PqpxBa3VMxCdxQef8w7ZzYaZcbzEMG2zXu\n0MZx9MAOkpteQbyiW1riXh8cuPRRGM9kdGSJBO6EQQ==\n-----END CERTIFICATE-----\n"
    private_key_text = "-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,5DED2ABEC5BA5199\n\nWbkXqSysHD3Bv/1vRWFgUXL/FstoAhgdMo8iHwulbOKnxenhArXEM1W3w3DALPFv\nNaCx3phqUR1kF5beVnGqKvbBxZAZg7xml7MOMPWKrX8+IbNbZKM2ajddUuzu9Qo2\noAoI57bOUTq4JHDKtSIiO3R/2GaFsa0IxXxRAktnlDkNR1kG66pjTehmEKoQ82I/\nBWxZ5CJZOMVtUqlK7h/g4aa0XdGehosHH3AQLYjiLGYTQFt+wCG6nNnXkjNW2n6j\nmWloL8ALtB48BXnRY2La8jCD+lNLpzZZug8vFTCrLaUIJ55TlTVQLU5ixP7VGJAS\nwjnANs1su8IjMC1zft8ilnWTA+JyMQqnqQoitluKnKp6o87AHqZhj1aUw0iXFse9\nAu8H920mw01/3nfPU2kHw3SF+NAqO6R9beMpnTTfy9jT00IOhJ+4Ugpcq09IUTol\nfLVu6cWYgJG1xQQmftdM4/5d0kJQGN5aFOa+sn80PKfxky3HCqkgbYKCWVUHJ+b6\n3U+zrawNmS0v0OjwxVqzUWx6l5TukyhdXNNBWyZRklSrF0kY5IYJZZ64PCQP4Q1c\n52l841MEEW5dBxWLb/ljXjIHKfKBdxfic4NbwsG5rAZ9nYgxN+2/r+KpODbooiFp\n32I82a1TXGBtyQS1APXf+S2NMB1oGQEaF+BU4Drh3G/wCQTosSIhQsuB7CH+iD/A\nKkSntX9bw5WeFzsGm6QBL6FB6PLFF1lk2MRANQlTHvJOxj+Qvdg3TAMC14dQKUrM\nj+IcM9eux3PooSHDpwqy8x/KRUTPZBW2dVHK8BCSUpYZydcZII0x2+vtlmJCFrrv\noO6YtXudLxZLhax8+lAaZ/44CMuG4HC3uQpoJczL22tCYs/tpBaw7Hh8oGqsaLxW\ncBE9ZoZzbrqnM0buPxo8V+xuaaM3CZIjP6xbJ3Oa3XWNrYvQPQKP2FjgK+PlhELz\n6QiMbH3/G3czbxN8jALP6sQ/15LrqFxbQmGP8aAZLPz+PaypnJLBBSsEx0TrxFEM\nozTt1+yvPYEwOR5LLvBRS+sZvV5WBfJSqWFNUR/gMlpwhu6Qth0/hR0WsHmRkG1N\npvYRKIXX/i7b54fAPWVViGtmzSm4yQGIGi7ouPEnBeHhbqIYKwAbZUGl8WsQdZNF\n4iJsiljzXzrDvV9Cf23iuDBbYxLSd72Ie65eFdWWj7Pgm0eSNICTE+ekEfE9HIni\nI6Qgq9IEVVkUCiKl/YZRq0w8QsNyAsjOK3BgoeebOlOTS7xZuI4s6CArhpJwp4IZ\nLzyyrEzq7vnaWWOjE01SdW3gp2aZaDxtu3ftK/hPDp8Jsn5tDg1X5GUSXgIWW/GI\nkmPyktqUEvpZSqgDL6rPtR/jeHcrq+CFAvR0OF+AOs8doHiMV+Lzku2S5FiQLXad\nlWXAokFDXiTZpDI4dq15Vx3D4DXQQ9RLbFsTVFYTFIfH39WT71iN5HfXek8VnMi6\nnfU80KNKuKgkkSWkM4yMkY82H4uuPqXxI6eIs4sFpPHfWNDVlZ0dQR40SeySBT1H\nSUayDetFO6hE38QIqAAUs2gWRuv6WhNfMc6E+gAFx1hUhpR6EKzO/Q==\n-----END RSA PRIVATE KEY-----\n"
    passphrase_text = "test passphrase"
    certificate_to_import = Certificate(certificate=certificate_text, private_key=private_key_text, passphrase=passphrase_text)
    certificate_name = "global"
    try:
        # update the 'global' certificate, which is the only supported certificate at the momen
        res = fb.certificates.update_certificates(names=[certificate_name], certificate=certificate_to_import)
        print(res)
    except rest.ApiException as e:
        print("Exception when importing certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**Certificate**](Certificate.md)|  | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

