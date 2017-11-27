# purity_fb.AdminsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_admins**](AdminsApi.md#list_admins) | **GET** /1.2/admins | 
[**update_admins**](AdminsApi.md#update_admins) | **PATCH** /1.2/admins | 


# **list_admins**
> AdminResponse list_admins(expose=expose, names=names)



list all administrative accounts

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
api_instance = purity_fb.AdminsApi()
expose = false # bool | display the unmasked API token (optional) (default to false)
names = ['names_example'] # list[str] | A list of names. (optional)

try: 
    api_response = api_instance.list_admins(expose=expose, names=names)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminsApi->list_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expose** | **bool**| display the unmasked API token | [optional] [default to false]
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**AdminResponse**](AdminResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_admins**
> AdminResponse update_admins(admin, names=names)



update administrative account attributes

### Example 
```python
from purity_fb import PurityFb, Admin, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # change password
        myAdmin = Admin()
        myAdmin.old_password = "pureuser"
        myAdmin.password = "fakepass"
        res = fb.admins.update_admins(myAdmin, names=['pureuser'])

    except rest.ApiException as e:
        print("Exception when changing password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin** | [**Admin**](Admin.md)|  | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**AdminResponse**](AdminResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

