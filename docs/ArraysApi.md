# purity_fb_1dot12.ArraysApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_arrays**](ArraysApi.md#list_arrays) | **GET** /1.12/arrays | 
[**list_arrays_http_specific_performance**](ArraysApi.md#list_arrays_http_specific_performance) | **GET** /1.12/arrays/http-specific-performance | 
[**list_arrays_nfs_specific_performance**](ArraysApi.md#list_arrays_nfs_specific_performance) | **GET** /1.12/arrays/nfs-specific-performance | 
[**list_arrays_performance**](ArraysApi.md#list_arrays_performance) | **GET** /1.12/arrays/performance | 
[**list_arrays_performance_replication**](ArraysApi.md#list_arrays_performance_replication) | **GET** /1.12/arrays/performance/replication | 
[**list_arrays_s3_specific_performance**](ArraysApi.md#list_arrays_s3_specific_performance) | **GET** /1.12/arrays/s3-specific-performance | 
[**list_arrays_space**](ArraysApi.md#list_arrays_space) | **GET** /1.12/arrays/space | 
[**list_clients_performance**](ArraysApi.md#list_clients_performance) | **GET** /1.12/arrays/clients/performance | 
[**list_eulas**](ArraysApi.md#list_eulas) | **GET** /1.12/arrays/eula | 
[**list_supported_time_zones**](ArraysApi.md#list_supported_time_zones) | **GET** /1.12/arrays/supported-time-zones | 
[**update_arrays**](ArraysApi.md#update_arrays) | **PATCH** /1.12/arrays | 
[**update_eulas**](ArraysApi.md#update_eulas) | **PATCH** /1.12/arrays/eula | 


# **list_arrays**
> ArrayResponse list_arrays()



List arrays

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
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]

### Return type

[**ArrayHttpPerformanceResponse**](ArrayHttpPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_arrays_nfs_specific_performance**
> ArrayNfsPerformanceResponse list_arrays_nfs_specific_performance(start_time=start_time, end_time=end_time, resolution=resolution)



List instant or historical nfs specific performance

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
        res = fb.arrays.list_arrays_nfs_specific_performance()
        print(res)
        # list nfs specific performance and sort by sample time (latest first)
        res = fb.arrays.list_arrays_nfs_specific_performance(sort='time-')
        # list historical nfs performance
        res = fb.arrays.list_arrays_nfs_specific_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000)
    except rest.ApiException as e:
        print("Exception when listing nfs performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]

### Return type

[**ArrayNfsPerformanceResponse**](ArrayNfsPerformanceResponse.md)

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
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
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

# **list_arrays_performance_replication**
> ArrayPerformanceReplicationResponse list_arrays_performance_replication(end_time=end_time, resolution=resolution, start_time=start_time, type=type)



List instant or historical array replication performance.

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
        # list instantaneous replication performance for array
        res = fb.arrays.list_arrays_performance_replication()
        print(res)

        # list instantaneous file-replication performance for array
        res = fb.arrays.list_arrays_performance_replication(type='file-system')
        print(res)

        # list historical object-replication performance for array between some
        # start time and end time
        res = fb.arrays.list_arrays_performance_replication(
            start_time=START_TIME,
            end_time=END_TIME,
            type='object-store',
            resolution=30000)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing array replication performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **type** | **str**| to sample space of either file systems, object store, or all | [optional] 

### Return type

[**ArrayPerformanceReplicationResponse**](ArrayPerformanceReplicationResponse.md)

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
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
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
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **type** | **str**| to sample space of either file systems, object store, or all | [optional] 

### Return type

[**ArraySpaceResponse**](ArraySpaceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_clients_performance**
> ClientPerformanceResponse list_clients_performance(names=names, filter=filter, sort=sort, limit=limit, total_only=total_only)



List client performance

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
        # list client performance for all clients
        res = fb.arrays.list_clients_performance()
        # list client performance for one specific array client
        res = fb.arrays.list_clients_performance(names=['123.123.123.123:8080'])
    except rest.ApiException as e:
        print("Exception when listing client performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**ClientPerformanceResponse**](ClientPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_eulas**
> EulaResponse list_eulas(filter=filter, limit=limit, sort=sort, start=start, token=token)



Displays the End User Agreement and signature.

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
        res = fb.arrays.list_eulas()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing eulas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**EulaResponse**](EulaResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_supported_time_zones**
> SupportedTimeZoneResponse list_supported_time_zones(filter=filter, limit=limit, names=names, sort=sort, start=start, token=token)



Lists the time zones supported by the array.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # List all supported time zones.
        res = fb.arrays.list_supported_time_zones()
        print(res)

        # List a specific time zone.
        res = fb.arrays.list_supported_time_zones(names=['Africa/Djibouti'])
        print(res)

        # List the only five time zones starting with "Asia".
        res = fb.arrays.list_supported_time_zones(limit=5, filter='name=\'Asia/*\'')
        print(res)
    except rest.ApiException as e:
        print('Exception when listing supported time zones: %s\n' % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**SupportedTimeZoneResponse**](SupportedTimeZoneResponse.md)

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

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Set the banner to "example-banner"
        # Rename the array to "example-name"
        # Set the NTP server to "0.example.ntp.server"
        # Change the array time zone to "America/Los_Angeles"
        # Updating idle_timeout to 300000, in milliseconds
        array_settings = PureArray(banner="example-banner",
                                   name="example-name",
                                   ntp_servers=["0.example.ntp.server"],
                                   time_zone="America/Los_Angeles",
                                   idle_timeout=300000)
        res = fb.arrays.update_arrays(array_settings=array_settings)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating arrays: %s\n" % e)
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

# **update_eulas**
> EulaResponse update_eulas(eula)



Modifies the signature on the End User Agreement.

### Example 
```python
from purity_fb import PurityFb, rest, Eula, EulaSignature

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Update the Eula signature
        signature = EulaSignature(name="example name", title="example", company="one company")
        eula_body = Eula(signature=signature)
        res = fb.arrays.update_eulas(eula=eula_body)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating eula: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eula** | [**Eula**](Eula.md)|  | 

### Return type

[**EulaResponse**](EulaResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

