# purity_fb_1dot8.CertificatesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate_certificate_groups**](CertificatesApi.md#add_certificate_certificate_groups) | **POST** /1.8/certificates/certificate-groups | 
[**create_certificates**](CertificatesApi.md#create_certificates) | **POST** /1.8/certificates | 
[**delete_certificates**](CertificatesApi.md#delete_certificates) | **DELETE** /1.8/certificates | 
[**list_certificate_certificate_groups**](CertificatesApi.md#list_certificate_certificate_groups) | **GET** /1.8/certificates/certificate-groups | 
[**list_certificate_uses**](CertificatesApi.md#list_certificate_uses) | **GET** /1.8/certificates/uses | 
[**list_certificates**](CertificatesApi.md#list_certificates) | **GET** /1.8/certificates | 
[**remove_certificate_certificate_groups**](CertificatesApi.md#remove_certificate_certificate_groups) | **DELETE** /1.8/certificates/certificate-groups | 
[**update_certificates**](CertificatesApi.md#update_certificates) | **PATCH** /1.8/certificates | 


# **add_certificate_certificate_groups**
> MemberResponse add_certificate_certificate_groups(certificate_group_ids, certificate_group_names, certificate_names)



Add certificates to certificate groups.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # add 'posix-cert' to the 'all-trusted-certs' group
        all_trusted_group = 'all-trusted-certs'
        posix_cert = 'posix-cert'
        res = fb.certificates.add_certificate_certificate_groups(certificate_names=[posix_cert],
                                                                 certificate_group_names=[all_trusted_group])
        print(res)

        # add both 'ad-cert-2' and 'ad-cert-1' to both the 'all-trusted-certs' group and the
        # 'all-ad-certs' group
        ad_cert1 = 'ad-cert-1'
        ad_cert2 = 'ad-cert-2'
        all_ad_group = 'all-ad-certs'
        res = fb.certificates.add_certificate_certificate_groups(certificate_names=[ad_cert1, ad_cert2],
                                                                 certificate_group_names=[all_trusted_group, all_ad_group])
        print(res)
    except rest.ApiException as e:
        print("Exception when adding certificates to certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | [**list[str]**](str.md)| A comma-separated list of certificate group ids. If there is not at least one resource that matches each of the elements of certificate group ids, then an error is returned. This cannot be provided together with the certificate group names query parameters. | 
 **certificate_group_names** | [**list[str]**](str.md)| A comma-separated list of certificate group names. If there is not at least one resource that matches each of the elements of certificate group names, then an error is returned. This cannot be provided together with the certificate group ids query parameters. | 
 **certificate_names** | [**list[str]**](str.md)| A comma-separated list of certificate names. If there is not at least one resource that matches each of the elements of certificate names, then an error is returned. This cannot be provided together with the certificate ids query parameters. | 

### Return type

[**MemberResponse**](MemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_certificates**
> CertificateResponse create_certificates(certificate, names=names)



Create certificates.

### Example 
```python
from purity_fb import PurityFb, Certificate, CertificatePost, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create a new external certificate named "ad-cert-1"
        cert_name = 'ad-cert-1'
        cert_text = '-----BEGIN CERTIFICATE-----\nMIIESzCCAzOgAwIBAgIJAIJMKJXXDn/JMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV\nBAYTAlVTMQ0wCwYDVQQIEwR0ZXN0MQ4wDAYDVQQHEwV0ZXN0IDENMAsGA1UEChME\ndGVzdDENMAsGA1UECxMEdGVzdDEVMBMGA1UEAxMMUHVyZSBTdG9yYWdlMRMwEQYJ\nKoZIhvcNAQkBFgR0ZXN0MB4XDTE3MTEwNjIyMzYyMFoXDTE4MTEwNjIyMzYyMFow\ndjELMAkGA1UEBhMCVVMxDTALBgNVBAgTBHRlc3QxDjAMBgNVBAcTBXRlc3QgMQ0w\nCwYDVQQKEwR0ZXN0MQ0wCwYDVQQLEwR0ZXN0MRUwEwYDVQQDEwxQdXJlIFN0b3Jh\nZ2UxEzARBgkqhkiG9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw\nggEKAoIBAQDcaGpPXJC1EC515wMEKyXEFuKFEDn4y1V5YmaLt+hXz8cfuA+gS3eD\nltP8PJah+7WrPouUQtfamHsuQtnFFLcVcdl83rIFX0m58zUiWbOUHI5wWnBYsqof\n52k/m40HM5XTATn5xpFsTSxm7vmlsKfGlQS7yI11HbD0OOz9CqT+iMFhTn/Wfyg2\nYOtmYIfCz0kt6wIFHlI9oPERwJ0JiMnPhsg0gerJwYl1j1vDhBiK32OVc4iIdOO4\nPVwpP1YbINr8LJ5qX2DOzBHDnaYrtJk9YEsSAwoqJ2/d29xA9JOeJwahl/M6aO48\nAbXbSlxVwOz0lEs85dseLp9dyTQb/uzjAgMBAAGjgdswgdgwHQYDVR0OBBYEFJJM\nML8khiOYzpaJP8sJCn0JSpx9MIGoBgNVHSMEgaAwgZ2AFJJMML8khiOYzpaJP8sJ\nCn0JSpx9oXqkeDB2MQswCQYDVQQGEwJVUzENMAsGA1UECBMEdGVzdDEOMAwGA1UE\nBxMFdGVzdCAxDTALBgNVBAoTBHRlc3QxDTALBgNVBAsTBHRlc3QxFTATBgNVBAMT\nDFB1cmUgU3RvcmFnZTETMBEGCSqGSIb3DQEJARYEdGVzdIIJAIJMKJXXDn/JMAwG\nA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAKjQ/SFPra2YmtNynNukuHOl\nCryjsXjBkeiyyfg3Bt9+M+9F6Y4Sh3/SSJCb6LQaqTQkeJJeb1fOHNaFjAxkjvaI\n2tnlCwhpQuoSXNgQEMdidMi9+S8hBonlXYePYZUQbvAu1VAZrU6f0k2OEDcAPLvA\nhZLvrmZeug+VZp3JfVOdU+QnzUx2atBBfN5lMFFNdqOzZ5Yz/Ooi9CVA73szIevi\nE728OLimWQ91u1s16isjusK3+zoqirFC7PN6K63sp0gPAldgCQD2bywmwgaYDnzP\n+9ZWNy6ebn927Qh22YUPWhj+kiITkhxcVYPMx4QtRjJhs5pQVBqHOIDnJQJc7qY=\n-----END CERTIFICATE-----'
        cert_type = 'external'

        create_body = CertificatePost(certificate=cert_text, certificate_type=cert_type)
        res = fb.certificates.create_certificates(names=[cert_name], certificate=create_body)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**CertificatePost**](CertificatePost.md)|  | 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_certificates**
> delete_certificates(ids=ids, names=names)



Delete certificates.

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
        # delete our external certificate named "ad-cert-1"
        cert_name = 'ad-cert-1'
        res = fb.certificates.delete_certificates(names=[cert_name])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificate_certificate_groups**
> MemberResponse list_certificate_certificate_groups(certificate_group_ids=certificate_group_ids, certificate_group_names=certificate_group_names, certificate_ids=certificate_ids, certificate_names=certificate_names, filter=filter, limit=limit, sort=sort, start=start, token=token)



List certificates' certificate groups.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all membership objects for certificates that belong to groups and the groups to
        # which they belong
        res = fb.certificates.list_certificate_certificate_groups()
        print(res)

        # list the membership objects to see what groups 'ad-cert-1' and 'posix-cert' belong to,
        # if any
        res = fb.certificates.list_certificate_certificate_groups(certificate_names=['ad-cert-1', 'posix-cert'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificates' certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | [**list[str]**](str.md)| A comma-separated list of certificate group ids. This cannot be provided together with the certificate group names query parameters. | [optional] 
 **certificate_group_names** | [**list[str]**](str.md)| A comma-separated list of certificate group names. This cannot be provided together with the certificate group ids query parameters. | [optional] 
 **certificate_ids** | [**list[str]**](str.md)| A comma-separated list of certificate ids. This cannot be provided together with the certificate names query parameters. | [optional] 
 **certificate_names** | [**list[str]**](str.md)| A comma-separated list of certificate names. This cannot be provided together with the certificate ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**MemberResponse**](MemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificate_uses**
> CertificateUseResponse list_certificate_uses(ids=ids, names=names)



List certificate uses.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list the uses of all certificates
        res = fb.certificates.list_certificate_uses()
        print(res)

        # list the uses of certificates named "ad-cert-1" and "posix-cert"
        res = fb.certificates.list_certificate_uses(names=['ad-cert-1', 'posix-cert'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificate uses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**CertificateUseResponse**](CertificateUseResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificates**
> CertificateResponse list_certificates(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List certificates.

### Example 
```python
from purity_fb import PurityFb, rest

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

        # list certificates named "ad-cert-1" and "posix-cert"
        res = fb.certificates.list_certificates(names=['ad-cert-1', 'posix-cert'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **remove_certificate_certificate_groups**
> remove_certificate_certificate_groups(certificate_group_ids, certificate_group_names, certificate_names)



Remove certificates from certificate groups.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # remove 'posix-cert' from the 'all-trusted-certs' group
        all_trusted_group = 'all-trusted-certs'
        posix_cert = 'posix-cert'
        res = fb.certificates.remove_certificate_certificate_groups(certificate_names=[posix_cert],
                                                                    certificate_group_names=[all_trusted_group])
        print(res)

        # remove both 'ad-cert-2' and 'ad-cert-1' from both the 'all-trusted-certs' group and the
        # 'all-ad-certs' group
        ad_cert1 = 'ad-cert-1'
        ad_cert2 = 'ad-cert-2'
        all_ad_group = 'all-ad-certs'
        res = fb.certificates.remove_certificate_certificate_groups(certificate_names=[ad_cert1, ad_cert2],
                                                                    certificate_group_names=[all_trusted_group, all_ad_group])
        print(res)
    except rest.ApiException as e:
        print("Exception when removing certificates from certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | [**list[str]**](str.md)| A comma-separated list of certificate group ids. If there is not at least one resource that matches each of the elements of certificate group ids, then an error is returned. This cannot be provided together with the certificate group names query parameters. | 
 **certificate_group_names** | [**list[str]**](str.md)| A comma-separated list of certificate group names. If there is not at least one resource that matches each of the elements of certificate group names, then an error is returned. This cannot be provided together with the certificate group ids query parameters. | 
 **certificate_names** | [**list[str]**](str.md)| A comma-separated list of certificate names. If there is not at least one resource that matches each of the elements of certificate names, then an error is returned. This cannot be provided together with the certificate ids query parameters. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_certificates**
> CertificateResponse update_certificates(certificate, ids=ids, names=names)



Update certificates.

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
        # change our built-in certificate named "global", which is used by the REST server and S3
        # to a new certificate issued by my internal CA
        cert_name = 'global'
        cert_text = '-----BEGIN CERTIFICATE-----\nMIIESzCCAzOgAwIBAgIJAIJMKJXXDn/JMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV\nBAYTAlVTMQ0wCwYDVQQIEwR0ZXN0MQ4wDAYDVQQHEwV0ZXN0IDENMAsGA1UEChME\ndGVzdDENMAsGA1UECxMEdGVzdDEVMBMGA1UEAxMMUHVyZSBTdG9yYWdlMRMwEQYJ\nKoZIhvcNAQkBFgR0ZXN0MB4XDTE3MTEwNjIyMzYyMFoXDTE4MTEwNjIyMzYyMFow\ndjELMAkGA1UEBhMCVVMxDTALBgNVBAgTBHRlc3QxDjAMBgNVBAcTBXRlc3QgMQ0w\nCwYDVQQKEwR0ZXN0MQ0wCwYDVQQLEwR0ZXN0MRUwEwYDVQQDEwxQdXJlIFN0b3Jh\nZ2UxEzARBgkqhkiG9w0BCQEWBHRlc3QwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw\nggEKAoIBAQDcaGpPXJC1EC515wMEKyXEFuKFEDn4y1V5YmaLt+hXz8cfuA+gS3eD\nltP8PJah+7WrPouUQtfamHsuQtnFFLcVcdl83rIFX0m58zUiWbOUHI5wWnBYsqof\n52k/m40HM5XTATn5xpFsTSxm7vmlsKfGlQS7yI11HbD0OOz9CqT+iMFhTn/Wfyg2\nYOtmYIfCz0kt6wIFHlI9oPERwJ0JiMnPhsg0gerJwYl1j1vDhBiK32OVc4iIdOO4\nPVwpP1YbINr8LJ5qX2DOzBHDnaYrtJk9YEsSAwoqJ2/d29xA9JOeJwahl/M6aO48\nAbXbSlxVwOz0lEs85dseLp9dyTQb/uzjAgMBAAGjgdswgdgwHQYDVR0OBBYEFJJM\nML8khiOYzpaJP8sJCn0JSpx9MIGoBgNVHSMEgaAwgZ2AFJJMML8khiOYzpaJP8sJ\nCn0JSpx9oXqkeDB2MQswCQYDVQQGEwJVUzENMAsGA1UECBMEdGVzdDEOMAwGA1UE\nBxMFdGVzdCAxDTALBgNVBAoTBHRlc3QxDTALBgNVBAsTBHRlc3QxFTATBgNVBAMT\nDFB1cmUgU3RvcmFnZTETMBEGCSqGSIb3DQEJARYEdGVzdIIJAIJMKJXXDn/JMAwG\nA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADggEBAKjQ/SFPra2YmtNynNukuHOl\nCryjsXjBkeiyyfg3Bt9+M+9F6Y4Sh3/SSJCb6LQaqTQkeJJeb1fOHNaFjAxkjvaI\n2tnlCwhpQuoSXNgQEMdidMi9+S8hBonlXYePYZUQbvAu1VAZrU6f0k2OEDcAPLvA\nhZLvrmZeug+VZp3JfVOdU+QnzUx2atBBfN5lMFFNdqOzZ5Yz/Ooi9CVA73szIevi\nE728OLimWQ91u1s16isjusK3+zoqirFC7PN6K63sp0gPAldgCQD2bywmwgaYDnzP\n+9ZWNy6ebn927Qh22YUPWhj+kiITkhxcVYPMx4QtRjJhs5pQVBqHOIDnJQJc7qY=\n-----END CERTIFICATE-----'
        # use a private key that was encrypted with a passphrase
        private_key = '-----BEGIN RSA PRIVATE KEY-----\nProc-Type: 4,ENCRYPTED\nDEK-Info: DES-EDE3-CBC,D6E1A92B08CB859F\n\nh+XvYwbbEIboztkR5/Gku7UsCnZtNI/ZYZru3jm/tRgjXR71PBgi9x1Rv5wyiDXA\n9F8xWyacRQgSqQCO2tc+rqoBTAd33wGo52k7BCuG2VJgbuzlZlC4vsyjKna1yGRw\nFHv+dHPWyTE/Cqcl0QQGjpqQmKbX6OXcUnDRp0IPzRf98A6DVZ/jbwuGl1JIkEme\nCuo4/5Hc4BMeHBYGtzbYZ83nFyrImhMQA+HzeULWSi0Ecx2vbafrlXVd0hI9E3c6\nsahuu6A9DSwEGWWW5x/ubq0i8mS94s7O4EjNoI8w6/yhd2edUTsTddJ2I+DJxOB1\nlBukWeph+/wAiCdVKuHW9A5xbPK0U24ipRh1vOG1ikeFR62gFktSnquOv4zpZL73\nSE7xWP1+FotaEgEL1hkHqfMfEnEL0/5oVyYVB9BZ2VaiystWvFk/mgLJiWGM0zx8\n5rA+0kqNTVYHhwElMUYMXILx3RMGVH+A0kKWvpl3BBuwDbQfgl0m1lLK6zZgtwVL\nkyctAjthTwC4KZorATa2CTBLq5cCSq1itoVueCYozuUPDMmCuC4Xf3dMEcYok+E5\nF4USqn7xcCqTu5ftqoiSt5bdJ7MOfL/KVXjQZAi/eUPaaREI27mqyfnVM6f2VcEp\nsQJnJg+zpcnBY0oICtGsakZWD0iE2ZA4FN177ogl8mlU4sY6XteHtPEFn8jjWuwW\ncylAo4jg/D6LPm+a7v1BYV41xLLQSFRvFGsyGON5CMg2vO9kjNnTDONNEchQ1C4A\nqIAIhjye+VD1F0L4McswRUQMISuWpbTND6HV2/DwXh9mDP2jVsttoJ3mjJrCeR1/\nTcMkN2C1isNUrRh+ReWtmanyhIorPLGX9TuDBef1r6caqVdGvDzjWaVUh6qTHsoY\nzt49SxXykIbZCdEbAQkoXfg8MuK+lxlGVEP/OS1uMXI8tVozBpepI8diFVznWpJo\nHVJCvcrOoIQr/B6kZX6mfqH5EJcnJPC4GUYwu+TRi03fmmKHi56xyWdrm/payoJH\n6ApOXeD4ViaFKkI6f69o5aADVZcmOWMqP6Yd8oxvl1Rn7ArR/RBcQwCMUZEA0dOs\ndu4S9hwTDlekT7unaVuXWmU9Js63DK82K3w+EjWUmYobX4tnM1nqJ4nBS8btt0kc\nBefHQP4gx72ytkJW4cVtFD/us0UBMTvODXDmBeZxlIJsNkU0EWyW+1kKBRpVhHGB\nofPRqYTk/m9yMzuDhutupW1uV+5g+lvpxXKQu4kSzJS6UVWZ33iz7yrvIOrJ3hxZ\nsJjWj+f0Bef/gym2JrGb1J756lPwBY4S/3/yiajbUvRvElOoVQB5XSH+th5N/hUJ\ntD2TJJsWnr/E6vwZjsYwK1hav/YcJi/YJdoXziZkKoYlf2WvwLAsvj9fNrpguwqV\npMJARiVwBDrWiB16GRdHxa0HwCJKB8Vpz9pDYQNdBseAhJzGmh5JaBiIbuVJaVwF\nZP+y2v/3Pa7wzAZTjD46V9EvADK6RW9If12OPHP4G2FvhdngxGbNjgZbEy0HUy4I\n6MRcPb3qaR5tnySoozrwW5IRYy7yZJ+UEg03nUi8eHKUL6anF5YzCg==\n-----END RSA PRIVATE KEY-----'
        passphrase = 'example password'

        create_body = Certificate(certificate=cert_text, private_key=private_key, passphrase=passphrase)
        res = fb.certificates.update_certificates(names=[cert_name], certificate=create_body)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate** | [**Certificate**](Certificate.md)|  | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**CertificateResponse**](CertificateResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

