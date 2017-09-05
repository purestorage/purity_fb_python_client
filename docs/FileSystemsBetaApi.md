# purity_fb.FileSystemsBetaApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_systems**](FileSystemsBetaApi.md#delete_file_systems) | **DELETE** /beta/file-systems | 


# **delete_file_systems**
> delete_file_systems(name)



Delete a file system by name

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # delete a file system with name myfs
        fb.file_systems_beta.delete_file_systems(name="myfs")
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

