# purity_fb_1dot9.FileSystemSnapshotsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_system_snapshots**](FileSystemSnapshotsApi.md#create_file_system_snapshots) | **POST** /1.9/file-system-snapshots | 
[**delete_file_system_snapshots**](FileSystemSnapshotsApi.md#delete_file_system_snapshots) | **DELETE** /1.9/file-system-snapshots | 
[**delete_file_system_snapshots_transfer**](FileSystemSnapshotsApi.md#delete_file_system_snapshots_transfer) | **DELETE** /1.9/file-system-snapshots/transfer | 
[**delete_filesystem_snapshot_policies**](FileSystemSnapshotsApi.md#delete_filesystem_snapshot_policies) | **DELETE** /1.9/file-system-snapshots/policies | 
[**list_file_system_snapshots**](FileSystemSnapshotsApi.md#list_file_system_snapshots) | **GET** /1.9/file-system-snapshots | 
[**list_file_system_snapshots_transfer**](FileSystemSnapshotsApi.md#list_file_system_snapshots_transfer) | **GET** /1.9/file-system-snapshots/transfer | 
[**list_filesystem_snapshot_policies**](FileSystemSnapshotsApi.md#list_filesystem_snapshot_policies) | **GET** /1.9/file-system-snapshots/policies | 
[**update_file_system_snapshots**](FileSystemSnapshotsApi.md#update_file_system_snapshots) | **PATCH** /1.9/file-system-snapshots | 


# **create_file_system_snapshots**
> FileSystemSnapshotResponse create_file_system_snapshots(sources=sources, source_ids=source_ids, send=send, targets=targets, suffix=suffix)



Create snapshots for the specified source file systems.

### Example 
```python
from purity_fb import PurityFb, SnapshotSuffix, rest
from settings import ARRAY, REMOTE_ARRAY, API_TOKEN, VERSION 


fb = PurityFb(ARRAY, version=VERSION)
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
        res = fb.file_system_snapshots.create_file_system_snapshots(sources=["myfs"],
                                                                    suffix=SnapshotSuffix("mysnap"))
        print(res)
        # create a snapshot with suffix mysnap for the file system named myfs
        res = fb.file_system_snapshots.create_file_system_snapshots(sources=["myfs"],
                                                                    send=True,
                                                                    targets=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | [**list[str]**](str.md)| A comma-separated list of names of source file systems. | [optional] 
 **source_ids** | [**list[str]**](str.md)| A comma-separated list of IDs of source file systems. | [optional] 
 **send** | **bool**| Whether to replicate created snapshots immediately to other arrays. If it&#39;s false, created snapshots may still be replicated to other arrays according to policy. | [optional] 
 **targets** | [**list[str]**](str.md)| A comma-separated list of targets arrays to replicate created snapshots to. Only valid when send is true. | [optional] 
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
> delete_file_system_snapshots(name, ids=ids)



Delete a file system snapshot.

### Example 
```python
from purity_fb import PurityFb, rest
from settings import ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
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
 **name** | **str**| The name of the file system or snapshot to be updated. | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_system_snapshots_transfer**
> delete_file_system_snapshots_transfer(ids=ids, names=names, remote_ids=remote_ids, remote_names=remote_names)



Cancel not completed snapshot transfers.

### Example 
```python
from purity_fb import PurityFb, rest
from settings import ARRAY, REMOTE_ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # eradicate a file system snapshot named myfs.mysnap
        res = fb.file_system_snapshots.delete_file_system_snapshots_transfer(names=["myfs.mysnap"],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_filesystem_snapshot_policies**
> delete_filesystem_snapshot_policies(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Delete a connection betwwen a file system snapshot and a policy.

### Example 
```python
from purity_fb import PurityFb, rest
from settings import ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # remove policy with id from a file system snapshot named myfs.2
        res = fb.file_system_snapshots.delete_filesystem_snapshot_policies(policy_ids=["10314f42-020d-7080-8013-000ddt400090"],
                                                                            member_names=["myfs.2"])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting policy from file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | [**list[str]**](str.md)| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | [**list[str]**](str.md)| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | [**list[str]**](str.md)| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | [**list[str]**](str.md)| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_snapshots**
> FileSystemSnapshotResponse list_file_system_snapshots(filter=filter, ids=ids, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only, names_or_sources=names_or_sources, names_or_owner_names=names_or_owner_names, source_ids=source_ids, owner_ids=owner_ids)



List file system snapshots.

### Example 
```python
from purity_fb import PurityFb, rest
from settings import ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
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
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **names_or_sources** | [**list[str]**](str.md)| A comma-separated list of resource names. Either the name of the snapshot or the source file system. | [optional] 
 **names_or_owner_names** | [**list[str]**](str.md)| A comma-separated list of resource names. Either the name of the snapshot or the owning file system. | [optional] 
 **source_ids** | [**list[str]**](str.md)| A comma-separated list of IDs of source file systems. | [optional] 
 **owner_ids** | [**list[str]**](str.md)| A comma-separated list of IDs of owning file systems. | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_snapshots_transfer**
> FileSystemSnapshotTransferResponse list_file_system_snapshots_transfer(ids=ids, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only, names_or_owner_names=names_or_owner_names)



List file system snapshot transfer records

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest
from settings import ARRAY, REMOTE_ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all file systems
        res = fb.file_system_snapshots.list_file_system_snapshots_transfer()
        print(res)
        # list first five filesystems and sort by provisioned in descendant order
        res = fb.file_system_snapshots.list_file_system_snapshots_transfer(names_or_owner_names=["myfs.mysnap"])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **names_or_owner_names** | [**list[str]**](str.md)| A comma-separated list of resource names. Either the name of the snapshot or the owning file system. | [optional] 

### Return type

[**FileSystemSnapshotTransferResponse**](FileSystemSnapshotTransferResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_filesystem_snapshot_policies**
> PolicyMemberResponse list_filesystem_snapshot_policies(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policies attached to filesystem snapshots.

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
 **policy_ids** | [**list[str]**](str.md)| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | [**list[str]**](str.md)| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | [**list[str]**](str.md)| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | [**list[str]**](str.md)| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**PolicyMemberResponse**](PolicyMemberResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_system_snapshots**
> FileSystemSnapshotResponse update_file_system_snapshots(name, attributes, ids=ids, latest_replica=latest_replica)



Update an existing file system snapshot.

### Example 
```python
from purity_fb import PurityFb, FileSystemSnapshot, rest
from settings import ARRAY, REMOTE_ARRAY, API_TOKEN, VERSION

fb = PurityFb(ARRAY, version=VERSION)
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
        # destroying the latest replicated snapshot should specify "latest_replica=True"
        res = fb.file_system_snapshots.update_file_system_snapshots(name="myfs.mysnap",
                                                                    latest_replica=True,
                                                                    attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file system or snapshot to be updated. | 
 **attributes** | [**SnapshotSuffix**](SnapshotSuffix.md)| The new attributes, only modifiable fields may be specified. | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **latest_replica** | **bool**| Used when destroying a snapshot. If not present or false, and the snapshot is the latest replicated snapshot, then destroy will fail. If true or the snapshot is not the latest replicated snapshot, then destroy will be successful. | [optional] [default to false]

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

