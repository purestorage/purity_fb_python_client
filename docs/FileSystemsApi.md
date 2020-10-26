# purity_fb_1dot11.FileSystemsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_systems**](FileSystemsApi.md#create_file_systems) | **POST** /1.11/file-systems | 
[**create_filesystem_policies**](FileSystemsApi.md#create_filesystem_policies) | **POST** /1.11/file-systems/policies | 
[**delete_file_systems**](FileSystemsApi.md#delete_file_systems) | **DELETE** /1.11/file-systems | 
[**delete_filesystem_policies**](FileSystemsApi.md#delete_filesystem_policies) | **DELETE** /1.11/file-systems/policies | 
[**list_file_systems**](FileSystemsApi.md#list_file_systems) | **GET** /1.11/file-systems | 
[**list_file_systems_performance**](FileSystemsApi.md#list_file_systems_performance) | **GET** /1.11/file-systems/performance | 
[**list_filesystem_policies**](FileSystemsApi.md#list_filesystem_policies) | **GET** /1.11/file-systems/policies | 
[**update_file_systems**](FileSystemsApi.md#update_file_systems) | **PATCH** /1.11/file-systems | 


# **create_file_systems**
> FileSystemResponse create_file_systems(file_system, overwrite=overwrite, discard_non_snapshotted_data=discard_non_snapshotted_data)



Create a new file system.

### Example 
```python
from purity_fb import PurityFb, FileSystem, Reference, NfsRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with given name, provisioned size, default quotas,
    # and NFSv4.1 enabled.
    default_user_space_quota = 1024000
    default_group_space_quota = 1024000000
    myfs = FileSystem(name="myfs", provisioned=5000, hard_limit_enabled=True,
                      nfs=NfsRule(v4_1_enabled=True),
                      default_user_quota=default_user_space_quota,
                      default_group_quota=default_group_space_quota)
    try:
        # post the file system object myfs on the array with the specific default user and group
        # quotas
        res = fb.file_systems.create_file_systems(file_system=myfs)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system: %s\n" % e)

    # copy snapshot 'myfs.mysnap' to file system 'myfs'
    myfs = FileSystem(name="myfs", source=Reference(name='myfs.mysnap'))
    try:
        # post the file system object myfs on the array
        res = fb.file_systems.create_file_systems(overwrite=True, discard_non_snapshotted_data=True, file_system=myfs)
        print(res)
    except rest.ApiException as e:
        print("Exception when restoring file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system** | [**FileSystem**](FileSystem.md)| The attribute map used to create the file system. | 
 **overwrite** | **bool**| Should we overwrites an existing file system? True if so. | [optional] 
 **discard_non_snapshotted_data** | **bool**| discard (true) the non-snapshotted data. | [optional] 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_filesystem_policies**
> PolicyMemberResponse create_filesystem_policies(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Create a connection between a file system and a policy.

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
        # assume we have a policy named "p1", and a file system with id
        # "100abf42-0000-4000-8023-000det400090"
        res = fb.file_systems.create_filesystem_policies(policy_names=["p1"],
                                                         member_ids=["100abf42-0000-4000-8023-000det400090"])
        print(res)
    except rest.ApiException as e:
        print("Exception when attaching policy to a file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 

### Return type

[**PolicyMemberResponse**](PolicyMemberResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_systems**
> delete_file_systems(ids=ids, name=name)



Delete a file system.

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
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **name** | **str**| The name of the file system or snapshot to be updated. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_filesystem_policies**
> delete_filesystem_policies(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Delete a connection between a file system and a policy.

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
        print("Exception when deleting policy against a file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems**
> FileSystemResponse list_file_systems(ids=ids, names=names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)



List file systems.

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
        print(res)
        # list first five filesystems and sort by provisioned in descendant order
        res = fb.file_systems.list_file_systems(limit=5, sort="provisioned-")
        print(res)
        # list all remaining file systems
        res = fb.file_systems.list_file_systems(token=res.pagination_info.continuation_token)
        # list with filter to see only file systems with at least one type of nfs enabled
        res = fb.file_systems.list_file_systems(filter='nfs.v3_enabled or nfs.v4_1_enabled')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems_performance**
> FileSystemPerformanceResponse list_file_systems_performance(resolution=resolution, protocol=protocol, end_time=end_time, filter=filter, ids=ids, limit=limit, names=names, sort=sort, start_time=start_time, start=start, token=token, total_only=total_only)



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

        # list instantaneous nfs performance for file system with id '10314f42-020d-7080-8013-000ddt400090'
        res = fb.file_systems.list_file_systems_performance(names=['10314f42-020d-7080-8013-000ddt400090'],
                                                            protocol='nfs')
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

[**FileSystemPerformanceResponse**](FileSystemPerformanceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_filesystem_policies**
> PolicyMemberResponse list_filesystem_policies(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policies attached to filesystems.

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
        print("Exception when listing file system policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**PolicyMemberResponse**](PolicyMemberResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_systems**
> FileSystemResponse update_file_systems(attributes, ids=ids, name=name, discard_detailed_permissions=discard_detailed_permissions, discard_non_snapshotted_data=discard_non_snapshotted_data, delete_link_on_eradication=delete_link_on_eradication, ignore_usage=ignore_usage)



Update an existing file system.

### Example 
```python
from purity_fb import PurityFb, FileSystemPatch, MultiProtocolRule, NfsRulePatch, ProtocolRule, SmbRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # update a file system object with a new provisioned size. enable hard limits.
    # enable NFSv4.1, and disable NFSv3. enable SMB in native ACL mode. disable HTTP
    # adjust the default user quota to a new value
    # note that name field should be None
    new_attr = FileSystemPatch(provisioned=1024, hard_limit_enabled=True,
                               nfs=NfsRulePatch(v3_enabled=False,
                                                v4_1_enabled=True,
                                                add_rules="1.1.1.1(rw,no_root_squash)"),
                               http=ProtocolRule(enabled=False),
                               smb=SmbRule(enabled=True, acl_mode="native"),
                               default_user_quota=4096,
                               multi_protocol=MultiProtocolRule(safeguard_acls=False,
                                                                access_control_style="independent"))
    try:
        # update the file system named myfs on the array
        res = fb.file_systems.update_file_systems(name="myfs", ignore_usage=True,
                                                  discard_detailed_permissions=True,
                                                  attributes=new_attr)
        print(res)

        # update the file system with id '10314f42-020d-7080-8013-000ddt400090' on the array
        res = fb.file_systems.update_file_systems(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                  ignore_usage=True, attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attributes** | [**FileSystemPatch**](FileSystemPatch.md)| The new attributes, only modifiable fields may be specified. | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **name** | **str**| The name of the file system or snapshot to be updated. | [optional] 
 **discard_detailed_permissions** | **bool**| This parameter must be set to &#x60;true&#x60; in order to change a file system&#39;s &#x60;access_control_style&#x60; from a style that supports more detailed access control lists to a style that only supports less detailed mode bits as a form of permission control. This parameter may not be set to &#x60;true&#x60; any other time. Setting this parameter to &#x60;true&#x60; is acknowledgement that any more detailed access control lists currently set within the file system will be lost, and NFS permission controls will only be enforced at the granularity level of NFS mode bits. | [optional] 
 **discard_non_snapshotted_data** | **bool**| This parameter must be set to &#x60;true&#x60; in order to restore a file system from a snapshot or to demote a file system (which restores the file system from the common baseline snapshot). Setting this parameter to &#x60;true&#x60; is acknowledgement that any non-snapshotted data currently in the file system will be irretrievably lost. | [optional] 
 **delete_link_on_eradication** | **bool**| If set to &#x60;true&#x60;, the file system can be destroyed, even if it has a replica link. If set to &#x60;false&#x60;, the file system cannot be destroyed if it has a replica link. Defaults to &#x60;false&#x60;. | [optional] 
 **ignore_usage** | **bool**| Allow update operations that lead to a hard_limit_enabled file system with usage over its provisioned size. The update can be either setting hard_limit_enabled when usage is higher than provisioned size, or resize provisioned size to a value under usage when hard_limit_enabled is True. | [optional] 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

