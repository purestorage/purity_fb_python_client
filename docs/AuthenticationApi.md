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
from purity_fb import PurityFb, rest

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
from purity_fb import PurityFb, FileSystem, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    # login to the array with your API_TOKEN
    # use *_with_http_info method to get response header as well as body
    res = fb.authentication.login_with_http_info(API_TOKEN)
    X_AUTH_TOKEN = res[2]['x-auth-token']
    # update x-auth-token header using the response of log in
    fb.authentication._api_client.default_headers['x-auth-token'] = X_AUTH_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
try:
    # logout from the array
    # use *_with_http_info method to get response header as well as body
    fb.authentication.logout_with_http_info()
except rest.ApiException as e:
    print("Exception when logging out from the array: %s\n" % e)
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

