# purity_fb_1dot7.QuotasGroupsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group_quotas**](QuotasGroupsApi.md#create_group_quotas) | **POST** /1.7/quotas/groups | 
[**delete_group_quotas**](QuotasGroupsApi.md#delete_group_quotas) | **DELETE** /1.7/quotas/groups | 
[**list_group_quotas**](QuotasGroupsApi.md#list_group_quotas) | **GET** /1.7/quotas/groups | 
[**update_group_quotas**](QuotasGroupsApi.md#update_group_quotas) | **PATCH** /1.7/quotas/groups | 


# **create_group_quotas**
> QuotasGroupResponse create_group_quotas(file_system_names=file_system_names, gids=gids, group_names=group_names, quota=quota)



Create a new group quota

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasGroup, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Create a file system
        file_system_name = "quotaFs"
        quotaFs = FileSystem(name=file_system_name)
        # post the file system object quotaFs on the array
        res = fb.file_systems.create_file_systems(file_system=quotaFs)

        # Add a quota of 1024000 for the file system to apply to the groups with ids 998 and 999
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name], gids=[998, 999],
                                                   quota=QuotasGroup(quota=1024000))
        # print the created quotas
        print(res.items)

        # Add a quota of 2048000 for the file system to apply to the groups with names group1 and group2
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name],
                                                   group_names=["group1", "group2"],
                                                   quota=QuotasGroup(quota=2048000))
        # print the created quotas
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or creating group quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **gids** | [**list[str]**](str.md)| A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter. | [optional] 
 **group_names** | [**list[str]**](str.md)| A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter. | [optional] 
 **quota** | [**QuotasGroup**](QuotasGroup.md)|  | [optional] 

### Return type

[**QuotasGroupResponse**](QuotasGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_group_quotas**
> delete_group_quotas(names=names, file_system_names=file_system_names, gids=gids, group_names=group_names)



Delete

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasGroup, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Assume you have a file system named quotaFs
        file_system_name = "quotaFs"
        quotaFs = FileSystem(name=file_system_name)

        # Delete the quotas of groups on the file system with ids 998 and 999
        fb.quotas_groups.delete_group_quotas(file_system_names=[file_system_name], gids=[998, 999])
        # Delete the quotas of groups on the file system with names group1 and group2
        fb.quotas_groups.delete_group_quotas(file_system_names=[file_system_name],
                                             group_names=["group1", "group2"])
    except rest.ApiException as e:
        print("Exception when deleting user quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **gids** | [**list[str]**](str.md)| A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter. | [optional] 
 **group_names** | [**list[str]**](str.md)| A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_group_quotas**
> QuotasGroupResponse list_group_quotas(names=names, filter=filter, limit=limit, sort=sort, start=start, token=token, file_system_names=file_system_names, gids=gids, group_names=group_names)



A list of quota group entries

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasGroup, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Create a file system
        file_system_name = "quotaFs"
        quotaFs = FileSystem(name=file_system_name)
        # post the file system object quotaFs on the array
        res = fb.file_systems.create_file_systems(file_system=quotaFs)

        # Add a quota of 1024000 for the file system to apply to the groups with ids 998 and 999
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name], gids=[998, 999],
                                                   quota=QuotasGroup(quota=1024000))

        # Add a quota of 2048000 for the file system to apply to the groups with names group1 and group2
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name],
                                                   group_names=["group1", "group2"],
                                                   quota=QuotasGroup(quota=2048000))

        # List all group quotas for the file system
        res = fb.quotas_groups.list_group_quotas(file_system_names=[file_system_name])
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or listing group quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
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

# **update_group_quotas**
> QuotasGroupResponse update_group_quotas(names=names, file_system_names=file_system_names, gids=gids, group_names=group_names, quota=quota)



Update existing group quotas

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasGroup, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Create a file system named quotaFs
        file_system_name = "quotaFs"
        quotaFs = FileSystem(name=file_system_name)
        # post the file system object quotaFs on the array
        res = fb.file_systems.create_file_systems(file_system=quotaFs)

        # Add a quota of 1024000 for the file system to apply to the groups with ids 998 and 999
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name],
                                                   gids=[998, 999],
                                                   quota=QuotasGroup(quota=1024000))
        # print the created quotas
        print(res.items)
        # Update the quota for the groups with with ids 998 and 999 to be 2048000
        res = fb.quotas_groups.update_group_quotas(file_system_names=[file_system_name],
                                                   gids=[998, 999],
                                                   quota=QuotasGroup(quota=2048000))
        # print the created quotas
        print(res.items)

        # Add a quota of 2048000 for the file system to apply to the groups with names group1 and group2
        res = fb.quotas_groups.create_group_quotas(file_system_names=[file_system_name],
                                                   group_names=["group1", "group2"],
                                                   quota=QuotasGroup(quota=2048000))
        # print the created quotas
        print(res.items)
        # Update the quota for the groups with names group1 and group2 to be 1024000
        res = fb.quotas_groups.update_group_quotas(file_system_names=[file_system_name],
                                                   group_names=["group1", "group2"],
                                                   quota=QuotasGroup(quota=1024000))
        # print the updated quotas
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or updating group quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **gids** | [**list[str]**](str.md)| A comma-separated list of group IDs. If after filtering, there is not at least one resource that matches each of the elements of group IDs, then an error is returned. This cannot be provided together with group_names query parameter. | [optional] 
 **group_names** | [**list[str]**](str.md)| A comma-separated list of group names. If after filtering, there is not at least one resource that matches each of the elements of group names, then an error is returned. This cannot be provided together with gids query parameter. | [optional] 
 **quota** | [**QuotasGroup**](QuotasGroup.md)|  | [optional] 

### Return type

[**QuotasGroupResponse**](QuotasGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

