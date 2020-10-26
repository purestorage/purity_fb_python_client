# purity_fb_1dot11.BucketsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_buckets**](BucketsApi.md#create_buckets) | **POST** /1.11/buckets | 
[**delete_buckets**](BucketsApi.md#delete_buckets) | **DELETE** /1.11/buckets | 
[**list_buckets**](BucketsApi.md#list_buckets) | **GET** /1.11/buckets | 
[**list_buckets_performance**](BucketsApi.md#list_buckets_performance) | **GET** /1.11/buckets/performance | 
[**list_buckets_s3_specific_performance**](BucketsApi.md#list_buckets_s3_specific_performance) | **GET** /1.11/buckets/s3-specific-performance | 
[**update_buckets**](BucketsApi.md#update_buckets) | **PATCH** /1.11/buckets | 


# **create_buckets**
> BucketResponse create_buckets(names=names, bucket=bucket)



Create new buckets.

### Example 
```python
from purity_fb import PurityFb, rest, BucketPost, Reference

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post the bucket object mybucket on the array
        attr = BucketPost()
        attr.account = Reference(name='myaccount')
        res = fb.buckets.create_buckets(names=["mybucket"], bucket=attr)

        # make another bucket in the account with id '10314f42-020d-7080-8013-000ddt400090'
        id_attr = BucketPost()
        id_attr.account = Reference(id='10314f42-020d-7080-8013-000ddt400090')
        res = fb.buckets.create_buckets(names=["mybucket"], bucket=id_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **bucket** | [**BucketPost**](BucketPost.md)| Bucket create parameters. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_buckets**
> delete_buckets(ids=ids, names=names)



Delete buckets.

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
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_buckets**
> BucketResponse list_buckets(filter=filter, ids=ids, names=names, limit=limit, sort=sort, start=start, token=token, total_only=total_only)



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
        print("Exception when listing buckets: %s\n" % e)
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
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_buckets_performance**
> BucketPerformanceResponse list_buckets_performance(resolution=resolution, end_time=end_time, filter=filter, ids=ids, limit=limit, names=names, sort=sort, start_time=start_time, start=start, token=token, total_only=total_only)



List instant or historical bucket performance.

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
        # list instantaneous performance for all buckets
        res = fb.buckets.list_buckets_performance()

        # list instantaneous performance for buckets 'bucket1' and 'bucket2'
        res = fb.buckets.list_buckets_performance(names=['bucket1', 'bucket2'])

        # list historical buckets performance for all buckets between some
        # start time and end time
        res = fb.buckets.list_buckets_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)

        # list historical buckets performance for buckets 'bucket1' and 'bucket2' between some
        # start time and end time
        res = fb.buckets.list_buckets_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000,
            names=['bucket1', 'bucket2'])

        # total instantaneous performance across 2 buckets
        res = fb.buckets.list_buckets_performance(names=['bucket1', 'bucket2'], total_only=True)
    except rest.ApiException as e:
        print("Exception when listing bucket performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**BucketPerformanceResponse**](BucketPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_buckets_s3_specific_performance**
> BucketS3PerformanceResponse list_buckets_s3_specific_performance(resolution=resolution, end_time=end_time, filter=filter, ids=ids, limit=limit, names=names, sort=sort, start_time=start_time, start=start, token=token, total_only=total_only)



List instant or historical bucket object store specific performance.

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
        # list instantaneous s3 specific performance for all buckets
        res = fb.buckets.list_buckets_s3_specific_performance()

        # list instantaneous s3 specific performance for buckets 'bucket1' and 'bucket2'
        res = fb.buckets.list_buckets_s3_specific_performance(names=['bucket1', 'bucket2'])

        # list historical buckets s3 specific performance for all buckets between some
        # start time and end time
        res = fb.buckets.list_buckets_s3_specific_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)

        # list historical buckets s3 specific performance for buckets 'bucket1' and 'bucket2' between some
        # start time and end time
        res = fb.buckets.list_buckets_s3_specific_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000,
            names=['bucket1', 'bucket2'])

        # total instantaneous s3 specific performance across 2 buckets
        res = fb.buckets.list_buckets_s3_specific_performance(names=['bucket1', 'bucket2'], total_only=True)
    except rest.ApiException as e:
        print("Exception when listing bucket s3 specific performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**BucketS3PerformanceResponse**](BucketS3PerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_buckets**
> BucketResponse update_buckets(ids=ids, names=names, bucket=bucket)



Update buckets.

### Example 
```python
from purity_fb import PurityFb, rest, BucketPatch

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Destroy the bucket named "mybucket", and also suspend versioning
        res = fb.buckets.update_buckets(names=["mybucket"],
                                        bucket=BucketPatch(destroyed=True, versioning="suspended"))

        # Recover the bucket "mybucket", and also enable versioning
        res = fb.buckets.update_buckets(names=["mybucket"],
                                        bucket=BucketPatch(destroyed=False, versioning="enabled"))

        print(res)
    except rest.ApiException as e:
        print("Exception when updating bucket: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **bucket** | [**BucketPatch**](BucketPatch.md)| Bucket update parameters. | [optional] 

### Return type

[**BucketResponse**](BucketResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

