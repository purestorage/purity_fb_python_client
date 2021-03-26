# purity_fb_1dot12.ObjectStoreAccessPoliciesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_object_store_access_policies_object_store_users**](ObjectStoreAccessPoliciesApi.md#add_object_store_access_policies_object_store_users) | **POST** /1.12/object-store-access-policies/object-store-users | 
[**list_object_store_access_policies**](ObjectStoreAccessPoliciesApi.md#list_object_store_access_policies) | **GET** /1.12/object-store-access-policies | 
[**list_object_store_access_policies_object_store_users**](ObjectStoreAccessPoliciesApi.md#list_object_store_access_policies_object_store_users) | **GET** /1.12/object-store-access-policies/object-store-users | 
[**remove_object_store_access_policies_object_store_users**](ObjectStoreAccessPoliciesApi.md#remove_object_store_access_policies_object_store_users) | **DELETE** /1.12/object-store-access-policies/object-store-users | 


# **add_object_store_access_policies_object_store_users**
> ObjectStoreAccessPolicyObjectStoreUserResponse add_object_store_access_policies_object_store_users(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Add a policy to an object store user.

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
        # add a member to a policy
        res = fb.object_store_access_policies.add_object_store_access_policies_object_store_users(
            member_names=["acc1/myobjuser"], policy_names=["pure:policy/bucket-list"])
        print(res)
    except rest.ApiException as e:
        print("Exception when adding a member to a policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 

### Return type

[**ObjectStoreAccessPolicyObjectStoreUserResponse**](ObjectStoreAccessPolicyObjectStoreUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_object_store_access_policies**
> ObjectStoreAccessPolicyResponse list_object_store_access_policies(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List object store access policies.

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
        # list all object store access policies
        res = fb.object_store_access_policies.list_object_store_access_policies()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing object store access policies: %s\n" % e)
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

[**ObjectStoreAccessPolicyResponse**](ObjectStoreAccessPolicyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_object_store_access_policies_object_store_users**
> ObjectStoreAccessPolicyObjectStoreUserResponse list_object_store_access_policies_object_store_users(filter=filter, limit=limit, policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names, sort=sort, start=start, token=token)



List object store access policies for object store users.

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
        # list access policies for object store users
        res = fb.object_store_access_policies.list_object_store_access_policies_object_store_users()
        print(res)

        # list access policies for specific user
        res = fb.object_store_access_policies.list_object_store_access_policies_object_store_users(
            member_names=["acc1/myobjuser"])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing users for object store access policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **policy_ids** | **list[str]**| A comma-separated list of policy IDs. This cannot be provided together with the policy names query parameters. | [optional] 
 **policy_names** | **list[str]**| A comma-separated list of policy names. This cannot be provided together with the policy ids query parameters. | [optional] 
 **member_ids** | **list[str]**| A comma-separated list of member ids. This cannot be provided together with the member names query parameters. | [optional] 
 **member_names** | **list[str]**| A comma-separated list of member names. This cannot be provided together with the member ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**ObjectStoreAccessPolicyObjectStoreUserResponse**](ObjectStoreAccessPolicyObjectStoreUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **remove_object_store_access_policies_object_store_users**
> remove_object_store_access_policies_object_store_users(policy_ids=policy_ids, policy_names=policy_names, member_ids=member_ids, member_names=member_names)



Remove a policy from an object store user.

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
        # remove a member from a policy
        res = fb.object_store_access_policies.remove_object_store_access_policies_object_store_users(
            member_names=["acc1/myobjuser"], policy_names=["pure:policy/bucket-list"])
        print(res)
    except rest.ApiException as e:
        print("Exception when removing member from policy: %s\n" % e)
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

