# purity_fb.FileSystemsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_systems**](FileSystemsApi.md#create_file_systems) | **POST** /1.3/file-systems | 
[**delete_file_systems**](FileSystemsApi.md#delete_file_systems) | **DELETE** /1.3/file-systems | 
[**list_file_systems**](FileSystemsApi.md#list_file_systems) | **GET** /1.3/file-systems | 
[**update_file_systems**](FileSystemsApi.md#update_file_systems) | **PATCH** /1.3/file-systems | 


# **create_file_systems**
> FileSystemResponse create_file_systems(file_system)



Create a new file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, NfsRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with given name, provisioned size, and NFS enabled.
    myfs = FileSystem(name="myfs", provisioned="5000", nfs=NfsRule(enabled=True))
    try:
        # post the file system object myfs on the array
        res = fb.file_systems.create_file_systems(file_system=myfs)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system** | [**FileSystem**](FileSystem.md)| the attribute map used to create the file system | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_systems**
> delete_file_systems(name)



Delete a file system by name

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
        # delete a file system with name myfs
        fb.file_systems.delete_file_systems(name="myfs")
    except rest.ApiException as e:
        print("Exception when deleting file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems**
> FileSystemResponse list_file_systems(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)



List file systems

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException sources=as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all file systems
        fb.file_systems.list_file_systems()
        # list and sort by provisioned in descendant order
        res = fb.file_systems.list_file_systems(limit=5, sort="provisioned-")
        # list with page size 5
        res = fb.file_systems.list_file_systems(limit=5)
        # list all remaining file systems
        res = fb.file_systems.list_file_systems(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.file_systems.list_file_systems(filter='name=\'myfs*\' and nfs.enabled and not(smb.enabled)')
    except rest.ApiException as e:
        print("Exception when listing file systems: %s\n" % e)
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
 **total** | **bool**| return a total object in addition to the other results | [optional] [default to false]
 **total_only** | **bool**| return only the total object | [optional] [default to false]

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_systems**
> FileSystemResponse update_file_systems(name, attributes)



Update an existing file system

### Example 
```python
from purity_fb import PurityFb, FileSystem, NfsRule, ProtocolRule, SmbRule, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a local file system object with provisioned size, and NFS enabled
    # note that name field should be None
    new_attr = FileSystem(provisioned="1024", nfs=NfsRule(enabled=True), http=ProtocolRule(enabled=False), smb=SmbRule(enabled=True, acl_mode="native"))
    try:
        # update the file system named myfs on the array
        res = fb.file_systems.update_file_systems(name="myfs", attributes=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating file system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the file system to be updated | 
 **attributes** | [**FileSystem**](FileSystem.md)| the new attributes, only modifiable fields could be used. | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

