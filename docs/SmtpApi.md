# purity_fb_1dot8.SmtpApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_smtp**](SmtpApi.md#list_smtp) | **GET** /1.8/smtp | 
[**update_smtp**](SmtpApi.md#update_smtp) | **PATCH** /1.8/smtp | 


# **list_smtp**
> SmtpResponse list_smtp()



List smtp

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
        res = fb.smtp.list_smtp() # The SMTP properties are related to alert routing
        print(res)
    except rest.ApiException as e:
        print("Exception when listing smtp settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SmtpResponse**](SmtpResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_smtp**
> SmtpResponse update_smtp(smtp_settings)



Update smtp

### Example 
```python
from purity_fb import PurityFb, Smtp, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        smtp_settings = Smtp(relay_host="test-host.com", sender_domain="purestorage.com")
        res = fb.smtp.update_smtp(smtp_settings=smtp_settings)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating smtp configuration settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **smtp_settings** | [**Smtp**](Smtp.md)|  | 

### Return type

[**SmtpResponse**](SmtpResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

