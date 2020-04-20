# purity_fb_1dot11.AdminsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_admins**](AdminsApi.md#list_admins) | **GET** /1.11/admins | 
[**update_admins**](AdminsApi.md#update_admins) | **PATCH** /1.11/admins | 


# **list_admins**
> AdminResponse list_admins(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token, expose=expose)



List all administrative accounts.

### Example 
```python
from purity_fb import PurityFb, Admin, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # list all admin accounts (given sufficient permissions)
        res = fb.admins.list_admins()
        # list a subset of admin accounts by name
        res = fb.admins.list_admins(names=['pureuser'])
        # list a subset of admin accounts by id
        res = fb.admins.list_admins(ids=['100abf42-0000-4000-8023-000det400090'])
    except rest.ApiException as e:
        print("Exception when listing admins: %s\n" % e)
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
 **expose** | **bool**| Display the unmasked API token. This is only valid when listing your own token. | [optional] [default to false]

### Return type

[**AdminResponse**](AdminResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_admins**
> AdminResponse update_admins(admin, ids=ids, names=names)



Update administrative account attributes.

### Example 
```python
from purity_fb import PurityFb, Admin, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # change password
        myAdmin = Admin()
        myAdmin.old_password = "pureuser"
        myAdmin.password = "fakepass"
        res = fb.admins.update_admins(names=['pureuser'], admin=myAdmin)

    except rest.ApiException as e:
        print("Exception when changing password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin** | [**Admin**](Admin.md)|  | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**AdminResponse**](AdminResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

