# purity_fb_1dot11.CertificateGroupsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_certificate_group_certificates**](CertificateGroupsApi.md#add_certificate_group_certificates) | **POST** /1.11/certificate-groups/certificates | 
[**create_certificate_groups**](CertificateGroupsApi.md#create_certificate_groups) | **POST** /1.11/certificate-groups | 
[**delete_certificate_groups**](CertificateGroupsApi.md#delete_certificate_groups) | **DELETE** /1.11/certificate-groups | 
[**list_certificate_group_certificates**](CertificateGroupsApi.md#list_certificate_group_certificates) | **GET** /1.11/certificate-groups/certificates | 
[**list_certificate_group_uses**](CertificateGroupsApi.md#list_certificate_group_uses) | **GET** /1.11/certificate-groups/uses | 
[**list_certificate_groups**](CertificateGroupsApi.md#list_certificate_groups) | **GET** /1.11/certificate-groups | 
[**remove_certificate_group_certificates**](CertificateGroupsApi.md#remove_certificate_group_certificates) | **DELETE** /1.11/certificate-groups/certificates | 


# **add_certificate_group_certificates**
> MemberResponse add_certificate_group_certificates(certificate_group_ids=certificate_group_ids, certificate_group_names=certificate_group_names, certificate_ids=certificate_ids, certificate_names=certificate_names)



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
        res = fb.certificate_groups.add_certificate_group_certificates(certificate_names=[posix_cert],
                                                                       certificate_group_names=[all_trusted_group])
        print(res)

        # add both 'ad-cert-2' and 'ad-cert-1' to both the 'all-trusted-certs' group and the
        # 'all-ad-certs' group
        ad_cert1 = 'ad-cert-1'
        ad_cert2 = 'ad-cert-2'
        all_ad_group = 'all-ad-certs'
        res = fb.certificate_groups.add_certificate_group_certificates(certificate_names=[ad_cert1, ad_cert2],
                                                                       certificate_group_names=[all_trusted_group, all_ad_group])
        print(res)
    except rest.ApiException as e:
        print("Exception when adding certificates to certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | **list[str]**| A comma-separated list of certificate group ids. This cannot be provided together with the certificate group names query parameters. | [optional] 
 **certificate_group_names** | **list[str]**| A comma-separated list of certificate group names. This cannot be provided together with the certificate group ids query parameters. | [optional] 
 **certificate_ids** | **list[str]**| A comma-separated list of certificate ids. This cannot be provided together with the certificate names query parameters. | [optional] 
 **certificate_names** | **list[str]**| A comma-separated list of certificate names. This cannot be provided together with the certificate ids query parameters. | [optional] 

### Return type

[**MemberResponse**](MemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_certificate_groups**
> CertificateGroupResponse create_certificate_groups(names=names)



Create certificate groups.

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
        # create groups to use for all certificates, as well as for all AD certificates
        group_for_all_certs = 'all-trusted-certs'
        group_for_active_directory_certs = 'all-ad-certs'
        # list the certificate groups named "all-trusted-certs" and "all-ad-certs"
        res = fb.certificate_groups.create_certificate_groups(names=[group_for_all_certs,
                                                                     group_for_active_directory_certs])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**CertificateGroupResponse**](CertificateGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_certificate_groups**
> delete_certificate_groups(ids=ids, names=names)



Delete certificate groups.

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
        # delete our group for active directory certificates
        group_for_active_directory_certs = 'all-ad-certs'
        # list the certificate groups named "all-trusted-certs" and "all-ad-certs"
        res = fb.certificate_groups.delete_certificate_groups(names=[group_for_active_directory_certs])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificate_group_certificates**
> MemberResponse list_certificate_group_certificates(certificate_group_ids=certificate_group_ids, certificate_group_names=certificate_group_names, certificate_ids=certificate_ids, certificate_names=certificate_names, filter=filter, limit=limit, sort=sort, start=start, token=token)



List certificate groups' certificates.

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
        # list all membership objects for certificate groups and the certificates that belong to
        # them
        res = fb.certificate_groups.list_certificate_group_certificates()
        print(res)

        # list the membership objects to see what certificates are contained within groups
        # 'all-trusted-certs' and 'all-ad-certs' belong to, if any
        res = fb.certificate_groups.list_certificate_group_certificates(certificate_group_names=['all-trusted-certs',
                                                                                                 'all-ad-certs'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificate groups' certificates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | **list[str]**| A comma-separated list of certificate group ids. This cannot be provided together with the certificate group names query parameters. | [optional] 
 **certificate_group_names** | **list[str]**| A comma-separated list of certificate group names. This cannot be provided together with the certificate group ids query parameters. | [optional] 
 **certificate_ids** | **list[str]**| A comma-separated list of certificate ids. This cannot be provided together with the certificate names query parameters. | [optional] 
 **certificate_names** | **list[str]**| A comma-separated list of certificate names. This cannot be provided together with the certificate ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**MemberResponse**](MemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificate_group_uses**
> CertificateGroupUseResponse list_certificate_group_uses(filter=filter, ids=ids, names=names, limit=limit, sort=sort, start=start, token=token)



List certificate group uses.

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
        # list the uses of all certificate groups
        res = fb.certificate_groups.list_certificate_group_uses()
        print(res)

        # list the uses of certificate groups named "all-trusted-certs" and "all-ad-certs"
        res = fb.certificate_groups.list_certificate_group_uses(names=['all-trusted-certs',
                                                                       'all-ad-certs'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificate group uses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**CertificateGroupUseResponse**](CertificateGroupUseResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_certificate_groups**
> CertificateGroupResponse list_certificate_groups(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List certificate groups.

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
        # list all certificate groups
        res = fb.certificate_groups.list_certificate_groups()
        print(res)

        # list the certificate groups named "all-trusted-certs" and "all-ad-certs"
        res = fb.certificate_groups.list_certificate_groups(names=['all-trusted-certs',
                                                                   'all-ad-certs'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**CertificateGroupResponse**](CertificateGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **remove_certificate_group_certificates**
> remove_certificate_group_certificates(certificate_group_ids=certificate_group_ids, certificate_group_names=certificate_group_names, certificate_ids=certificate_ids, certificate_names=certificate_names)



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
        # add 'posix-cert' to the 'all-trusted-certs' group
        all_trusted_group = 'all-trusted-certs'
        posix_cert = 'posix-cert'
        res = fb.certificate_groups.remove_certificate_group_certificates(certificate_names=[posix_cert],
                                                                          certificate_group_names=[all_trusted_group])
        print(res)

        # add both 'ad-cert-2' and 'ad-cert-1' to both the 'all-trusted-certs' group and the
        # 'all-ad-certs' group
        ad_cert1 = 'ad-cert-1'
        ad_cert2 = 'ad-cert-2'
        all_ad_group = 'all-ad-certs'
        res = fb.certificate_groups.remove_certificate_group_certificates(certificate_names=[ad_cert1, ad_cert2],
                                                                          certificate_group_names=[all_trusted_group, all_ad_group])
        print(res)
    except rest.ApiException as e:
        print("Exception when removing certificates from certificate groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_group_ids** | **list[str]**| A comma-separated list of certificate group ids. This cannot be provided together with the certificate group names query parameters. | [optional] 
 **certificate_group_names** | **list[str]**| A comma-separated list of certificate group names. This cannot be provided together with the certificate group ids query parameters. | [optional] 
 **certificate_ids** | **list[str]**| A comma-separated list of certificate ids. This cannot be provided together with the certificate names query parameters. | [optional] 
 **certificate_names** | **list[str]**| A comma-separated list of certificate names. This cannot be provided together with the certificate ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

