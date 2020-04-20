# purity_fb_1dot11.AdminsCacheApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_admin_cache**](AdminsCacheApi.md#delete_admin_cache) | **DELETE** /1.11/admins/cache | 
[**list_admin_cache**](AdminsCacheApi.md#list_admin_cache) | **GET** /1.11/admins/cache | 


# **delete_admin_cache**
> delete_admin_cache(ids=ids, names=names)



Delete specified admin cache entries, or clear the cache.

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
        # delete an admin cache entry
        fb.admin_cache.delete_admin_cache(names=['adminuser'])
        # delete all admin cache entries
        fb.admin_cache.delete_admin_cache()

    except rest.ApiException as e:
        print("Exception when deleting an admin cache entry: %s\n" % e)
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

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_admin_cache**
> AdminCacheResponse list_admin_cache(refresh=refresh, filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List admin cache entries.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # list admin cache entry
        res = fb.admin_cache.list_admin_cache(names=['adminuser'])
        # refresh admin cache entry for user with id '10314f42-020d-7080-8013-000ddt400090'
        res = fb.admin_cache.list_admin_cache(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                              refresh=True)
    except rest.ApiException as e:
        print("Exception when listing admin cache users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether to refresh the user info from directory service | [optional] [default to false]
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**AdminCacheResponse**](AdminCacheResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

