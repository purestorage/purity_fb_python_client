# purity_fb_1dot5.ObjectStoreAccessKeysApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_store_access_keys**](ObjectStoreAccessKeysApi.md#create_object_store_access_keys) | **POST** /1.5/object-store-access-keys | 
[**delete_object_store_access_keys**](ObjectStoreAccessKeysApi.md#delete_object_store_access_keys) | **DELETE** /1.5/object-store-access-keys | 
[**list_object_store_access_keys**](ObjectStoreAccessKeysApi.md#list_object_store_access_keys) | **GET** /1.5/object-store-access-keys | 
[**update_object_store_access_keys**](ObjectStoreAccessKeysApi.md#update_object_store_access_keys) | **PATCH** /1.5/object-store-access-keys | 


# **create_object_store_access_keys**
> ObjectStoreAccessKeyResponse create_object_store_access_keys(object_store_access_key=object_store_access_key)



Create a new object store access key

### Example 
```python
from purity_fb import PurityFb, rest, ObjectStoreAccessKey

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # generate access key and secret key for object store user
        # note: you need to handle the secret key since you can't retrieve it from the array after create
        res = fb.object_store_access_keys.create_object_store_access_keys(
            object_store_access_key=ObjectStoreAccessKey(user={'name': 'myobjuser'}))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store access key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **object_store_access_key** | [**Objectstoreaccesskey**](Objectstoreaccesskey.md)| The attribute map used to create the object store access key | [optional] 

### Return type

[**ObjectStoreAccessKeyResponse**](ObjectStoreAccessKeyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_object_store_access_keys**
> delete_object_store_access_keys(names=names)



Delete an object store access key by name

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
        # delete an access key with name myobjaccesskey
        fb.object_store_access_keys.delete_object_store_access_keys(names=["myobjaccesskey"])
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

# **list_object_store_access_keys**
> ObjectStoreAccessKeyResponse list_object_store_access_keys(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List object store access keys

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
        # list all object store access keys
        res = fb.object_store_access_keys.list_object_store_access_keys()
        # list and sort by created in descendant order
        res = fb.object_store_access_keys.list_object_store_access_keys(limit=5, sort="created-")
        # list with page size 5
        res = fb.object_store_access_keys.list_object_store_access_keys(limit=5)
        # list all remaining object store access keys
        res = fb.object_store_access_keys.list_object_store_access_keys(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.object_store_access_keys.list_object_store_access_keys(filter='user.name=\'myobjuser\'')
    except rest.ApiException as e:
        print("Exception when listing object store access keys: %s\n" % e)
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

[**ObjectStoreAccessKeyResponse**](ObjectStoreAccessKeyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_object_store_access_keys**
> ObjectStoreAccessKeyResponse update_object_store_access_keys(names=names, object_store_access_key=object_store_access_key)



Update an existing object store access key

### Example 
```python
from purity_fb import PurityFb, rest, ObjectStoreAccessKey

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        res = fb.object_store_access_keys.update_object_store_access_keys(
            names=['myobjaccesskey'], object_store_access_key=ObjectStoreAccessKey(enabled=False))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating object store access key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **object_store_access_key** | [**ObjectStoreAccessKey**](ObjectStoreAccessKey.md)| the attribute map used to update the object store access key | [optional] 

### Return type

[**ObjectStoreAccessKeyResponse**](ObjectStoreAccessKeyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

