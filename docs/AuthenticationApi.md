# purity_fb_1dot11.AuthenticationApi

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
# this is required for versions before Purity//FB 2.1.3 because they only supports self-signed
# certificates. in later versions, this may be unnecessary if you have imported a certificate.
fb.disable_verify_ssl()
my_ca_certificate_file = '/net/ssl/fb_ca_certificate.pem'
try:
    # login to the array with your API_TOKEN
    # use *_with_http_info method to get response header as well as body
    res = fb.authentication.login_with_http_info(API_TOKEN)
    X_AUTH_TOKEN = res[2]['x-auth-token']

    # SSL verification can be turned on later. In order to make a transition from no SSL
    # verification to strict SSL verification easier, you may turn on a "Certificate Optional" mode
    # that SSL supports. This will allow REST calls to succeed without SSL verification when no
    # certificate is provided, but will begin strictly checking the certificate once one has been
    # provided, so that there is no disruption.
    fb.allow_verify_ssl()
    fb.configure_ca_certificate_file(my_ca_certificate_file)
    # enable strict verification once the file is configured.
    fb.enable_verify_ssl()

    # You can also provide the certificate at the same time that you enable strict SSL verification,
    # if you have already confirmed that your certificate is correct.
    fb.enable_verify_ssl(ca_certs_file_path=my_ca_certificate_file)
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)

# if you provide the path to a CA certificate(s) file on initialization, then SSL verification will
# be enabled by default
secure_fb = PurityFb("10.255.9.28", ca_certs_file_path=my_ca_certificate_file)
try:
    # login to the array with your API_TOKEN
    # use *_with_http_info method to get response header as well as body
    res = secure_fb.authentication.login_with_http_info(API_TOKEN)
    X_AUTH_TOKEN = res[2]['x-auth-token']

    # the CA certificate used for SSL verification can be changed later if desired
    new_ca_certificate_file = '/net/ssl/replacement_fb_ca_certificate.pem'
    secure_fb.configure_ca_certificate_file(new_ca_certificate_file)

    # SSL verification can be turned off later if desired
    secure_fb.disable_verify_ssl()
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

