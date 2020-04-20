# purity_fb_1dot11.ApiClientsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_api_clients**](ApiClientsApi.md#create_api_clients) | **POST** /1.11/api-clients | 
[**delete_api_clients**](ApiClientsApi.md#delete_api_clients) | **DELETE** /1.11/api-clients | 
[**list_api_clients**](ApiClientsApi.md#list_api_clients) | **GET** /1.11/api-clients | 
[**update_api_clients**](ApiClientsApi.md#update_api_clients) | **PATCH** /1.11/api-clients | 


# **create_api_clients**
> ApiClientsResponse create_api_clients(api_client, names=names)



Configure a new api client.

### Example 
```python
from purity_fb import PurityFb, rest, ApiClientPost

CLIENT_NAME = 'my_api_client'
CLIENT_TTL_IN_MS = 1000 * 60 * 60       # 1 hour in milliseconds
CLIENT_PUB_KEY = ("\n"
"-----BEGIN PUBLIC KEY-----\n"
"MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArSe6chh1JzME9svOKjU0\n"
"eKTm8S23Ok3Vr2bWuPri/YHfLrlnRwWoCt+st0/BebKSJ+fQUWOaLlqpZQKpI8oR\n"
"gJ9sWmwGibVG8cTuz7XMkskx9bsm/bjIenuB4W+s3g0BCsi9930mfdKgJgFzY69O\n"
"nLh7d7hAFcmhSJa945PryQZpvJ/U4Ue5F4d+WXgEJ0SoSRaZ6bbeMPhcbMHTzTum\n"
"2ZrPBkK5cqPYitaso6BXeAlqNQPw4Kbu4Ugm0CTogrtImkwoonWDDP34XMOq+u7q\n"
"sNTbJSvDKMTM1RPPrTWCaLiuZkdLVEVesZ9/8+XUMIgBTElwQJDCAQer03MJzqRr\n"
"1eCZGgLfDuYqwMG2MFaAX7kgqBwwyqRTd6MxaQxt2nkdfwiXSY71llzEQ23g3T+1\n"
"64zjwAL5f+dtu8PkGF7IdU2T8P2Qk9bG9pckwZHWYkBK77BAk5jbmSzsKGZgRb2R\n"
"1E+TWDKIaveFhQp251j/C5wkZwMXgjOzN+BOPo+OiLBGUl+jRybWA9f7Vq1MEdf6\n"
"SEdLiqYrXcZERkYBMieLXAfdtaztAIb96cUu+OKMSLDk+D0GHkUfm7lEbDK3ew1+\n"
"D6z+BnxDyH6oqZzz4lS2kPLBLsc+6pdTGuKLf0S9YuLiqJe659AdwU8+X/3KtwNd\n"
"FVJSaxdFbWx0nj3hJqFkIO8CAwEAAQ==\n"
"-----END PUBLIC KEY-----\n")

fb = PurityFb("10.255.8.20", version=__version__)  # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Create a new api client with a max_role of storage_admin who has permissions to 
        # perform storage related operations such as administering volumns, hosts and host groups.
        # Note that this created api client will have the lesser of the permissions granted by max_role
        # in the api_client and the max role of the associated oath login.
        # The public_key will be the key provided by your oath login provider.
        attr = ApiClientPost(max_role={'name':'storage_admin'},
                             public_key=CLIENT_PUB_KEY,
                             issuer=CLIENT_NAME,
                             access_token_ttl_in_ms=CLIENT_TTL_IN_MS)
        res = fb.api_clients.create_api_clients(names=[CLIENT_NAME], api_client=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating api_clients: %s\n" % e)

```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_client** | [**ApiClientPost**](ApiClientPost.md)|  | 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of names, then an error is returned. For example, &#x60;name01,name02&#x60;. | [optional] 

### Return type

[**ApiClientsResponse**](ApiClientsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_api_clients**
> delete_api_clients(ids=ids, names=names)



Delete a configured api client.

### Example 
```python
from purity_fb import PurityFb, rest


CLIENT_NAME = 'my_api_client'
fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Delete the api client named "my_api_client"
        res = fb.api_clients.delete_api_clients(names=[CLIENT_NAME])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting api clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of names, then an error is returned. For example, &#x60;name01,name02&#x60;. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_api_clients**
> ApiClientsResponse list_api_clients(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



Return a list of configured api clients.

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
        # List all configured api clients.
        res = fb.api_clients.list_api_clients()
        print(res)
        # List first two api clients beginning with 'my_oath'. Use default sorting.
        res = fb.api_clients.list_api_clients(limit=2, names=["my_oauth"])
        print(res)
        # List the first api client when sorting by name.
        res = fb.api_clients.list_api_clients(limit=1, sort="name")
        print(res)
        # List all api_clients servers that are enabled
        res = fb.api_clients.list_api_clients(filter='enabled=\"True\"')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing api clients: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. If there is not at least one resource that matches each of the elements of names, then an error is returned. For example, &#x60;name01,name02&#x60;. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**ApiClientsResponse**](ApiClientsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_api_clients**
> ApiClientsResponse update_api_clients(names, api_clients, ids=ids)



Enable or disable an api client.

### Example 
```python
from purity_fb import PurityFb, rest, ApiClientPatch

CLIENT_NAME = 'my_api_client'
fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Enable the api client.
        attr = ApiClientPatch(enabled=True)
        res = fb.api_clients.update_api_clients(api_clients=attr, names=[CLIENT_NAME])
        print(res)
    except rest.ApiException as e:
        print("Exception when updating api client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A required list of names. | 
 **api_clients** | [**ApiClientPatch**](ApiClientPatch.md)|  | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 

### Return type

[**ApiClientsResponse**](ApiClientsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

