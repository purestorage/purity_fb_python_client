# purity_fb.HardwareConnectorsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_hardware_connectors**](HardwareConnectorsApi.md#list_hardware_connectors) | **GET** /1.3/hardware-connectors | 
[**update_hardware_connectors**](HardwareConnectorsApi.md#update_hardware_connectors) | **PATCH** /1.3/hardware-connectors | 


# **list_hardware_connectors**
> HardwareConnectorResponse list_hardware_connectors(filter=filter, sort=sort, start=start, limit=limit, token=token, names=names)



List hardware connectors

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
        # list all hardware connectors
        res = fb.hardware_connectors.list_hardware_connectors()
        # list and sort by name in descendant order
        res = fb.hardware_connectors.list_hardware_connectors(limit=5, sort="name-")
        # list with page size 5
        res = fb.hardware_connectors.list_hardware_connectors(limit=5)
        # list all remaining hardware connectors
        res = fb.hardware_connectors.list_hardware_connectors(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.hardware_connectors.list_hardware_connectors(filter='port_count=4')
    except rest.ApiException as e:
        print("Exception when listing hardware connectors: %s\n" % e)```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**HardwareConnectorResponse**](HardwareConnectorResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_hardware_connectors**
> HardwareConnectorResponse update_hardware_connectors(names=names, hardware_connector=hardware_connector)



Update an existing hardware connector

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
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **hardware_connector** | [**HardwareConnector**](HardwareConnector.md)| the attribute map used to update the hardware connector | [optional] 

### Return type

[**HardwareConnectorResponse**](HardwareConnectorResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

