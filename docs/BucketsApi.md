# purity_fb_1dot5.BucketsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buckets**](BucketsApi.md#create_buckets) | **POST** /1.5/buckets | 
[**delete_buckets**](BucketsApi.md#delete_buckets) | **DELETE** /1.5/buckets | 
[**list_buckets**](BucketsApi.md#list_buckets) | **GET** /1.5/buckets | 
[**update_buckets**](BucketsApi.md#update_buckets) | **PATCH** /1.5/buckets | 


# **create_buckets**
> BucketResponse create_buckets(account=account, names=names)



Create new buckets

### Example 
```python
from purity_fb import PurityFb, rest, Bucket, Reference

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post the bucket object mybucket on the array
        attr = Bucket()
        attr.account = Reference(name='myaccount')
        res = fb.buckets.create_buckets(names=["mybucket"], account=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account** | [**BucketPost**](BucketPost.md)| bucket create parameters | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_buckets**
> delete_buckets(names=names)



Delete buckets by name(s)

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
        # delete the bucket object mybucket on the array
        res = fb.buckets.delete_buckets(names=["mybucket"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store account: %s\n" % e)
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

# **list_buckets**
> BucketResponse list_buckets(filter=filter, sort=sort, start=start, limit=limit, token=token, total_only=total_only, names=names)



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
        print(res)
        # list and sort by unique in descendant order
        res = fb.buckets.list_buckets(limit=5, sort="space.unique-")
        print(res)
        # list with page size 5
        res = fb.buckets.list_buckets(limit=5)
        print(res)
        # list all remaining object store accounts
        res = fb.buckets.list_buckets(token=res.pagination_info.continuation_token)
        print(res)
        # list with filter
        res = fb.buckets.list_buckets(filter='name=\'mybucket*\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing buckets: %s\n" % e)        print("Exception when listing buckets: %s\n" % e)
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
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_buckets**
> BucketResponse update_buckets(destroyed=destroyed, names=names)



Update buckets

### Example 
```python
from purity_fb import PurityFb, rest, Bucket

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update the bucket object mybucket on the array
        res = fb.buckets.update_buckets(names=["mybucket"], destroyed=Bucket(destroyed=True))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destroyed** | [**BucketPatch**](BucketPatch.md)| bucket update parameters | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

