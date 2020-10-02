# purity_fb_1dot10.TargetsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_targets**](TargetsApi.md#create_targets) | **POST** /1.10/targets | 
[**delete_targets**](TargetsApi.md#delete_targets) | **DELETE** /1.10/targets | 
[**list_targets**](TargetsApi.md#list_targets) | **GET** /1.10/targets | 
[**list_targets_performance_replication**](TargetsApi.md#list_targets_performance_replication) | **GET** /1.10/targets/performance/replication | 
[**update_targets**](TargetsApi.md#update_targets) | **PATCH** /1.10/targets | 


# **create_targets**
> TargetResponse create_targets(target, names=names)



Create a new target.

### Example 
```python
from purity_fb import PurityFb, TargetPost, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a target by hostname name
    name = "target"
    hostname = "my.target.com"
    target = TargetPost(address=hostname)
    try:
        # post the target object on the array
        res = fb.targets.create_targets(names=[name], target=target)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating target: %s\n" % e)

    # create a target by ip address
    name = "target2"
    address = "1.1.1.1"
    target = TargetPost(address=address)
    try:
        # post the target object on the array
        res = fb.targets.create_targets(names=[name], target=target)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | [**TargetPost**](TargetPost.md)| The attribute map used to create the target. | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**TargetResponse**](TargetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_targets**
> delete_targets(ids=ids, names=names)



Delete a target.

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
        # delete the target with the name 'target'
        fb.targets.delete_targets(names=['target'])

        # delete the target with the id '10314f42-020d-7080-8013-000ddt400090'
        fb.targets.delete_targets(ids=['10314f42-020d-7080-8013-000ddt400090'])
    except rest.ApiException as e:
        print("Exception when deleting target: %s\n" % e)
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

# **list_targets**
> TargetResponse list_targets(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List targets.

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
        # list all targets
        fb.targets.list_targets()
        # list first three targets using default sort
        res = fb.targets.list_targets(limit=3)
        print(res)
        # list first three targets and sort by address
        res = fb.targets.list_targets(limit=3, sort='address')
        print(res)
        # list all remaining targets
        res = fb.targets.list_targets(token=res.pagination_info.continuation_token)
        print(res)
        # list with filter to see only targets that match a specific ip format
        res = fb.targets.list_targets(filter='name=\'12.56.23.*\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing targets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**TargetResponse**](TargetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_targets_performance_replication**
> PerformanceReplicationResponse list_targets_performance_replication(end_time=end_time, filter=filter, ids=ids, limit=limit, names=names, resolution=resolution, sort=sort, start=start, start_time=start_time, token=token, total_only=total_only, type=type)



List instant or historical target replication performance.

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
        # list instantaneous replication performance for all targets
        res = fb.targets.list_targets_performance_replication()
        print(res)

        # list instantaneous file-replication performance for all targets
        res = fb.targets.list_targets_performance_replication(type='file-system')
        print(res)

        # list instantaneous file-replication performance for target with id '10314f42-020d-7080-8013-000ddt400090'
        res = fb.targets.list_targets_performance_replication(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                             type='file-system')
        print(res)

        # list historical object-replication performance for all targets between some
        # start time and end time
        res = fb.target.list_targets_performance_replication(
            start_time=START_TIME,
            end_time=END_TIME,
            type='object-store',
            resolution=30000)
        print(res)

        # list historical object-replication performance for target 's3target1' between some
        # start time and end time
        res = fb.target.list_targets_performance_replication(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000,
            type='object-store',
            names=['s3target1'])
        print(res)

        # total instantaneous performance across 2 targets for object-replication
        res = fb.target.list_targets_performance_replication(names=['s3target1', 's3target2'], type='object-store',
                                                             total_only=True)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing target replication performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **type** | **str**| to sample space of either file systems, object store, or all | [optional] 

### Return type

[**PerformanceReplicationResponse**](PerformanceReplicationResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_targets**
> TargetResponse update_targets(target, ids=ids, names=names)



Update an existing target.

### Example 
```python
from purity_fb import PurityFb, Target, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # Change the name of an existing target to "remote2"
    # Change the address of an existing target to "1.1.1.1"
    new_attr = Target(name='remote2',
                      address='1.1.1.1')
    try:
        # Update the existing target that's named 'remote1' with our new attributes
        res = fb.targets.update_targets(names=['remote1'], target=new_attr)
        print(res)

        # Update the existing target that has the id '10314f42-020d-7080-8013-000ddt400090' with our new attributes
        res = fb.targets.update_targets(ids=['10314f42-020d-7080-8013-000ddt400090'], target=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating target: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | [**Target**](Target.md)| The attribute map used to update the target. | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**TargetResponse**](TargetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

