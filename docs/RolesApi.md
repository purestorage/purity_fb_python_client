# purity_fb_1dot11.RolesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_roles**](RolesApi.md#list_roles) | **GET** /1.11/roles | 


# **list_roles**
> RoleResponse list_roles()



List roles.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all roles
        fb.roles.list_roles()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleResponse**](RoleResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

