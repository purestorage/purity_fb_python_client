# purity_fb_1dot4.AdminsCacheApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_admin_cache**](AdminsCacheApi.md#delete_admin_cache) | **DELETE** /1.4/admins/cache | 
[**list_admin_cache**](AdminsCacheApi.md#list_admin_cache) | **GET** /1.4/admins/cache | 


# **delete_admin_cache**
> delete_admin_cache(names=names)



Delete

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
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_admin_cache**
> AdminCacheResponse list_admin_cache(names, refresh=refresh, filter=filter, limit=limit, sort=sort, start=start, token=token)



A list of admin cache entries

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
        # refresh admin cache entry
        res = fb.admin_cache.list_admin_cache(names=['adminuser'], refresh=True)
    except rest.ApiException as e:
        print("Exception when listing admin cache users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A required list of names. | 
 **refresh** | **bool**| Whether to refresh the user info from directory service | [optional] [default to false]
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
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

