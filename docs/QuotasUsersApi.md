# purity_fb_1dot7.QuotasUsersApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_quotas**](QuotasUsersApi.md#create_user_quotas) | **POST** /1.7/quotas/users | 
[**delete_user_quotas**](QuotasUsersApi.md#delete_user_quotas) | **DELETE** /1.7/quotas/users | 
[**list_user_quotas**](QuotasUsersApi.md#list_user_quotas) | **GET** /1.7/quotas/users | 
[**update_user_quotas**](QuotasUsersApi.md#update_user_quotas) | **PATCH** /1.7/quotas/users | 


# **create_user_quotas**
> QuotasUserResponse create_user_quotas(file_system_names=file_system_names, uids=uids, user_names=user_names, quota=quota)



Create a new user quota

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasUser, rest

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

        # Add a quota of 1024 for the file system to apply to the users with ids 123 and 124
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name], uids=[123, 124],
                                                 quota=QuotasUser(quota=1024))
        # print the created quotas
        print(res.items)

        # Add a quota of 2048 for the file system to apply to the users with names user1 and user2
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name],
                                                 user_names=["user1", "user2"],
                                                 quota=QuotasUser(quota=2048))
        # print the created quotas
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or creating user quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **uids** | [**list[str]**](str.md)| A comma-separated list of user IDs. If after filtering, there is not at least one resource that matches each of the elements of user IDs, then an error is returned. This cannot be provided together with user_names query parameter. | [optional] 
 **user_names** | [**list[str]**](str.md)| A comma-separated list of user names. If after filtering, there is not at least one resource that matches each of the elements of user names, then an error is returned. This cannot be provided together with uids query parameter. | [optional] 
 **quota** | [**QuotasUser**](QuotasUser.md)|  | [optional] 

### Return type

[**QuotasUserResponse**](QuotasUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_user_quotas**
> delete_user_quotas(names=names, file_system_names=file_system_names, uids=uids, user_names=user_names)



Delete

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasUser, rest

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

        # Delete the quotas of users on the file system with ids 123 and 124
        fb.quotas_users.delete_user_quotas(file_system_names=[file_system_name], uids=[123, 124])
        # Delete the quotas of users on the file system with names user1 and user2
        fb.quotas_users.delete_user_quotas(file_system_names=[file_system_name],
                                           user_names=["user1", "user2"])
    except rest.ApiException as e:
        print("Exception when deleting user quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **uids** | [**list[str]**](str.md)| A comma-separated list of user IDs. If after filtering, there is not at least one resource that matches each of the elements of user IDs, then an error is returned. This cannot be provided together with user_names query parameter. | [optional] 
 **user_names** | [**list[str]**](str.md)| A comma-separated list of user names. If after filtering, there is not at least one resource that matches each of the elements of user names, then an error is returned. This cannot be provided together with uids query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_user_quotas**
> QuotasUserResponse list_user_quotas(names=names, filter=filter, limit=limit, sort=sort, start=start, token=token, file_system_names=file_system_names, uids=uids)



A list of quota user entries

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasUser, rest

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

        # Add a quota of 1024 for the file system to apply to the users with ids 123 and 124
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name], uids=[123, 124],
                                                 quota=QuotasUser(quota=1024))

        # Add a quota of 2048 for the file system to apply to the users with names user1 and user2
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name],
                                                 user_names=["user1", "user2"],
                                                 quota=QuotasUser(quota=2048))

        # List all user quotas for the file system
        res = fb.quotas_users.list_user_quotas(file_system_names=[file_system_name])
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or listing user quotas: %s\n" % e)
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
 **uids** | [**list[str]**](str.md)| A comma-separated list of user IDs. If after filtering, there is not at least one resource that matches each of the elements of user IDs, then an error is returned. This cannot be provided together with user_names query parameter. | [optional] 

### Return type

[**QuotasUserResponse**](QuotasUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_user_quotas**
> QuotasUserResponse update_user_quotas(names=names, file_system_names=file_system_names, uids=uids, user_names=user_names, quota=quota)



Update existing user quotas

### Example 
```python
from purity_fb import PurityFb, FileSystem, QuotasUser, rest

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

        # Add a quota of 1024 for the file system to apply to the users with ids 123 and 124
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name],
                                                 uids=[123, 124],
                                                 quota=QuotasUser(quota=1024))
        # print the created quotas
        print(res.items)
        # Update the quota for users with ids 123 and 124 to be 2048 bytes
        res = fb.quotas_users.update_user_quotas(file_system_names=[file_system_name],
                                                 uids=[123, 124],
                                                 quota=QuotasUser(quota=2048))
        # print the updated quotas
        print(res.items)

        # Add a quota of 2048 for the file system to apply to the users with names user1 and user2
        res = fb.quotas_users.create_user_quotas(file_system_names=[file_system_name],
                                                 user_names=["user1", "user2"],
                                                 quota=QuotasUser(quota=2048))
        # print the created quotas
        print(res.items)
        # Update the quota for users with names user1 and user2 to be 1024 bytes
        res = fb.quotas_users.update_user_quotas(file_system_names=[file_system_name],
                                                 user_names=["user1", "user2"],
                                                 quota=QuotasUser(quota=1024))
        # print the updated quotas
        print(res.items)
    except rest.ApiException as e:
        print("Exception when creating file system or updating user quotas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **file_system_names** | [**list[str]**](str.md)| A comma-separated list of file system names. If after filtering, there is not at least one resource that matches each of the elements of names, then an error is returned. | [optional] 
 **uids** | [**list[str]**](str.md)| A comma-separated list of user IDs. If after filtering, there is not at least one resource that matches each of the elements of user IDs, then an error is returned. This cannot be provided together with user_names query parameter. | [optional] 
 **user_names** | [**list[str]**](str.md)| A comma-separated list of user names. If after filtering, there is not at least one resource that matches each of the elements of user names, then an error is returned. This cannot be provided together with uids query parameter. | [optional] 
 **quota** | [**QuotasUser**](QuotasUser.md)|  | [optional] 

### Return type

[**QuotasUserResponse**](QuotasUserResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

