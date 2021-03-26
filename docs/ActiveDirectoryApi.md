# purity_fb_1dot12.ActiveDirectoryApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_active_directory**](ActiveDirectoryApi.md#create_active_directory) | **POST** /1.12/active-directory | 
[**delete_active_directory**](ActiveDirectoryApi.md#delete_active_directory) | **DELETE** /1.12/active-directory | 
[**list_active_directory**](ActiveDirectoryApi.md#list_active_directory) | **GET** /1.12/active-directory | 
[**test_active_directory**](ActiveDirectoryApi.md#test_active_directory) | **GET** /1.12/active-directory/test | 
[**update_active_directory**](ActiveDirectoryApi.md#update_active_directory) | **PATCH** /1.12/active-directory | 


# **create_active_directory**
> ActiveDirectoryResponse create_active_directory(active_directory, names=names, join_existing_account=join_existing_account)



Create an Active Directory account

### Example 
```python
from purity_fb import PurityFb, ActiveDirectoryPost, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        AD_ACCOUNT_NAME = "ad_test_account"

        # When creating a new Active Directory account, it is required that you specify the domain.
        # You will also need to provide the credentials for an account which has level of
        # permissions necessary to create and configure the array's corresponding Computer account
        # within the Active Directory domain itself.
        DOMAIN = "my-corporation.com"
        ADMIN_USER = "Administrator"
        ADMIN_PASSWORD = "some_secure_passw0rd!"

        # Additionally, several optional values can be specified during creation in order to further
        # configure the Active Directory Account. With the exception of the `computer_name`, all
        # optional values can be later updated via a PATCH with update_active_directory().
        COMPUTER_ACCOUNT_NAME = "FB-Array1"
        ENCRYPTION_TYPES = ["aes128-cts-hmac-sha1-96", "aes256-cts-hmac-sha1-96"]
        SPNS = ["nfs/vip1.my-array.my-corporation.com"]
        JOIN_OU = "OU=MyOrg,OU=PureArrays"

        # If the following server preferences are not provided, the array will use DNS to
        # automatically discover available servers within the domain.
        PREFERRED_LDAP_SERVERS = ["ldap.my-corporation.com"]
        PREFERRED_KERBEROS_SERVERS = ["10.10.20.80"]

        attr = ActiveDirectoryPost(domain=DOMAIN,
                                   computer_name=COMPUTER_ACCOUNT_NAME,
                                   join_ou=JOIN_OU,
                                   service_principal_names=SPNS,
                                   encryption_types=ENCRYPTION_TYPES,
                                   directory_servers=PREFERRED_LDAP_SERVERS,
                                   kerberos_servers=PREFERRED_KERBEROS_SERVERS,
                                   user=ADMIN_USER,
                                   password=ADMIN_PASSWORD)
        res = fb.active_directory.create_active_directory(attr,
                                                          names=[AD_ACCOUNT_NAME])
        print(res)

        # In some environments, it may be desirable to have the array join to the Active Directory
        # domain using an existing Computer account that has already been created and configured.
        # To accomplish this, the `join_existing_account` query parameter must be used. However,
        # certain values cannot be specified upon creation when joining a new account (e.g.
        # service_principal_names, fqdns, join_ou and encryption_types.
        attr = ActiveDirectoryPost(domain=DOMAIN,
                                   computer_name=COMPUTER_ACCOUNT_NAME,
                                   directory_servers=PREFERRED_LDAP_SERVERS,
                                   kerberos_servers=PREFERRED_KERBEROS_SERVERS,
                                   user=ADMIN_USER,
                                   password=ADMIN_PASSWORD)
        res = fb.active_directory.create_active_directory(attr,
                                                          names=[AD_ACCOUNT_NAME],
                                                          join_existing_account=True)
        print(res)

    except rest.ApiException as e:
        print("Exception when updating Active Directory account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_directory** | [**ActiveDirectoryPost**](ActiveDirectoryPost.md)|  | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **join_existing_account** | **bool**| If specified as &#x60;true&#x60;, the domain is searched for a pre-existing computer account to join to, and no new account will be created within the domain. The &#x60;user&#x60; specified when joining to a pre-existing account must have permissions to &#39;read attributes from&#39; and &#39;reset the password of&#39; the pre-existing account. &#x60;service_principal_names&#x60;, &#x60;encryption_types&#x60;, and &#x60;join_ou&#x60; will be read from the pre-existing account and cannot be specified when joining to an existing account. If not specified, defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**ActiveDirectoryResponse**](ActiveDirectoryResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_active_directory**
> delete_active_directory(ids=ids, local_only=local_only, names=names)



Deletes a configured Active Directory account

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        AD_ACCOUNT_NAME = "ad_test_account"

        # Delete the Active Directory account by name.
        res = fb.active_directory.delete_active_directory(names=[AD_ACCOUNT_NAME])
        print(res)

        # For the next example, specify the account by ID
        AD_ACCOUNT_ID = "b6c1ad27-0d4e-45aa-8f0f-fd3ccaf3ca06"

        # By default, as in the above example call, the array will not only
        # delete the account information stored on the array, but it will
        # also attempt to delete the corresponding Computer account within
        # the Active Directory domain.
        # If desired, the `local_only` keyword parameter can be used to
        # indicate that you do not wish to delete the Computer account
        # from the domain.
        res = fb.active_directory.delete_active_directory(ids=[AD_ACCOUNT_ID], local_only=True)
        print(res)

    except rest.ApiException as e:
        print("Exception when deleting an Active Directory account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **local_only** | **bool**| If specified as &#x60;true&#x60;, only delete the Active Directory configuration on the local array, without deleting the computer account created in the Active Directory domain. If not specified, defaults to &#x60;false&#x60;. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_active_directory**
> ActiveDirectoryResponse list_active_directory(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



Lists the configured Active Directory accounts

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
        # list all Active Directory accounts which are currently configured on
        # the array.
        # Note that there is currently a maximum of one Active Directory account
        # that is allowed to be configured on the array.
        res = fb.active_directory.list_active_directory()
        print(res)

        # Even with the current account limit, names or ids can be provided to filter
        # out any account which doesn't match the provided value.
        EXPECTED_ACCOUNT_NAME = "ad_test_account"
        EXPECTED_ACCOUNT_ID = "b6c1ad27-0d4e-45aa-8f0f-fd3ccaf3ca06"
        res_by_name = fb.active_directory.list_active_directory(names=[EXPECTED_ACCOUNT_NAME])
        print(res_by_name)

        res_by_id = fb.active_directory.list_active_directory(ids=[EXPECTED_ACCOUNT_ID])
        print(res_by_id)

    except rest.ApiException as e:
        print("Exception when listing Active Directory accounts: %s\n" % e)
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

[**ActiveDirectoryResponse**](ActiveDirectoryResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_active_directory**
> TestResultResponse test_active_directory(filter=filter, ids=ids, limit=limit, names=names, sort=sort)



Test a configured Active Directory account.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Test various levels of functionality for all configured Active Directory
        # accounts. This returns the results of each test as well as detailed
        # information regarding suspected issues.
        res = fb.active_directory.test_active_directory()
        print(res)

    except rest.ApiException as e:
        print("Exception when testing an Active Directory account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 

### Return type

[**TestResultResponse**](TestResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_active_directory**
> ActiveDirectoryResponse update_active_directory(active_directory, ids=ids, names=names)



Updates a configured Active Directory account

### Example 
```python
from purity_fb import PurityFb, ActiveDirectoryPatch, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Relocate the array's corresponding Computer account within the Active
        # Directory domain.
        # Unlike the rest of the properties that can be updated by update_active_directory(), any
        # updates to the `join_ou` must be done alone. It is not possible to move the array's
        # corresponding Computer account while simultaneously updating its other properties.
        AD_ACCOUNT_NAME = "ad_test_account"
        attr = ActiveDirectoryPatch(join_ou="OU=MyOrg,OU=PureArrays")
        res = fb.active_directory.update_active_directory(active_directory=attr, names=[AD_ACCOUNT_NAME])
        print(res)

        # Set or update the addresses of the preferred LDAP and Kerberos key
        # distribution servers. Accepted server formats are IP address and DNS name.
        PREFERRED_LDAP_SERVERS = ["ldap.my-corporation.com"]
        PREFERRED_KERBEROS_SERVERS = ["10.10.20.80"]
        attr = ActiveDirectoryPatch(directory_servers=PREFERRED_LDAP_SERVERS,
                                    kerberos_servers=PREFERRED_KERBEROS_SERVERS)
        res = fb.active_directory.update_active_directory(active_directory=attr, names=[AD_ACCOUNT_NAME])
        print(res)

        # Update the Encryption Types and Service Principal Names which are used by the account.
        ENCRYPTION_TYPES = ['aes128-cts-hmac-sha1-96', 'aes256-cts-hmac-sha1-96']
        SPNS = ["nfs/vip1.my-array.my-corporation.com"]
        attr = ActiveDirectoryPatch(encryption_types=ENCRYPTION_TYPES,
                                    service_principal_names=SPNS)
        res = fb.active_directory.update_active_directory(active_directory=attr, names=[AD_ACCOUNT_NAME])
        print(res)

        # As an alternative to specifying Service Principal Names, a list of FQDNs may be provided.
        FQDNS = ["vip1.my-array.my-corporation.com"]
        attr = ActiveDirectoryPatch(fqdns=ENCRYPTION_TYPES)
        res = fb.active_directory.update_active_directory(active_directory=attr, names=[AD_ACCOUNT_NAME])
        print(res)

    except rest.ApiException as e:
        print("Exception when updating Active Directory account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_directory** | [**ActiveDirectoryPatch**](ActiveDirectoryPatch.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**ActiveDirectoryResponse**](ActiveDirectoryResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

