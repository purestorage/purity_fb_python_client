# purity_fb.ArraysApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_arrays**](ArraysApi.md#list_arrays) | **GET** /1.3/arrays | 
[**list_arrays_http_specific_performance**](ArraysApi.md#list_arrays_http_specific_performance) | **GET** /1.3/arrays/http-specific-performance | 
[**list_arrays_performance**](ArraysApi.md#list_arrays_performance) | **GET** /1.3/arrays/performance | 
[**list_arrays_s3_specific_performance**](ArraysApi.md#list_arrays_s3_specific_performance) | **GET** /1.3/arrays/s3-specific-performance | 
[**list_arrays_space**](ArraysApi.md#list_arrays_space) | **GET** /1.3/arrays/space | 
[**update_arrays**](ArraysApi.md#update_arrays) | **PATCH** /1.3/arrays | 


# **list_arrays**
> ArrayResponse list_arrays()



List arrays

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
        res = fb.arrays.list_arrays()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing arrays: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayResponse**](ArrayResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_arrays_http_specific_performance**
> ArrayHttpPerformanceResponse list_arrays_http_specific_performance(start_time=start_time, end_time=end_time, resolution=resolution)



List instant or historical http specific performance

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
        res = fb.arrays.list_arrays_http_specific_performance()
        print(res)
        # list http specific performance and sort by sample time (latest first)
        res = fb.alerts.list_arrays_http_specific_performance(sort='time-')
        # list historical http performance
        res = fb.alerts.list_arrays_http_specific_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)
    except rest.ApiException as e:
        print("Exception when listing http performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| time to start sample in milliseconds since epoch | [optional] 
 **end_time** | **int**| time to end sample in milliseconds since epoch | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]

### Return type

[**ArrayHttpPerformanceResponse**](ArrayHttpPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_arrays_performance**
> ArrayPerformanceResponse list_arrays_performance(start_time=start_time, end_time=end_time, resolution=resolution, protocol=protocol)



List instant or historical array performance

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
        res = fb.arrays.list_arrays_performance()
        print(res)
        # list array performance for http
        res = fb.alerts.list_arrays_performance(protocol='http')
        # list array performance for s3
        res = fb.alerts.list_arrays_performance(protocol='s3')
        # list array performance for nfs
        res = fb.alerts.list_arrays_performance(protocol='nfs')
        # list historical array performance
        res = fb.alerts.list_arrays_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)
    except rest.ApiException as e:
        print("Exception when listing array performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| time to start sample in milliseconds since epoch | [optional] 
 **end_time** | **int**| time to end sample in milliseconds since epoch | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **protocol** | **str**| to sample performance of a certain protocol | [optional] 

### Return type

[**ArrayPerformanceResponse**](ArrayPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_arrays_s3_specific_performance**
> ArrayS3PerformanceResponse list_arrays_s3_specific_performance(start_time=start_time, end_time=end_time, resolution=resolution)



List instant or historical object store specific performance

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
        res = fb.arrays.list_arrays_s3_specific_performance()
        print(res)
        # list s3 specific performance and sort by sample time (latest first)
        res = fb.arrays.list_arrays_s3_specific_performance(sort='time-')
        # list historical s3 performance
        res = fb.arrays.list_arrays_s3_specific_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)
    except rest.ApiException as e:
        print("Exception when listing s3 performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| time to start sample in milliseconds since epoch | [optional] 
 **end_time** | **int**| time to end sample in milliseconds since epoch | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]

### Return type

[**ArrayS3PerformanceResponse**](ArrayS3PerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_arrays_space**
> ArraySpaceResponse list_arrays_space(start_time=start_time, end_time=end_time, resolution=resolution, type=type)



List instant or historical array space

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
        res = fb.arrays.list_arrays_space()
        print(res)
        # list array space and sort by capacity
        res = fb.arrays.list_arrays_space(sort='capacity')
        print(res)
        # list array space of file systems
        res = fb.arrays.list_arrays_space(type='file-system')
        print(res)
        # list historical array space
        res = fb.arrays.list_arrays_space(start_time=START_TIME,
                                          end_time=END_TIME,
                                          resolution=30000)
    except rest.ApiException as e:
        print("Exception when listing array space: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| time to start sample in milliseconds since epoch | [optional] 
 **end_time** | **int**| time to end sample in milliseconds since epoch | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **type** | **str**| to sample space of either file systems or object store | [optional] 

### Return type

[**ArraySpaceResponse**](ArraySpaceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_arrays**
> ArrayResponse update_arrays(array_settings)



Update arrays

### Example 
```python
from purity_fb import PurityFb, PureArray, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        array_settings = PureArray(name="example-name", ntp_servers=["0.example.ntp.server"])
        res = fb.arrays.update_arrays(array_settings=array_settings)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing arrays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_settings** | [**PureArray**](PureArray.md)|  | 

### Return type

[**ArrayResponse**](ArrayResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

