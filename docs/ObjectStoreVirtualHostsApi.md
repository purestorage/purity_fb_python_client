# purity_fb_1dot12.ObjectStoreVirtualHostsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_store_virtual_hosts**](ObjectStoreVirtualHostsApi.md#create_object_store_virtual_hosts) | **POST** /1.12/object-store-virtual-hosts | 
[**delete_object_store_virtual_hosts**](ObjectStoreVirtualHostsApi.md#delete_object_store_virtual_hosts) | **DELETE** /1.12/object-store-virtual-hosts | 
[**list_object_store_virtual_hosts**](ObjectStoreVirtualHostsApi.md#list_object_store_virtual_hosts) | **GET** /1.12/object-store-virtual-hosts | 


# **create_object_store_virtual_hosts**
> ObjectStoreVirtualHostResponse create_object_store_virtual_hosts(names=names)



Create a new object store virtual host.

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
        # post the object store virtual host on the array
        res = fb.object_store_virtual_hosts.create_object_store_virtual_hosts(names=["s3.myhost.com"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating object store virtual host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**ObjectStoreVirtualHostResponse**](ObjectStoreVirtualHostResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_object_store_virtual_hosts**
> delete_object_store_virtual_hosts(ids=ids, names=names)



Delete an object store virtual host.

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
        # delete the object store virtual host on the array
        res = fb.object_store_virtual_hosts.delete_object_store_virtual_hosts(names=["s3.myhost.com"])
        # delete by id
        res = fb.object_store_virtual_hosts.delete_object_store_virtual_hosts(ids=['10314f42-020d-7080-8013-000ddt400090'])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting object store virtual host: %s\n" % e)
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

# **list_object_store_virtual_hosts**
> ObjectStoreVirtualHostResponse list_object_store_virtual_hosts(filter=filter, ids=ids, names=names, limit=limit, sort=sort, start=start, token=token)



List object store virtual hosts.

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
        # list all object store virtual hosts
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts()
        # list and sort by created in descendant order
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts(limit=3, sort="name-")
        # list with page size 3
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts(limit=3)
        # list with filter
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts(filter='name=\'s3.myhost*\'')
        # list by name
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts(names=['s3.myhost*'])
        # list by id
        res = fb.object_store_virtual_hosts.list_object_store_virtual_hosts(ids=['10314f42-020d-7080-8013-000ddt400090'])

        print(res)
    except rest.ApiException as e:
        print("Exception when listing object store virtual host: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**ObjectStoreVirtualHostResponse**](ObjectStoreVirtualHostResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

