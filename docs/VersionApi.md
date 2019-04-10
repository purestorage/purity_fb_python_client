# purity_fb_1dot7.VersionApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_versions**](VersionApi.md#list_versions) | **GET** /api_version | 


# **list_versions**
> VersionResponse list_versions()



Get all supported REST versions

### Example 
```python
from purity_fb import PurityFb, VersionResponse, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    # no need to login to get API versions
    res = fb.api_version.list_versions()
    assert isinstance(res, VersionResponse)
    print (res.versions)  # ["1.0", "1.1", "1.2"]
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionResponse**](VersionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

