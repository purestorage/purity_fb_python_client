# purity_fb.HardwareApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hardware**](HardwareApi.md#list_hardware) | **GET** /1.3/hardware | 
[**update_hardware**](HardwareApi.md#update_hardware) | **PATCH** /1.3/hardware | 


# **list_hardware**
> HardwareResponse list_hardware(names=names, filter=filter, limit=limit, sort=sort, start=start, token=token)



List hardware components

### Example 
```python
from purity_fb import PurityFb, Hardware, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # list all hardware components
        res = fb.hardware.list_hardware()
        # list a subset of hardware components by name
        res = fb.hardware.list_hardware(names=['CH1.FB1', 'CH1.FB2'])
        # list all ethernet ports
        res = fb.hardware.list_hardware(filter='type=\'eth\'')
    except rest.ApiException as e:
        print("Exception when listing hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**HardwareResponse**](HardwareResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_hardware**
> HardwareResponse update_hardware(names, hardware)



Update an existing hardware component

### Example 
```python
from purity_fb import PurityFb, Hardware, rest

fb = PurityFb('10.255.8.20') # assume the array IP is 10.255.8.20
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # turn visual identifier on
        res = fb.hardware.update_hardware(names=['CH1.FB1'], hardware=Hardware(identify_enabled=True))
        # turn visual identifier off
        res = fb.hardware.update_hardware(names=['CH1.FB1'], hardware=Hardware(identify_enabled=False))
    except rest.ApiException as e:
        print("Exception when updating hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)|  | 
 **hardware** | [**Hardware**](Hardware.md)|  | 

### Return type

[**HardwareResponse**](HardwareResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

