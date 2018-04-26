# purity_fb.BucketsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_buckets**](BucketsApi.md#list_buckets) | **GET** /1.3/buckets | 


# **list_buckets**
> BucketResponse list_buckets(filter=filter, sort=sort, start=start, limit=limit, token=token, total_only=total_only)



List buckets

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
        # list all buckets
        res = fb.buckets.list_buckets()
        # list and sort by unique in descendant order
        res = fb.buckets.list_buckets(limit=5, sort="space.unique-")
        # list with page size 5
        res = fb.buckets.list_buckets(limit=5)
        # list all remaining object store accounts
        res = fb.buckets.list_buckets(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.buckets.list_buckets(filter='name=\'mybucket*\'')
    except rest.ApiException as e:
        print("Exception when listing buckets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total_only** | **bool**| return only the total object | [optional] [default to false]

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

