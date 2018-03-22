# purity_fb.ObjectStoreUsersApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_store_users**](ObjectStoreUsersApi.md#create_object_store_users) | **POST** /1.3/object-store-users | 
[**delete_object_store_users**](ObjectStoreUsersApi.md#delete_object_store_users) | **DELETE** /1.3/object-store-users | 
[**list_object_store_users**](ObjectStoreUsersApi.md#list_object_store_users) | **GET** /1.3/object-store-users | 


# **create_object_store_users**
> ObjectStoreUserResponse create_object_store_users(names=names)



Create a new object store user

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
        # post the object store user object myobjuser on the array
        res = fb.object_store_users.create_object_store_users(names=["myobjuser"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**ObjectStoreUserResponse**](ObjectStoreUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_object_store_users**
> delete_object_store_users(names=names)



Delete an object store user by name

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
        # delete a object store user with name myobjuser
        fb.object_store_users.delete_object_store_users(names=["myobjuser"])
    except rest.ApiException as e:
        print("Exception when deleting object store user: %s\n" % e)
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

# **list_object_store_users**
> ObjectStoreUserResponse list_object_store_users(filter=filter, sort=sort, start=start, limit=limit, token=token, names=names)



List object store users

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
        # list all object store users
        res = fb.object_store_users.list_object_store_users()
        # list and sort by created in descendant order
        res = fb.object_store_users.list_object_store_users(limit=5, sort="created-")
        # list with page size 5
        res = fb.object_store_users.list_object_store_users(limit=5)
        # list all remaining object store users
        res = fb.object_store_users.list_object_store_users(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.object_store_users.list_object_store_users(filter='name=\'myobjuser*\'')
    except rest.ApiException as e:
        print("Exception when listing object store users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**ObjectStoreUserResponse**](ObjectStoreUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

