# purity_fb_1dot9.QuotasSettingsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_quotas_settings**](QuotasSettingsApi.md#list_quotas_settings) | **GET** /1.9/quotas/settings | 
[**update_quotas_settings**](QuotasSettingsApi.md#update_quotas_settings) | **PATCH** /1.9/quotas/settings | 


# **list_quotas_settings**
> QuotasSettingResponse list_quotas_settings()



List quotas notification settings.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # check the contact info being sent to end users and groups regarding their quotas, and
        # check if direct notifications to them are enabled
        res = fb.quotas_settings.list_quotas_settings()
        # print the result of our list for record keeping
        print(res)
    except rest.ApiException as e:
        print("Exception when listing quotas settings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QuotasSettingResponse**](QuotasSettingResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_quotas_settings**
> QuotasSettingResponse update_quotas_settings(quotas_setting)



Update quotas notification settings.

### Example 
```python
from purity_fb import PurityFb, QuotasSetting, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # set our contact info to a person and their email, and enable direct notification of
        # users and groups regarding their quotas
        new_contact = 'John Doe - j.doe@mycompany.com'
        update_settings = QuotasSetting(contact=new_contact, direct_notifications_enabled=True)
        res = fb.quotas_settings.update_quotas_settings(quotas_setting=update_settings)
        # print the result of our update for record keeping
        print(res)
    except rest.ApiException as e:
        print("Exception when updating quotas settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quotas_setting** | [**QuotasSetting**](QuotasSetting.md)|  | 

### Return type

[**QuotasSettingResponse**](QuotasSettingResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

