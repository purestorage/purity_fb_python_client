# purity_fb_1dot11.DirectoryServicesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_directory_services**](DirectoryServicesApi.md#list_directory_services) | **GET** /1.11/directory-services | 
[**list_directory_services_roles**](DirectoryServicesApi.md#list_directory_services_roles) | **GET** /1.11/directory-services/roles | 
[**test_directory_services**](DirectoryServicesApi.md#test_directory_services) | **GET** /1.11/directory-services/test | 
[**test_directory_services_with_changes**](DirectoryServicesApi.md#test_directory_services_with_changes) | **PATCH** /1.11/directory-services/test | 
[**update_directory_services**](DirectoryServicesApi.md#update_directory_services) | **PATCH** /1.11/directory-services | 
[**update_directory_services_roles**](DirectoryServicesApi.md#update_directory_services_roles) | **PATCH** /1.11/directory-services/roles | 


# **list_directory_services**
> DirectoryServiceResponse list_directory_services(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List directory services.

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
        # list Directory Services configuration
        res = fb.directory_services.list_directory_services(names=["nfs"])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing directory services configuration: %s\n" % e)
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

[**DirectoryServiceResponse**](DirectoryServiceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_directory_services_roles**
> DirectoryServiceRolesResponse list_directory_services_roles(ids=ids, names=names)



List directory services roles configurations.

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryServiceRole

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list Directory Services configuration
        res = fb.directory_services.list_directory_services_roles()
        print(res)

        # list settings configuration for a specific role
        ROLE_NAME = 'array_admin'
        res = fb.directory_services.list_directory_services_roles(names=[ROLE_NAME])
    except rest.ApiException as e:
        print("Exception when listing directory services roles configurations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**DirectoryServiceRolesResponse**](DirectoryServiceRolesResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_directory_services**
> TestResultResponse test_directory_services(ids=ids, names=names)



Test directory services.

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryService, Reference

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # test the nfs directory service configuration that exists already
        res = fb.directory_services.test_directory_services(names=['nfs'])
        print(res)
    except rest.ApiException as e:
        print("Exception when testing directory services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**TestResultResponse**](TestResultResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_directory_services_with_changes**
> TestResultResponse test_directory_services_with_changes(ids=ids, names=names, directory_service=directory_service)



Test directory services with changes.

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryService, Reference

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # test the existing nfs directory service configuration, but using a different certificate
        # and bind user
        test_bind_user = 'CN=differentUser,CN=Users,DC=example,DC=com'
        test_certificate_name = 'nfs-server-certificate'
        cert_reference = Reference(name=test_certificate_name)
        test_ds_config = DirectoryService(bind_user=test_bind_user, certificate=cert_reference)

        res = fb.directory_services.test_directory_services_with_changes(names=['nfs'],
                                                                         directory_service=test_ds_config)
        print(res)

    except rest.ApiException as e:
        print("Exception when testing directory services changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **directory_service** | [**DirectoryService**](DirectoryService.md)| An optional directory service configuration which, if provided, will be used to overwrite aspects of the existing directory service objects when performing tests. | [optional] 

### Return type

[**TestResultResponse**](TestResultResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_directory_services**
> DirectoryServiceResponse update_directory_services(directory_service, ids=ids, names=names)



Update directory services.

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryService, Reference

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update Directory Services smb configuration to specify a join OU in an LDAP server
        name = 'smb'
        URI = 'ldaps://ad1.mycompany.com'
        BASE_DN = 'DC=mycompany,DC=com'
        BIND_USER = 'CN=John,OU=Users,DC=mycompany,DC=com'
        BIND_PW = 'johnldappassword'

        SMB_JOIN_OU = 'OU=PureStorage,OU=StorageArrays,OU=ServiceMachines'
        SMB_ATTRS = {'join_ou': SMB_JOIN_OU}

        directory_service = DirectoryService(base_dn=BASE_DN, bind_password=BIND_PW, bind_user=BIND_USER, uris=[URI],
                                             enabled=True, smb=SMB_ATTRS)
        res = fb.directory_services.update_directory_services(names=[name], directory_service=directory_service)
        print(res)

        # update Directory Services nfs configuration to use an NIS configuration
        name = 'nfs'
        MASTER_SERVER_HOSTNAME = 'nis.master.server.example.com'
        BACKUP_SERVER_HOSTNAME = 'nis.backup.server.example.com'
        BACKUP_SERVER_IP = '188.123.4.43'
        nis_servers = [MASTER_SERVER_HOSTNAME, BACKUP_SERVER_IP, BACKUP_SERVER_HOSTNAME]

        NIS_DOMAIN = 'my-nis-domain'
        NFS_ATTRS = {'nis_domains': [NIS_DOMAIN], 'nis_servers': nis_servers}

        # the only fields needed in order to enable the nfs directory service when configuring
        # NIS are an NIS domain and NIS servers
        directory_service = DirectoryService(enabled=True, nfs=NFS_ATTRS)
        res = fb.directory_services.update_directory_services(names=[name],
                                                              directory_service=directory_service)
        print(res)

        # update the management directory service to use an Oracle Unified Directory server,
        # specifying our user object class as "inetOrgPerson" and our login attribute as
        # "givenName"
        name = 'management'
        OUD_URI = 'ldap://my-oud-leader.example.com'
        OUD_BASE_DN = 'DC=example,DC=com'
        OUD_BIND_USER = 'CN=ServiceAcct,OU=Users,DC=example,DC=com'
        OUD_BIND_PW = 'something-absurdly-complex'

        USER_LOGIN_ATTR = 'givenName'
        USER_OBJ_CLASS = 'inetOrgPerson'
        MGMT_ATTRS = {'user_login_attribute': USER_LOGIN_ATTR,
                      'user_object_class': USER_OBJ_CLASS}
        directory_service = DirectoryService(base_dn=OUD_BASE_DN, bind_password=OUD_BIND_PW,
                                             bind_user=OUD_BIND_USER, uris=[OUD_URI],
                                             enabled=True, management=MGMT_ATTRS)
        res = fb.directory_services.update_directory_services(names=[name],
                                                              directory_service=directory_service)
        print(res)

    except rest.ApiException as e:
        print("Exception when updating directory services configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_service** | [**DirectoryService**](DirectoryService.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**DirectoryServiceResponse**](DirectoryServiceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_directory_services_roles**
> DirectoryServiceRolesResponse update_directory_services_roles(names, directory_service_role, ids=ids)



Update directory services roles configurations.

### Example 
```python
from purity_fb import PurityFb, rest, DirectoryServiceRole

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update Directory Services role configuration
        ARRAY_ADMIN_GRP = 'admins'
        GROUP_BASE = 'ou=purestorage,ou=us'
        ROLE_NAME = 'array_admin'

        directory_service_role = DirectoryServiceRole(group_base=GROUP_BASE, group=ARRAY_ADMIN_GRP)
        res = fb.directory_services.update_directory_services_roles(names=[ROLE_NAME],
            directory_service_role=directory_service_role)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating directory services roles configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A required list of names. | 
 **directory_service_role** | [**DirectoryServiceRole**](DirectoryServiceRole.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 

### Return type

[**DirectoryServiceRolesResponse**](DirectoryServiceRolesResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

