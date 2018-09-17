# purity_fb_1dot5.FileSystemsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_systems**](FileSystemsApi.md#create_file_systems) | **POST** /1.5/file-systems | 
[**create_filesystem_policies**](FileSystemsApi.md#create_filesystem_policies) | **POST** /1.5/file-systems/policies | 
[**delete_file_systems**](FileSystemsApi.md#delete_file_systems) | **DELETE** /1.5/file-systems | 
[**delete_filesystem_policies**](FileSystemsApi.md#delete_filesystem_policies) | **DELETE** /1.5/file-systems/policies | 
[**list_file_systems**](FileSystemsApi.md#list_file_systems) | **GET** /1.5/file-systems | 
[**list_file_systems_performance**](FileSystemsApi.md#list_file_systems_performance) | **GET** /1.5/file-systems/performance | 
[**list_filesystem_policies**](FileSystemsApi.md#list_filesystem_policies) | **GET** /1.5/file-systems/policies | 
[**update_file_systems**](FileSystemsApi.md#update_file_systems) | **PATCH** /1.5/file-systems | 


# **create_file_systems**
> FileSystemResponse create_file_systems(file_system)



Create a new file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, NfsRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with given name, provisioned size, and NFS enabled.
    myfs = FileSystem(name="myfs", provisioned="5000", hard_limit_enabled=True, nfs=NfsRule(enabled=True))
    try:
        # post the file system object myfs on the array
        res = fb.file_systems.create_file_systems(file_system=myfs)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system** | [**FileSystem**](FileSystem.md)| the attribute map used to create the file system | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_filesystem_policies**
> PolicyObjectsResponse create_filesystem_policies(policy_names=policy_names, member_names=member_names)



Create a connection between a file system and a policy

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
        # attach policy to a file system
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.file_systems.create_filesystem_policies(policy_names=["p1"],
                                                         member_names=["myfs"])
        print(res)
    except rest.ApiException as e:
        print("Exception when attaching policy to a file system: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_names** | [**list[str]**](str.md)| A list of policy names. | [optional] 
 **member_names** | [**list[str]**](str.md)| A list of member names. | [optional] 

### Return type

[**PolicyObjectsResponse**](PolicyObjectsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_systems**
> delete_file_systems(name)



Delete a file system by name

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
        # eradicate a file system with name myfs
        fb.file_systems.delete_file_systems(name="myfs")
    except rest.ApiException as e:
        print("Exception when deleting file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_filesystem_policies**
> delete_filesystem_policies(policy_names=policy_names, member_names=member_names)



Delete a connection betwwen a file system and a policy

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
        # attach policy to a file system
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.file_systems.delete_filesystem_policies(policy_names=["p1"],
                                                         member_names=["myfs"])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting policy against a file system: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_names** | [**list[str]**](str.md)| A list of policy names. | [optional] 
 **member_names** | [**list[str]**](str.md)| A list of member names. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems**
> FileSystemResponse list_file_systems(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)



List file systems

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all file systems
        fb.file_systems.list_file_systems()
        # list first five filesystems using default sort
        res = fb.file_systems.list_file_systems(limit=5)
        # list first five filesystems and sort by provisioned in descendant order
        res = fb.file_systems.list_file_systems(limit=5, sort="provisioned-")
        # list all remaining file systems
        res = fb.file_systems.list_file_systems(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.file_systems.list_file_systems(filter='name=\'myfs*\' and nfs.enabled and not(smb.enabled)')
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| return a total object in addition to the other results | [optional] [default to false]
 **total_only** | **bool**| return only the total object | [optional] [default to false]

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems_performance**
> FileSystemPerformanceResponse list_file_systems_performance(resolution=resolution, protocol=protocol, end_time=end_time, filter=filter, limit=limit, names=names, sort=sort, start_time=start_time, start=start, token=token, total_only=total_only)



List instant or historical file system performance.

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
        # list instantaneous nfs performance for all file systems
        res = fb.file_systems.list_file_systems_performance(protocol='nfs')
        print(res)

        # list instantaneous nfs performance for file systems 'fs1' and 'fs2'
        res = fb.file_systems.list_file_systems_performance(names=['fs1', 'fs2'], protocol='nfs')
        print(res)

        # list historical file systems nfs performance for all file systems between some
        # start time and end time
        res = fb.file_systems.list_file_systems_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            protocol='nfs',
            resolution=30000)
        print(res)

        # list historical file systems nfs performance for file systems 'fs1' and 'fs2' between some
        # start time and end time
        res = fb.file_systems.list_file_systems_performance(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000,
            protocol='nfs',
            names=['fs1', 'fs2'])
        print(res)

        # total instantaneous performance across 2 filesystems
        res = fb.file_systems.list_file_systems_performance(names=['fs1', 'fs2'], protocol='nfs',
                                                            total_only=True)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing file system performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **protocol** | **str**| to sample performance of a certain protocol | [optional] 
 **end_time** | **int**| time to end sample in milliseconds since epoch | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start_time** | **int**| time to start sample in milliseconds since epoch | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 
 **total_only** | **bool**| return only the total object | [optional] [default to false]

### Return type

[**FileSystemPerformanceResponse**](FileSystemPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_filesystem_policies**
> PolicyObjectsResponse list_filesystem_policies(policy_names=policy_names, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to filesystems

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
        # list all policies
        res = fb.file_systems.list_filesystem_policies()
        print(res)
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.file_systems.list_filesystem_policies(policy_names=["p1"],
                                                        member_names=["myfs"])
        print(res)
        # list and sort by name in descendant order
        res = fb.file_systems.list_filesystem_policies(limit=5, sort="policy.name-")
        print(res)
        # list with page size 5
        res = fb.file_systems.list_filesystem_policies(limit=5)
        print(res)
        # list all remaining policies
        res = fb.file_systems.list_filesystem_policies(token=res.pagination_info.continuation_token)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing policy file system: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_names** | [**list[str]**](str.md)| A list of policy names. | [optional] 
 **member_names** | [**list[str]**](str.md)| A list of member names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**PolicyObjectsResponse**](PolicyObjectsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_systems**
> FileSystemResponse update_file_systems(name, attributes, ignore_usage=ignore_usage)



Update an existing file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, NfsRule, ProtocolRule, SmbRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with provisioned size, and NFS enabled
    # note that name field should be None
    new_attr = FileSystem(provisioned="1024", hard_limit_enabled=True, nfs=NfsRule(enabled=True), http=ProtocolRule(enabled=False), smb=SmbRule(enabled=True, acl_mode="native"))
    try:
        # update the file system named myfs on the array
        res = fb.file_systems.update_file_systems(name="myfs", ignore_usage=True, attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the file system to be updated | 
 **attributes** | [**FileSystem**](FileSystem.md)| the new attributes, only modifiable fields could be used. | 
 **ignore_usage** | **bool**| Allow update operations that lead to a hard_limit_enabled file system with usage over its provisioned size. The update can be either setting hard_limit_enabled when usage is higher than provisioned size, or resize provisioned size to a value under usage when hard_limit_enabled is True. | [optional] 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

