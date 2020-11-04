# purity_fb_1dot11.SyslogApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_syslog_servers**](SyslogApi.md#create_syslog_servers) | **POST** /1.11/syslog-servers | 
[**delete_syslog_servers**](SyslogApi.md#delete_syslog_servers) | **DELETE** /1.11/syslog-servers | 
[**list_syslog_servers**](SyslogApi.md#list_syslog_servers) | **GET** /1.11/syslog-servers | 
[**list_syslog_settings**](SyslogApi.md#list_syslog_settings) | **GET** /1.11/syslog-servers/settings | 
[**test_syslog_config**](SyslogApi.md#test_syslog_config) | **GET** /1.11/syslog-servers/test | 
[**update_syslog_servers**](SyslogApi.md#update_syslog_servers) | **PATCH** /1.11/syslog-servers | 
[**update_syslog_settings**](SyslogApi.md#update_syslog_settings) | **PATCH** /1.11/syslog-servers/settings | 


# **create_syslog_servers**
> SyslogServerResponse create_syslog_servers(names, syslog)



Configure a new syslog server. Transmission of syslog messages is enabled immediately.

### Example 
```python
from purity_fb import PurityFb, rest, SyslogServerPostOrPatch

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Post a syslog server using a TCP connection
        attr = SyslogServerPostOrPatch(uri='tcp://my_syslog_host.domain.com:541')
        res = fb.syslog.create_syslog_servers(syslog=attr, names=["my_tcp_connection"])
        print(res)

        # Post a syslog server using a UDP connection
        udp_attr = SyslogServerPostOrPatch(uri='udp://my_syslog_host.domain.com:540')
        res = fb.syslog.create_syslog_servers(syslog=udp_attr, names=["my_udp_connection"])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating syslog server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| Performs the operation on the unique name specified. | 
 **syslog** | [**SyslogServerPostOrPatch**](SyslogServerPostOrPatch.md)|  | 

### Return type

[**SyslogServerResponse**](SyslogServerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_syslog_servers**
> delete_syslog_servers(ids=ids, names=names)



Delete a configured syslog server and stop forwarding syslog messages.

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
        # Delete the syslog server named "syslog_old"
        res = fb.syslog.delete_syslog_servers(names=["syslog_old"])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting syslog server: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_syslog_servers**
> SyslogServerResponse list_syslog_servers(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



Return a list of configured syslog servers.

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
        # List all configured syslog servers
        res = fb.syslog.list_syslog_servers()
        print(res)

        # List first two syslog servers beginning with 'syslog_fb'. Use default sorting.
        res = fb.syslog.list_syslog_servers(limit=2, names=["syslog_fb*"])
        print(res)

        # List the first syslog server when sorting by name.
        res = fb.syslog.list_syslog_servers(limit=1, sort="name")
        print(res)

        # List all syslog servers using TCP connections
        res = fb.syslog.list_syslog_servers(filter='uri=\'tcp*\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing syslog servers: %s\n" % e)
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

[**SyslogServerResponse**](SyslogServerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_syslog_settings**
> SyslogServerSettingResponse list_syslog_settings(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List Syslog settings

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
        # List the current syslog server settings
        res = fb.syslog.list_syslog_settings()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing syslog server settings: %s\n" % e)
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

[**SyslogServerSettingResponse**](SyslogServerSettingResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_syslog_config**
> SyslogServerTestResponse test_syslog_config(ids=ids, names=names, token=token)



Test Syslog Configuration

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
        # Log two test messages to each configured syslog server.
        res = fb.syslog.test_syslog_config()
        print(res)
    except rest.ApiException as e:
        print("Exception when testing syslog configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| Performs the operation on the unique name specified. Enter multiple names in comma-separated format. For example, &#x60;name01,name02&#x60;. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**SyslogServerTestResponse**](SyslogServerTestResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_syslog_servers**
> SyslogServerResponse update_syslog_servers(syslog, ids=ids, names=names)



Modify the URI of a configured syslog server.

### Example 
```python
from purity_fb import PurityFb, rest, SyslogServerPostOrPatch

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Update the uri of the server named "main_syslog"
        attr = SyslogServerPostOrPatch(uri='tcp://new_syslog_host.domain.com:541')
        res = fb.syslog.update_syslog_servers(syslog=attr, names=["main_syslog"])
        print(res)
    except rest.ApiException as e:
        print("Exception when updating syslog server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog** | [**SyslogServerPostOrPatch**](SyslogServerPostOrPatch.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**SyslogServerResponse**](SyslogServerResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_syslog_settings**
> SyslogServerSettingResponse update_syslog_settings(syslog_settings, ids=ids, names=names)



Update Syslog settings

### Example 
```python
from purity_fb import PurityFb, rest, SyslogServerSettingPatch, Reference

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Assuming a certificate named "syslog_server_cert" has already been uploaded to the array,
        # retrieve that certificate by name and configure it to be used to authenticate the
        # connection with syslog servers.
        cert_name = 'syslog_server_cert'
        cert_res = fb.certificates.list_certificates(names=[cert_name])

        cert_item = cert_res.items[0]

        # Build a Reference using information from the certificate GET result
        cert_reference = Reference(name=cert_item.name, id=cert_item.id, resource_type='certificates')

        attr = SyslogServerSettingPatch(ca_certificate=cert_reference)
        res = fb.syslog.update_syslog_settings(syslog_settings=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating syslog server settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **syslog_settings** | [**SyslogServerSettingPatch**](SyslogServerSettingPatch.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**SyslogServerSettingResponse**](SyslogServerSettingResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

