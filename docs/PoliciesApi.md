# purity_fb_1dot10.PoliciesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policies**](PoliciesApi.md#create_policies) | **POST** /1.10/policies | 
[**create_policy_file_system_replica_links**](PoliciesApi.md#create_policy_file_system_replica_links) | **POST** /1.10/policies/file-system-replica-links | 
[**create_policy_filesystems**](PoliciesApi.md#create_policy_filesystems) | **POST** /1.10/policies/file-systems | 
[**delete_policies**](PoliciesApi.md#delete_policies) | **DELETE** /1.10/policies | 
[**delete_policy_file_system_replica_links**](PoliciesApi.md#delete_policy_file_system_replica_links) | **DELETE** /1.10/policies/file-system-replica-links | 
[**delete_policy_filesystem_snapshots**](PoliciesApi.md#delete_policy_filesystem_snapshots) | **DELETE** /1.10/policies/file-system-snapshots | 
[**delete_policy_filesystems**](PoliciesApi.md#delete_policy_filesystems) | **DELETE** /1.10/policies/file-systems | 
[**list_policies**](PoliciesApi.md#list_policies) | **GET** /1.10/policies | 
[**list_policy_file_system_replica_links**](PoliciesApi.md#list_policy_file_system_replica_links) | **GET** /1.10/policies/file-system-replica-links | 
[**list_policy_filesystem_snapshots**](PoliciesApi.md#list_policy_filesystem_snapshots) | **GET** /1.10/policies/file-system-snapshots | 
[**list_policy_filesystems**](PoliciesApi.md#list_policy_filesystems) | **GET** /1.10/policies/file-systems | 
[**list_policy_members**](PoliciesApi.md#list_policy_members) | **GET** /1.10/policies/members | 
[**update_policies**](PoliciesApi.md#update_policies) | **PATCH** /1.10/policies | 


# **create_policies**
> PolicyResponse create_policies(policy, names=names)



Create a new policy.

### Example 
```python
from purity_fb import PurityFb, rest, Policy, PolicyRule

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post a policy object p1 on the array
        attr = Policy(enabled=True,
                      rules=[
                          # Take a snapshot every 5m and keep for 1h
                          PolicyRule(every=1000*60*5, keep_for=1000*60*60)
                      ])
        res = fb.policies.create_policies(names=["p1"], policy=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)| The attribute map used to create the policy. | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_policy_file_system_replica_links**
> PolicyMemberWithRemoteResponse create_policy_file_system_replica_links(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names)



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
        res = fb.policies.create_policy_filesystem_replica_links(
                policy_names=['policy_1'],
                local_file_system_names=['local_fs'],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when adding file system replica link to policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_names** | **list[str]**| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | **list[str]**| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

[**PolicyMemberWithRemoteResponse**](PolicyMemberWithRemoteResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_policy_filesystems**
> PolicyMemberResponse create_policy_filesystems(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



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
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.policies.create_policy_filesystems(policy_names=["p1"],
                                                    member_names=["myfs"])
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

# **delete_policies**
> delete_policies(ids=ids, names=names)



Delete a policy.

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
        # delete a policy name p1
        res = fb.policies.delete_policies(names=["p1"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating policy: %s\n" % e)
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

# **delete_policy_file_system_replica_links**
> delete_policy_file_system_replica_links(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names)



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
        res = fb.policies.delete_policy_filesystem_replica_links(
                policy_names=['policy_1'],
                member_names=['local_fs'],
                remote_names=[REMOTE_ARRAY])
        print(res)
    except rest.ApiException as e:
        print("Exception when adding file system replica link to policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_file_system_names** | **list[str]**| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | **list[str]**| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_policy_filesystem_snapshots**
> delete_policy_filesystem_snapshots(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Delete a connection betwwen a file system snapshot and a policy.

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
        # attach policy to a file system snapshot
        # assume we have a policy named "p1", and a file system snapshot named "myfs.suffix"
        res = fb.policies.delete_policy_filesystem_snapshots(policy_names=["p1"],
                                                    member_names=["myfs.suffix"])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting policy against a file system snapshot: %s\n" % e)
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

# **delete_policy_filesystems**
> delete_policy_filesystems(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Delete a connection betwwen a file system and a policy.

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
        res = fb.policies.delete_policy_filesystems(policy_names=["p1"],
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

# **list_policies**
> PolicyResponse list_policies(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List policies.

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
        res = fb.policies.list_policies()
        print(res)
        # list and sort by name in descendant order
        res = fb.policies.list_policies(limit=5, sort="name-")
        print(res)
        # list with page size 5
        res = fb.policies.list_policies(limit=5)
        print(res)
        # list all remaining policies
        res = fb.policies.list_policies(token=res.pagination_info.continuation_token)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing policies: %s\n" % e)
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

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_policy_file_system_replica_links**
> PolicyMemberWithRemoteResponse list_policy_file_system_replica_links(local_file_system_names=local_file_system_names, local_file_system_ids=local_file_system_ids, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, remote_ids=remote_ids, remote_names=remote_names, remote_file_system_names=remote_file_system_names, remote_file_system_ids=remote_file_system_ids, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to file system replica links.

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
        res = fb.policies.list_policy_filesystem_replica_links()
        print(res)
        # list first five replica link and policy connections and sort by policy name
        res = fb.policies.list_policy_filesystem_replica_links(limit=5, sort='policy.name')
        print(res)
        # list remaining replica link and policies connections
        res = fb.policies.list_policy_filesystem_replica_links(
                token=res.pagination_info.continuation_token)
        print(res)
        # list a specific replica link and policy connection
        res = fb.policies.list_policy_filesystem_replica_links(
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
 **local_file_system_names** | **list[str]**| A comma-separated list of local file system names. This cannot be provided together with the &#x60;local_file_system_ids&#x60; query parameter. | [optional] 
 **local_file_system_ids** | **list[str]**| A comma-separated list of local file system IDs. This cannot be provided together with the &#x60;local_file_system_names&#x60; query parameter. | [optional] 
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **remote_file_system_names** | **list[str]**| A comma-separated list of remote file system names. This cannot be provided together with &#x60;remote_file_system_ids&#x60; query parameter. | [optional] 
 **remote_file_system_ids** | **list[str]**| A comma-separated list of remote file system IDs. This cannot be provided together with &#x60;remote_file_system_names&#x60; query parameter. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**PolicyMemberWithRemoteResponse**](PolicyMemberWithRemoteResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_policy_filesystem_snapshots**
> PolicyMemberResponse list_policy_filesystem_snapshots(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



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
        res = fb.policies.list_policy_filesystem_snapshots()
        print(res)
        # assume we have a policy named "p1", and a file system snapshot named "myfs.1"
        res = fb.policies.list_policy_filesystem_snapshots(policy_names=["p1"],
                                                           member_names=["myfs.1"])
        print(res)
        # assume we have a policy with id "10314f42-020d-7080-8013-000ddt400090",
        # and a file system snapshot with name "myfs.2"
        res = fb.policies.list_policy_filesystem_snapshots(policy_ids=["10314f42-020d-7080-8013-000ddt400090"],
                                                           member_names=["myfs.2"])
        print(res)
        # list and sort by name in descendant order
        res = fb.policies.list_policy_filesystem_snapshots(limit=5, sort="policy.name-")
        print(res)
        # list with page size 5
        res = fb.policies.list_policy_filesystem_snapshots(limit=5)
        print(res)
        # list all remaining policies
        if(res.pagination_info.continuation_token != None):
            res = fb.policies.list_policy_filesystem_snapshots(token=res.pagination_info.continuation_token)
            print(res)
    except rest.ApiException as e:
        print("Exception when listing policy file system snapshot: %s\n" % e)
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

# **list_policy_filesystems**
> PolicyMemberResponse list_policy_filesystems(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to filesystems.

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
        res = fb.policies.list_policy_filesystems()
        print(res)
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.policies.list_policy_filesystems(policy_names=["p1"],
                                                  member_names=["myfs"])
        print(res)
        # list and sort by name in descendant order
        res = fb.policies.list_policy_filesystems(limit=5, sort="policy.name-")
        print(res)
        # list with page size 5
        res = fb.policies.list_policy_filesystems(limit=5)
        print(res)
        # list all remaining policies
        res = fb.policies.list_policy_filesystems(token=res.pagination_info.continuation_token)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing policy file system: %s\n" % e)
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

# **list_policy_members**
> PolicyMemberResponse list_policy_members(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, member_types=member_types, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to filesystems and filesystem snapshots.

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
        # list all policies
        res = fb.policies.list_policy_members()
        print(res)
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.policies.list_policy_members(policy_names=["p1"],
                                              member_names=["myfs"])
        print(res)
        res = fb.policies.list_policy_members(policy_names=["p1"],
                                              member_names=["myfs"],
                                              remote_names=[REMOTE_ARRAY])
        print(res)
        # assume we have a policy named "p1", and a file system snapshot named "myfs.1"
        res = fb.policies.list_policy_members(policy_names=["p1"],
                                              member_names=["myfs.1"])
        print(res)
        # list and sort by name in descendant order
        res = fb.policies.list_policy_members(limit=5, sort="policy.name-")
        print(res)
        # list with page size 5
        res = fb.policies.list_policy_members(limit=5)
        print(res)
        # list all remaining policies
        res = fb.policies.list_policy_members(token=res.pagination_info.continuation_token)
        print(res)
    except rest.ApiException as e:
        print("Exception when listing policy members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 
 **member_types** | **list[str]**| A list of member types. | [optional] 
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

# **update_policies**
> PolicyResponse update_policies(policy_patch, names=names)



Update an existing policy.

### Example 
```python
from purity_fb import PurityFb, rest, PolicyPatch

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Update the policy "p1", and set the "enabled" field to "False"
        res = fb.policies.update_policies(
            names=["p1"], policy_patch=PolicyPatch(enabled=False))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_patch** | [**PolicyPatch**](PolicyPatch.md)| The attribute map used to update the policy. | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

