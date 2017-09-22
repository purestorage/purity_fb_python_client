# purity_fb.FileSystemSnapshotsBetaApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_system_snapshots**](FileSystemSnapshotsBetaApi.md#delete_file_system_snapshots) | **DELETE** /beta/file-system-snapshots | 


# **delete_file_system_snapshots**
> delete_file_system_snapshots(name)



Delete a file system snapshot by name

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
        # delete a file system snapshot named myfs.mysnap
        fb.file_system_snapshots_beta.delete_file_system_snapshots(name="myfs.mysnap")
    except rest.ApiException as e:
        print("Exception when deleting file system snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system snapshot to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

