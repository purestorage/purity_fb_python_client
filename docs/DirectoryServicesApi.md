# purity_fb_1dot5.DirectoryServicesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_directory_services**](DirectoryServicesApi.md#list_directory_services) | **GET** /1.5/directory-services | 
[**list_directory_services_roles**](DirectoryServicesApi.md#list_directory_services_roles) | **GET** /1.5/directory-services/roles | 
[**test_directory_services**](DirectoryServicesApi.md#test_directory_services) | **GET** /1.5/directory-services/test | 
[**update_directory_services**](DirectoryServicesApi.md#update_directory_services) | **PATCH** /1.5/directory-services | 
[**update_directory_services_roles**](DirectoryServicesApi.md#update_directory_services_roles) | **PATCH** /1.5/directory-services/roles | 


# **list_directory_services**
> DirectoryServiceResponse list_directory_services(filter=filter, limit=limit, sort=sort, start=start, token=token, names=names)



List directory services

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
        # list Directory Services configuration
        res = fb.directory_services.list_directory_services(names=["management"])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing directory services configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**DirectoryServiceResponse**](DirectoryServiceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_directory_services_roles**
> DirectoryServiceRolesResponse list_directory_services_roles(names=names)



List directory services roles configurations

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryServiceRole

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list Directory Services configuration
        res = fb.directory_services.list_directory_services_roles()
        print(res)

        # list settings configuration for a specific role
        ROLE_NAME = 'array_admin'
        res = fb.directory_services.list_directory_services_roles(names=[ROLE_NAME])
    except rest.ApiException as e:
        print("Exception when listing directory services roles configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**DirectoryServiceRolesResponse**](DirectoryServiceRolesResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_directory_services**
> TestResultResponse test_directory_services(names=names)



Test directory services

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
        # test directory services for the specified profile
        res = fb.alert_watchers.test_directory_services(
            names=['management'])
        print(res)
    except rest.ApiException as e:
        print("Exception when testing directory services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**TestResultResponse**](TestResultResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_directory_services**
> DirectoryServiceResponse update_directory_services(directory_service, names=names)



Update directory services

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
        # update Directory Services management configuration
        name="management"
        URI = 'ldaps://ad1.mycompany.com'
        BASE_DN = 'DC=mycompany,DC=com'
        BIND_USER = 'CN=John,OU=Users,DC=mycompany,DC=com'
        BIND_PW = '****'

        directory_service = DirectoryService(base_dn=BASE_DN, bind_password=BIND_PW, bind_user=BIND_USER, uris=[URI],
                                             enabled=True)
        res = self.directory_services.update_directory_services(names=[name], directory_service=directory_service)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating directory services configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_service** | [**DirectoryService**](DirectoryService.md)|  | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**DirectoryServiceResponse**](DirectoryServiceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_directory_services_roles**
> DirectoryServiceRolesResponse update_directory_services_roles(names, directory_service_role)



Update directory services roles configurations

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryServiceRole

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update Directory Services configuration
        ARRAY_ADMIN_GRP = 'admins'
        GROUP_BASE = 'ou=purestorage,ou=us'
        ROLE_NAME = 'array_admin'

        directory_service_role = DirectoryServiceRole(group_base=GROUP_BASE, array_admin_group=ARRAY_ADMIN_GRP)
        res = self.directory_services.update_directory_services_roles(names=[ROLE_NAME],
            directory_service_role=directory_service_role)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating directory services roles configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A required list of names. | 
 **directory_service_role** | [**DirectoryServiceRole**](DirectoryServiceRole.md)|  | 

### Return type

[**DirectoryServiceRolesResponse**](DirectoryServiceRolesResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

