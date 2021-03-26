# purity_fb_1dot12.LoginBannerApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_login_banner**](LoginBannerApi.md#list_login_banner) | **GET** /login-banner | 


# **list_login_banner**
> LoginBannerResponse list_login_banner()



Get the login banner for the array.

### Example 
```python
from purity_fb import PurityFb, LoginBannerResponse, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    # no need to login to get login-banner
    res = fb.login_banner.list_login_banner()
    assert isinstance(res, LoginBannerResponse)
    print(res.login_banner)  # ex: "Restricted area. Authorized personnel only."
except rest.ApiException as e:
    print("Exception when getting login-banner from the array: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LoginBannerResponse**](LoginBannerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

