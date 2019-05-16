# purity_fb_1dot8.SupportApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_support**](SupportApi.md#list_support) | **GET** /1.8/support | 
[**test_support**](SupportApi.md#test_support) | **GET** /1.8/support/test | 
[**update_support**](SupportApi.md#update_support) | **PATCH** /1.8/support | 


# **list_support**
> SupportResponse list_support()



List support

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # List support
        res = fb.support.list_support()
        print(res.items)
    except rest.ApiException as e:
        print("Exception when listing support settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportResponse**](SupportResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_support**
> TestResultResponse test_support(filter=filter, sort=sort, test_type=test_type)



Test support

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Test phonehome
        res = fb.support.test_support(test_type='phonehome')
        # print the results
        print(res.items)
        # Test remote assist
        res = fb.support.test_support(test_type='remote-assist')
        # print the results
        print(res.items)
        # Test both
        res = fb.support.test_support()
        # print the results
        print(res.items)
    except rest.ApiException as e:
        print("Exception when testing support: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **test_type** | **str**| Specify the type of test, either \&quot;phonehome\&quot; or \&quot;remote-assist\&quot;. | [optional] 

### Return type

[**TestResultResponse**](TestResultResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_support**
> SupportResponse update_support(support)



Update support

### Example 
```python
from purity_fb import PurityFb, rest, Support

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update support settings to enable phonehome and set a proxy
        proxy = 'https://my-proxy:my-password.com:8888'
        phonehome_enabled = True
        support_settings_updates = Support(proxy=proxy, phonehome_enabled=phonehome_enabled)
        res = fb.support.update_support(support=support_settings_updates)
        # print our response containing our updates
        print(res.items)

        # open a remote assist session
        remote_assist_active = True
        open_ra_settings = Support(remote_assist_active=remote_assist_active)
        res = fb.support.update_support(support=support_settings_updates)
        # print our response, which will now have the time that our remote assist session was opened
        # and when it will expire
        print(res.items)
    except rest.ApiException as e:
        print("Exception when updating support settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **support** | [**Support**](Support.md)|  | 

### Return type

[**SupportResponse**](SupportResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

