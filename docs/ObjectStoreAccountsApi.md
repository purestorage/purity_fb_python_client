# purity_fb.ObjectStoreAccountsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_store_accounts**](ObjectStoreAccountsApi.md#create_object_store_accounts) | **POST** /1.3/object-store-accounts | 
[**delete_object_store_accounts**](ObjectStoreAccountsApi.md#delete_object_store_accounts) | **DELETE** /1.3/object-store-accounts | 
[**list_object_store_accounts**](ObjectStoreAccountsApi.md#list_object_store_accounts) | **GET** /1.3/object-store-accounts | 


# **create_object_store_accounts**
> ObjectStoreAccountResponse create_object_store_accounts(names=names)



Create a new object store account

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
        # post the object store account object myobjaccount on the array
        res = fb.object_store_accounts.create_object_store_accounts(names=["myobjaccount"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**ObjectStoreAccountResponse**](ObjectStoreAccountResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_object_store_accounts**
> delete_object_store_accounts(names=names)



Delete an object store account by name

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
        # delete a object store account with name myobjaccount
        fb.object_store_accounts.delete_object_store_accounts(names=["myobjaccount"])
    except rest.ApiException as e:
        print("Exception when deleting object store account: %s\n" % e)
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

# **list_object_store_accounts**
> ObjectStoreAccountResponse list_object_store_accounts(filter=filter, sort=sort, start=start, limit=limit, token=token, total_only=total_only, names=names)



List object store accounts

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
        # list all object store accounts
        res = fb.object_store_accounts.list_object_store_accounts()
        # list and sort by unique in descendant order
        res = fb.object_store_accounts.list_object_store_accounts(limit=5, sort="space.unique-")
        # list with page size 5
        res = fb.object_store_accounts.list_object_store_accounts(limit=5)
        # list all remaining object store accounts
        res = fb.object_store_accounts.list_object_store_accounts(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.object_store_accounts.list_object_store_accounts(filter='name=\'myobjaccount*\'')
    except rest.ApiException as e:
        print("Exception when listing object store accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total_only** | **bool**| return only the total object | [optional] [default to false]
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**ObjectStoreAccountResponse**](ObjectStoreAccountResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

