# purity_fb_1dot8.LogsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_logs**](LogsApi.md#list_logs) | **GET** /1.8/logs | 


# **list_logs**
> file list_logs(end_time=end_time, start_time=start_time)



Download logs

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("irvm-yliu") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login('T-25ef41ee-1518-426f-9c46-372babb93e1b') # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        res = fb.logs.list_logs(start_time=1527415200000, end_time=1527415200000)
        print(res)
    except rest.ApiException as e:
        print("Exception when download logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 

### Return type

[**file**](file.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

