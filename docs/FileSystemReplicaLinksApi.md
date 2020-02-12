# purity_fb_1dot9.FileSystemReplicaLinksApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_system_replica_link_policies**](FileSystemReplicaLinksApi.md#create_file_system_replica_link_policies) | **POST** /1.9/file-system-replica-links/policies | 
[**create_file_system_replica_links**](FileSystemReplicaLinksApi.md#create_file_system_replica_links) | **POST** /1.9/file-system-replica-links | 
[**delete_file_system_replica_link_policies**](FileSystemReplicaLinksApi.md#delete_file_system_replica_link_policies) | **DELETE** /1.9/file-system-replica-links/policies | 
[**list_file_system_replica_link_policies**](FileSystemReplicaLinksApi.md#list_file_system_replica_link_policies) | **GET** /1.9/file-system-replica-links/policies | 
[**list_file_system_replica_link_transfer**](FileSystemReplicaLinksApi.md#list_file_system_replica_link_transfer) | **GET** /1.9/file-system-replica-links/transfer | 
[**list_file_system_replica_links**](FileSystemReplicaLinksApi.md#list_file_system_replica_links) | **GET** /1.9/file-system-replica-links | 


# **create_file_system_replica_link_policies**
> PolicyMemberWithRemoteResponse create_file_system_replica_link_policies(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names)



Create a connection between a file system replica link and a policy.

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
        res = fb.file_system_replica_links.create_file_system_replica_link_policies(
                policy_names=['policy_1'],
                local_file_system_names=['local_fs'],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when add policy to file system replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_names** | [**list[str]**](str.md)| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | [**list[str]**](str.md)| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | [**list[str]**](str.md)| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | [**list[str]**](str.md)| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

[**PolicyMemberWithRemoteResponse**](PolicyMemberWithRemoteResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_file_system_replica_links**
> FileSystemReplicaLinkResponse create_file_system_replica_links(local_file_system_ids=local_file_system_ids, local_file_system_names=local_file_system_names, remote_ids=remote_ids, remote_names=remote_names, remote_file_system_names=remote_file_system_names, file_system_replica_link=file_system_replica_link)



Create new file system replica links.

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
        res = fb.file_system_replica_links.create_file_system_replica_links(
                local_file_system_names=["local_fs"],
                remote_file_system_names=["remote_fs"],
                remote_names=[REMOTE_ARRAY],
                file_system_replica_link=FileSystemReplicaLink(policies=[LocationReference(name=POLICY_NAME)]))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating file system replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **local_file_system_names** | [**list[str]**](str.md)| A comma-separated list of local file system names. This cannot be provided together with &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **remote_file_system_names** | [**list[str]**](str.md)| A comma-separated list of remote file system names. | [optional] 
 **file_system_replica_link** | [**FileSystemReplicaLink**](FileSystemReplicaLink.md)| The attribute map used to create the file system replica link. | [optional] 

### Return type

[**FileSystemReplicaLinkResponse**](FileSystemReplicaLinkResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_system_replica_link_policies**
> delete_file_system_replica_link_policies(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names)



Delete a connection betwwen a file system replica link and a policy.

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
        res = fb.file_system_replica_links.delete_file_system_replica_link_policies(
                policy_names=['policy_1'],
                member_names=['local_fs'],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when add policy to file system replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_names** | [**list[str]**](str.md)| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | [**list[str]**](str.md)| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | [**list[str]**](str.md)| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | [**list[str]**](str.md)| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
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

# **list_file_system_replica_link_policies**
> PolicyMemberWithRemoteResponse list_file_system_replica_link_policies(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names, remote_file_system_names=remote_file_system_names, remote_file_system_ids=remote_file_system_ids, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policies attached to file system replica links.

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
        # list all replica link and policy connections
        res = fb.file_system_replica_links.list_filesystem_replica_link_policies()
        print(res)
        # list first five replica link and policy connections and sort by local file system
        res = fb.file_system_replica_links.list_filesystem_replica_link_policies(limit=5, sort='member.name')
        print(res)
        # list remaining replica link and policies
        res = fb.file_system_replica_links.list_filesystem_replica_link_policies(
                token=res.pagination_info.continuation_token)
        print(res)
        # list a specific replica link and policy connection
        res = fb.file_system_replica_links.list_filesystem_replica_link_policies(
                policy_names=['policy_1'],
                member_names=['local_fs'],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing replica links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_names** | [**list[str]**](str.md)| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | [**list[str]**](str.md)| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | [**list[str]**](str.md)| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | [**list[str]**](str.md)| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **remote_file_system_names** | [**list[str]**](str.md)| A comma-separated list of remote file system names. This cannot be provided together with &#x60;remote_file_system_ids&#x60; query parameter. | [optional] 
 **remote_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of remote file system IDs. This cannot be provided together with &#x60;remote_file_system_names&#x60; query parameter. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**PolicyMemberWithRemoteResponse**](PolicyMemberWithRemoteResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_replica_link_transfer**
> FileSystemSnapshotTransferResponse list_file_system_replica_link_transfer(ids=ids, remote_ids=remote_ids, remote_names=remote_names, names_or_owner_names=names_or_owner_names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)



List file system replica link transfer records

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
        res = fb.file_system_replica_links.list_file_system_replica_link_transfer()
        print(res)
        # list first five filesystems and sort by provisioned in descendant order
        res = fb.file_system_replica_links.list_file_system_replica_link_transfer(names_or_owner_names=["myfs.mysnap"])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **names_or_owner_names** | [**list[str]**](str.md)| A comma-separated list of resource names. Either the name of the snapshot or the owning file system. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**FileSystemSnapshotTransferResponse**](FileSystemSnapshotTransferResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_replica_links**
> FileSystemReplicaLinkResponse list_file_system_replica_links(ids=ids, filter=filter, limit=limit, local_file_system_ids=local_file_system_ids, local_file_system_names=local_file_system_names, remote_file_system_names=remote_file_system_names, remote_ids=remote_ids, remote_names=remote_names, sort=sort, start=start, token=token)



List file system replica links.

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
        # list all replica links
        fb.file_system_replica_links.list_file_system_replica_links()
        # list first five replica links and sort by local file system
        res = fb.file_system_replica_links.list_file_system_replica_links(limit=5, sort='local_file_system.name')
        print(res)
        # list remaining replica links
        res = fb.file_system_replica_links.list_file_system_replica_links(token=res.pagination_info.continuation_token)
        print(res)
        # list replica links on the remote
        res = fb.file_system_replica_links.list_file_system_replica_links(remote_names=[REMOTE_ARRAY])
        print(res)
        # list with filter to see only replica links that are paused
        res = fb.file_system_replica_links.list_file_system_replica_links(filter='paused')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing replica links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **local_file_system_ids** | [**list[str]**](str.md)| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **local_file_system_names** | [**list[str]**](str.md)| A comma-separated list of local file system names. This cannot be provided together with &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **remote_file_system_names** | [**list[str]**](str.md)| A comma-separated list of remote file system names. | [optional] 
 **remote_ids** | [**list[str]**](str.md)| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | [**list[str]**](str.md)| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**FileSystemReplicaLinkResponse**](FileSystemReplicaLinkResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

