# purity_fb_1dot10.SnmpManagersApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snmp_managers**](SnmpManagersApi.md#create_snmp_managers) | **POST** /1.10/snmp-managers | 
[**delete_snmp_managers**](SnmpManagersApi.md#delete_snmp_managers) | **DELETE** /1.10/snmp-managers | 
[**list_snmp_managers**](SnmpManagersApi.md#list_snmp_managers) | **GET** /1.10/snmp-managers | 
[**test_snmp_managers**](SnmpManagersApi.md#test_snmp_managers) | **GET** /1.10/snmp-managers/test | 
[**update_snmp_managers**](SnmpManagersApi.md#update_snmp_managers) | **PATCH** /1.10/snmp-managers | 


# **create_snmp_managers**
> SnmpManagerResponse create_snmp_managers(names, snmp_manager)



Create SNMP managers.

### Example 
```python
from purity_fb import PurityFb, rest, SnmpManagerPost, SnmpV2c, SnmpV3

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        snmp_host = 'snmphost1.example.gov'
        # create an snmp trap manager using snmpv3 with the name 'my-v3-manager' and appropriate
        # v3 attributes
        v3_attrs = SnmpV3(auth_protocol='SHA', auth_passphrase='my-password-1!',
                          privacy_protocol='AES', privacy_passphrase='min8chars',
                          user='service-account-1')
        new_v3_manager = SnmpManagerPost(host=snmp_host, notification='trap',
                                         version='v3', v3=v3_attrs)
        v3_manager_name = 'my-v3-manager'
        res = fb.snmp_managers.create_snmp_managers(names=[v3_manager_name],
                                                    snmp_manager=new_v3_manager)
        print(res)

        # create an snmp inform manager using snmpv2c with the name 'my-v2c-manager' and appropriate
        # v2c attributes
        v2_attrs = SnmpV2c(community='some-community-for-informs')
        new_v2c_manager = SnmpManagerPost(host=snmp_host, notification='inform',
                                          version='v2c', v2c=v2_attrs)
        v2c_manager_name = 'my-v2c-manager'
        res = fb.snmp_managers.create_snmp_managers(names=[v2c_manager_name],
                                                    snmp_manager=new_v2c_manager)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating snmp managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A required list of names. | 
 **snmp_manager** | [**SnmpManagerPost**](SnmpManagerPost.md)| The attribute map used to create the snmp manager. | 

### Return type

[**SnmpManagerResponse**](SnmpManagerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_snmp_managers**
> delete_snmp_managers(ids=ids, names=names)



Delete SNMP managers.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # delete the snmp manager with the name 'my-v3-manager'
        manager_name = 'my-v3-manager'
        res = fb.snmp_managers.delete_snmp_managers(names=[manager_name])
        print(res)

        # list all snmp managers using v2c as their snmp version and then delete them, thus cleaning
        # up managers on older versions
        version_filter_string = '(version="v2c")'
        res = fb.snmp_managers.list_snmp_managers(filter=version_filter_string)
        print(res)
        for snmp_manager in res.items:
            name_to_delete = snmp_manager.name
            res = fb.snmp_managers.delete_snmp_managers(names=[name_to_delete])
            print(res)
    except rest.ApiException as e:
        print("Exception when deleting snmp managers: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_snmp_managers**
> SnmpManagerResponse list_snmp_managers(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List SNMP managers.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all snmp managers
        res = fb.snmp_managers.list_snmp_managers()
        print(res)

        # list the snmp manager with the name 'my-v3-manager'
        manager_name = 'my-v3-manager'
        res = fb.snmp_managers.list_snmp_managers(names=[manager_name])
        print(res)

        # list all snmp managers using v3 as their snmp version
        version_filter_string = '(version="v3")'
        res = fb.snmp_managers.list_snmp_managers(filter=version_filter_string)
        print(res)

        # list all snmp managers sorting by host
        sort_string = 'host'
        res = fb.snmp_managers.list_snmp_managers(sort=sort_string)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing snmp managers: %s\n" % e)
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

[**SnmpManagerResponse**](SnmpManagerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_snmp_managers**
> SnmpManagerTestResponse test_snmp_managers(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



Test SNMP managers.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # test the snmp manager with the name 'my-v3-manager'
        manager_name = 'my-v3-manager'
        res = fb.snmp_managers.test_snmp_managers(names=[manager_name])
        print(res)

        # test the snmp manager with the id '10314f42-020d-7080-8013-000ddt400090'
        manager_id = '10314f42-020d-7080-8013-000ddt400090'
        res = fb.snmp_managers.test_snmp_managers(ids=[manager_id])
        print(res)
    except rest.ApiException as e:
        print("Exception when testing snmp managers: %s\n" % e)
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

[**SnmpManagerTestResponse**](SnmpManagerTestResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_snmp_managers**
> SnmpManagerResponse update_snmp_managers(snmp_manager, ids=ids, names=names)



Update SNMP managers.

### Example 
```python
from purity_fb import PurityFb, rest, SnmpManager, SnmpV2c, SnmpV3

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update an snmp trap manager using snmpv2c with the name 'my-manager' to use snmpv3
        # with v3 attributes
        new_v3_attrs = SnmpV3(auth_protocol='SHA', auth_passphrase='my-password-1!',
                              privacy_protocol='AES', privacy_passphrase='min8chars',
                              user='service-account-1')
        manager_v3_update_attrs = SnmpManager(version='v3', v3=new_v3_attrs)
        existing_manager_name = 'my-v3-manager'
        # updating the manager to use v3 instead of v2c will automatically clear out v2c
        # attributes
        res = fb.snmp_managers.update_snmp_managers(names=[existing_manager_name],
                                                    snmp_manager=manager_v3_update_attrs)
        print(res)

        # update an snmp trap manager using snmpv3 with the name 'my-manager-2' to use snmpv2c
        # with v2c attributes
        new_v2_attrs = SnmpV2c(community='community-for-informs-and-traps')
        manager_v2c_update_attrs = SnmpManager(version='v2c', v2c=new_v2_attrs)
        existing_manager_name = 'my-v2c-manager'
        # updating the manager to use v2c instead of v3 will automatically clear out v3
        # attributes
        res = fb.snmp_managers.update_snmp_managers(names=[existing_manager_name],
                                                    snmp_manager=manager_v2c_update_attrs)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating snmp managers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_manager** | [**SnmpManager**](SnmpManager.md)| The attribute map used to update the snmp manager. | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**SnmpManagerResponse**](SnmpManagerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

