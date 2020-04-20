# purity_fb_1dot11.BladeApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_blades**](BladeApi.md#list_blades) | **GET** /1.11/blades | 


# **list_blades**
> BladeResponse list_blades(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List blades.

### Example 
```python
from purity_fb import PurityFb, Blade, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # list all blades
        res = fb.blade.list_blades()
        # list a subset of blades by name
        res = fb.blade.list_blades(names=['CH1.FB1', 'CH1.FB2'])
        # list a subset of blades by id
        res = fb.blade.list_blades(names=['100abf42-0000-4000-8023-000det400090',
                                          '10314f42-020d-7080-8013-000ddt400090'])
        # list all healthy blades
        res = fb.blade.list_blades(filter='status=\'healthy\'')
    except rest.ApiException as e:
        print("Exception when listing blades: %s\n" % e)
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

[**BladeResponse**](BladeResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

