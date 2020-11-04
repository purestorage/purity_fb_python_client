# purity_fb_1dot11.UsageUsersApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_user_usage**](UsageUsersApi.md#list_user_usage) | **GET** /1.11/usage/users | 


# **list_user_usage**
> QuotasUserResponse list_user_usage(names=names, filter=filter, limit=limit, sort=sort, start=start, token=token, file_system_names=file_system_names, uids=uids)



A list of usage user entries

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
    try:
        # Create a file system named usageFs
        file_system_name = "usageFs"
        usageFs = FileSystem(name=file_system_name)
        # post the file system object usageFs on the array
        res = fb.file_systems.create_file_systems(file_system=usageFs)

        # List usage for all users who have space used on usageFs
        res = fb.usage_users.list_user_usage(file_system_names=[file_system_name])
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or listing user usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 
 **file_system_names** | **list[str]**| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **uids** | **list[str]**| A comma-separated list of user IDs. If after filtering, there is not at least one resource that matches each of the elements of user IDs, then an error is returned. This cannot be provided together with user_names query parameter. | [optional] 

### Return type

[**QuotasUserResponse**](QuotasUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

