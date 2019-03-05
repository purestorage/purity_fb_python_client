# purity_fb_1dot6.FileSystemSnapshotsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_system_snapshots**](FileSystemSnapshotsApi.md#create_file_system_snapshots) | **POST** /1.6/file-system-snapshots | 
[**delete_file_system_snapshots**](FileSystemSnapshotsApi.md#delete_file_system_snapshots) | **DELETE** /1.6/file-system-snapshots | 
[**list_file_system_snapshots**](FileSystemSnapshotsApi.md#list_file_system_snapshots) | **GET** /1.6/file-system-snapshots | 
[**list_filesystem_snapshot_policies**](FileSystemSnapshotsApi.md#list_filesystem_snapshot_policies) | **GET** /1.6/file-system-snapshots/policies | 
[**update_file_system_snapshots**](FileSystemSnapshotsApi.md#update_file_system_snapshots) | **PATCH** /1.6/file-system-snapshots | 


# **create_file_system_snapshots**
> FileSystemSnapshotResponse create_file_system_snapshots(sources, suffix=suffix)



Create snapshots for the specified source file systems

### Example 
```python
from purity_fb import PurityFb, SnapshotSuffix, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create a snapshot for the file system named myfs
        res = fb.file_system_snapshots.create_file_system_snapshots(sources=["myfs"])
        print(res)
        # create a snapshot with suffix mysnap for the file system named myfs
        res = fb.file_system_snapshots.create_file_system_snapshots(sources=["myfs"], suffix=SnapshotSuffix("mysnap"))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | [**list[str]**](str.md)| A list of names of source file systems. | 
 **suffix** | [**SnapshotSuffix**](SnapshotSuffix.md)| the suffix of the snapshot | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_system_snapshots**
> delete_file_system_snapshots(name)



Delete a file system snapshot by name

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
        # eradicate a file system snapshot named myfs.mysnap
        res = fb.file_system_snapshots.delete_file_system_snapshots(name="myfs.mysnap")
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system snapshot to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_snapshots**
> FileSystemSnapshotResponse list_file_system_snapshots(filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only, names_or_sources=names_or_sources)



List file system snapshots

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
        # list all file system snapshots
        fb.file_system_snapshots.list_file_system_snapshots()
        # list with page size 5, and sort by source file system name
        res = fb.file_system_snapshots.list_file_system_snapshots(limit=5, sort="source")
        print(res)
        # list all remaining file system snapshots
        res = fb.file_system_snapshots.list_file_system_snapshots(token=res.pagination_info.continuation_token)
        print(res)
        # list with filter
        res = fb.file_system_snapshots.list_file_system_snapshots(filter='source=\'myfs*\' and contains(suffix, \'1\')')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **names_or_sources** | [**list[str]**](str.md)| A comma-separated list of resource names. Either the name of the snapshot or the source. | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_filesystem_snapshot_policies**
> PolicyObjectsResponse list_filesystem_snapshot_policies(policy_names=policy_names, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to filesystem snapshots

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
        res = fb.file_system_snapshots.list_filesystem_snapshot_policies()
        print(res)
        # assume we have a policy named "p1", and a file system snapshot named "myfs.1"
        res = fb.file_system_snapshots.list_filesystem_snapshot_policies(policy_names=["p1"],
                                                                         member_names=["myfs.1"])
        print(res)
        # list and sort by name in descendant order
        res = fb.file_system_snapshots.list_filesystem_snapshot_policies(limit=5, sort="policy.name-")
        print(res)
        # list with page size 5
        res = fb.file_system_snapshots.list_filesystem_snapshot_policies(limit=5)
        print(res)
        # list all remaining policies
        if (res.pagination_info.continuation_token != None):
            res = fb.file_system_snapshots.list_filesystem_snapshot_policies(token=res.pagination_info.continuation_token)
            print(res)
    except rest.ApiException as e:
        print("Exception when listing policy file system snapshot: %s\n" % e)
```

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

# **update_file_system_snapshots**
> FileSystemSnapshotResponse update_file_system_snapshots(name, attributes)



Update an existing file system snapshot

### Example 
```python
from purity_fb import PurityFb, FileSystemSnapshot, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system snapshot object with destroyed field being true
    new_attr = FileSystemSnapshot(destroyed=True)
    try:
        # destroying the file system snapshot myfs.mysnap
        res = fb.file_system_snapshots.update_file_system_snapshots(name="myfs.mysnap", attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file system snapshot to be updated. | 
 **attributes** | [**SnapshotSuffix**](SnapshotSuffix.md)| the new attributes, only modifiable fields could be used. | 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

