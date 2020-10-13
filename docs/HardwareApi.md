# purity_fb_1dot10.HardwareApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hardware**](HardwareApi.md#list_hardware) | **GET** /1.10/hardware | 
[**update_hardware**](HardwareApi.md#update_hardware) | **PATCH** /1.10/hardware | 


# **list_hardware**
> HardwareResponse list_hardware(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List hardware components.

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
        # list all fans
        res = fb.hardware.list_hardware(filter='type=\'fan\'')
        # list all XFMs
        res = fb.hardware.list_hardware(filter='type=\'xfm\'')
    except rest.ApiException as e:
        print("Exception when listing hardware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**HardwareResponse**](HardwareResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_hardware**
> HardwareResponse update_hardware(hardware, ids=ids, names=names)



Update an existing hardware component.

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
 **hardware** | [**Hardware**](Hardware.md)|  | 
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**HardwareResponse**](HardwareResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

