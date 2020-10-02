# purity_fb_1dot10.ObjectStoreRemoteCredentialsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_object_store_remote_credentials**](ObjectStoreRemoteCredentialsApi.md#create_object_store_remote_credentials) | **POST** /1.10/object-store-remote-credentials | 
[**delete_object_store_remote_credentials**](ObjectStoreRemoteCredentialsApi.md#delete_object_store_remote_credentials) | **DELETE** /1.10/object-store-remote-credentials | 
[**list_object_store_remote_credentials**](ObjectStoreRemoteCredentialsApi.md#list_object_store_remote_credentials) | **GET** /1.10/object-store-remote-credentials | 
[**update_object_store_remote_credentials**](ObjectStoreRemoteCredentialsApi.md#update_object_store_remote_credentials) | **PATCH** /1.10/object-store-remote-credentials | 


# **create_object_store_remote_credentials**
> ObjectStoreRemoteCredentialsResponse create_object_store_remote_credentials(remote_credentials, names=names)



Create a new object store remote credentials object.

### Example 
```python
from purity_fb import PurityFb, ObjectStoreRemoteCredentials, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a remote credentials object corresponding to user credentials on the remote
    name = "remote/credentials"
    access_key = "PSFBIKZFCAAAKOEJ"
    secret_key = "0BEC00003+b1228C223c0FbF1ab5e4GICJGBPJPEOLJCD"
    remote_credentials = ObjectStoreRemoteCredentials(access_key_id=access_key, secret_access_key=secret_key)
    try:
        # post the remote credentials object on the local array
        res = fb.object_store_remote_credentials.create_object_store_remote_credentials(names=[name], remote_credentials=remote_credentials)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating remote credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_credentials** | [**ObjectStoreRemoteCredentials**](ObjectStoreRemoteCredentials.md)| The attribute map used to create the object store remote credentials object. | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**ObjectStoreRemoteCredentialsResponse**](ObjectStoreRemoteCredentialsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_object_store_remote_credentials**
> delete_object_store_remote_credentials(ids=ids, names=names)



Delete an object store remote credentials object.

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
        # delete the remote credentials with the name 'remote/credentials'
        fb.object_store_remote_credentials.delete_object_store_remote_credentials(names=['remote/credentials'])

        # delete the remote credentials with the id '10314f42-020d-7080-8013-000ddt400090'
        fb.object_store_remote_credentials.delete_object_store_remote_credentials(ids=['10314f42-020d-7080-8013-000ddt400090'])
    except rest.ApiException as e:
        print("Exception when deleting remote credentials: %s\n" % e)
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

# **list_object_store_remote_credentials**
> ObjectStoreRemoteCredentialsResponse list_object_store_remote_credentials(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List object store remote credentials.

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
        # list all remote credentials
        fb.object_store_remote_credentials.list_object_store_remote_credentials()
        # list first five remote credentials using default sort
        res = fb.object_store_remote_credentials.list_object_store_remote_credentials(limit=5)
        print(res)
        # list first five remote credentials and sort by access key
        res = fb.object_store_remote_credentials.list_object_store_remote_credentials(limit=5, sort='access_key_id')
        print(res)
        # list all remaining remote credentials
        res = fb.object_store_remote_credentials.list_object_store_remote_credentials(token=res.pagination_info.continuation_token)
        print(res)
        # list with filter to see only remote credentials that are on a specific remote
        res = fb.object_store_remote_credentials.list_object_store_remote_credentials(filter='name=\'s3target/*\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing remote credentials: %s\n" % e)
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

[**ObjectStoreRemoteCredentialsResponse**](ObjectStoreRemoteCredentialsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_object_store_remote_credentials**
> ObjectStoreRemoteCredentialsResponse update_object_store_remote_credentials(remote_credentials, ids=ids, names=names)



Update an existing object store remote credentials object.

### Example 
```python
from purity_fb import PurityFb, ObjectStoreRemoteCredentials, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # Change the name of an existing set of remote credentials to "remote/credentials2"
    # Change the access key id of an existing set of remote credentials
    # Change the secret access key of an existing set of remote credentials
    new_attr = ObjectStoreRemoteCredentials(name='remote/credentials2',
                                            access_key_id='PSFBIKZFCAAAKOEJ',
                                            secret_access_key='0BEC00003+b1228C223c0FbF1ab5e4GICJGBPJPEOLJCD')
    try:
        # update the the remote credentials with the name 'remote/credentials1' with our new attributes
        res = fb.object_store_remote_credentials.update_object_store_remote_credentials(names=['remote/credentials1'],
                                                                                        remote_credentials=new_attr)
        print(res)

        # update the the remote credentials with the id '10314f42-020d-7080-8013-000ddt400090' with our new attributes
        res = fb.object_store_remote_credentials.update_object_store_remote_credentials(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                                                        remote_credentials=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating remote credentials: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_credentials** | [**ObjectStoreRemoteCredentials**](ObjectStoreRemoteCredentials.md)| The attribute map used to update the object store remote credentials object. | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**ObjectStoreRemoteCredentialsResponse**](ObjectStoreRemoteCredentialsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

