# purity_fb_1dot7.AlertsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_alerts**](AlertsApi.md#list_alerts) | **GET** /1.7/alerts | 
[**update_alerts**](AlertsApi.md#update_alerts) | **PATCH** /1.7/alerts | 


# **list_alerts**
> AlertResponse list_alerts(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List all alerts

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
        res = fb.alerts.list_alerts()
        print(res)
        # list alerts and sort by severity
        res = fb.alerts.list_alerts(sort='severity')
    except rest.ApiException as e:
        print("Exception when listing alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_alerts**
> AlertResponse update_alerts(alert_settings, names=names)



Update alerts

### Example 
```python
from purity_fb import PurityFb, Alert, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    alert_settings = Alert(flagged=False)
    try:
        # unflag an alert with the given id
        res = fb.alerts.update_alerts(
            names=['1'], alert_settings=alert_settings)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating alert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alert_settings** | [**Alert**](Alert.md)|  | 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**AlertResponse**](AlertResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

