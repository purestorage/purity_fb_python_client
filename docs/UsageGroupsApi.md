# purity_fb_1dot9.UsageGroupsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_group_usage**](UsageGroupsApi.md#list_group_usage) | **GET** /1.9/usage/groups | 


# **list_group_usage**
> QuotasGroupResponse list_group_usage(names=names, filter=filter, limit=limit, sort=sort, start=start, token=token, file_system_names=file_system_names, gids=gids, group_names=group_names)



A list of usage group entries

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

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

        # List usage for all groups that have space used on usageFs
        res = fb.usage_groups.list_group_usage(file_system_names=[file_system_name])
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or listing group usage: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **gids** | [**list[str]**](str.md)| A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter. | [optional] 
 **group_names** | [**list[str]**](str.md)| A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter. | [optional] 

### Return type

[**QuotasGroupResponse**](QuotasGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

