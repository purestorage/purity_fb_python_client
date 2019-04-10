# purity_fb_1dot7.PoliciesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policies**](PoliciesApi.md#create_policies) | **POST** /1.7/policies | 
[**create_policy_filesystems**](PoliciesApi.md#create_policy_filesystems) | **POST** /1.7/policies/file-systems | 
[**delete_policies**](PoliciesApi.md#delete_policies) | **DELETE** /1.7/policies | 
[**delete_policy_filesystems**](PoliciesApi.md#delete_policy_filesystems) | **DELETE** /1.7/policies/file-systems | 
[**list_policies**](PoliciesApi.md#list_policies) | **GET** /1.7/policies | 
[**list_policy_filesystem_snapshots**](PoliciesApi.md#list_policy_filesystem_snapshots) | **GET** /1.7/policies/file-system-snapshots | 
[**list_policy_filesystems**](PoliciesApi.md#list_policy_filesystems) | **GET** /1.7/policies/file-systems | 
[**list_policy_members**](PoliciesApi.md#list_policy_members) | **GET** /1.7/policies/members | 
[**update_policies**](PoliciesApi.md#update_policies) | **PATCH** /1.7/policies | 


# **create_policies**
> PolicyResponse create_policies(policy, names=names)



Create a new policy

### Example 
```python
from purity_fb import PurityFb, rest, Policy

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post a policy object p1 on the array
        attr = Policy()
        res = fb.policies.create_policies(names=["p1"], policy=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy** | [**Policy**](Policy.md)| The attribute map used to create the policy | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_policy_filesystems**
> PolicyObjectsResponse create_policy_filesystems(policy_names=policy_names, member_names=member_names)



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
        res = fb.policies.create_policy_filesystems(policy_names=["p1"],
                                                    member_names=["myfs"])
        print(res)
    except rest.ApiException as e:
        print("Exception when attaching policy to a file system: %s\n" % e)
```

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

# **delete_policies**
> delete_policies(names=names)



Delete a policy by name

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
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_policy_filesystems**
> delete_policy_filesystems(policy_names=policy_names, member_names=member_names)



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
        res = fb.policies.delete_policy_filesystems(policy_names=["p1"],
                                                    member_names=["myfs"])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting policy against a file system: %s\n" % e)
```

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

# **list_policies**
> PolicyResponse list_policies(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policies

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
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_policy_filesystem_snapshots**
> PolicyObjectsResponse list_policy_filesystem_snapshots(policy_names=policy_names, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



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

# **list_policy_filesystems**
> PolicyObjectsResponse list_policy_filesystems(policy_names=policy_names, member_names=member_names, filter=filter, sort=sort, start=start, limit=limit, token=token)



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

# **list_policy_members**
> PolicyObjectsResponse list_policy_members(policy_names=policy_names, member_names=member_names, member_types=member_types, filter=filter, sort=sort, start=start, limit=limit, token=token)



List policy attached to filesystems and filesystem snapshots

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
        res = fb.policies.list_policy_members()
        print(res)
        # assume we have a policy named "p1", and a file system named "myfs"
        res = fb.policies.list_policy_members(policy_names=["p1"],
                                              member_names=["myfs"])
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
 **policy_names** | [**list[str]**](str.md)| A list of policy names. | [optional] 
 **member_names** | [**list[str]**](str.md)| A list of member names. | [optional] 
 **member_types** | [**list[str]**](str.md)| A list of member types. | [optional] 
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

# **update_policies**
> PolicyResponse update_policies(policy_patch, names=names)



Update an existing policy

### Example 
```python
from purity_fb import PurityFb, rest, Policy

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        res = fb.policies.update_policies(
            names=["p1"], policy_patch=Policy(enabled=False))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_patch** | [**PolicyPatch**](PolicyPatch.md)| the attribute map used to update the policy | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**PolicyResponse**](PolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

