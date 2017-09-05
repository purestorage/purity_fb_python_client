# purity_fb.AuthenticationApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthenticationApi.md#login) | **POST** /login | 
[**logout**](AuthenticationApi.md#logout) | **POST** /logout | 


# **login**
> LoginResponse login(api_token)



Log in to the server

### Example 
```python
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    # login to the array with your API_TOKEN
    # use *_with_http_info method to get response header as well as body
    res = fb.authentication.login_with_http_info(API_TOKEN)
    X_AUTH_TOKEN = res[2]['x-auth-token']
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_token** | **str**| the token to log in | 

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

[ApiTokenQueryParam](index.md#ApiTokenQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **logout**
> logout()



Log out from the server

### Example 
```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthTokenHeader
purity_fb.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# purity_fb.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = purity_fb.AuthenticationApi()

try: 
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

