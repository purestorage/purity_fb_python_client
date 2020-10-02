# purity_fb_1dot10.NetworkInterfacesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_interfaces**](NetworkInterfacesApi.md#create_network_interfaces) | **POST** /1.10/network-interfaces | 
[**delete_network_interfaces**](NetworkInterfacesApi.md#delete_network_interfaces) | **DELETE** /1.10/network-interfaces | 
[**list_network_interfaces**](NetworkInterfacesApi.md#list_network_interfaces) | **GET** /1.10/network-interfaces | 
[**update_network_interfaces**](NetworkInterfacesApi.md#update_network_interfaces) | **PATCH** /1.10/network-interfaces | 


# **create_network_interfaces**
> NetworkInterfaceResponse create_network_interfaces(names=names, network_interface=network_interface)



Create a new network interface.

### Example 
```python
from purity_fb import PurityFb, rest, NetworkInterface

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create vip named myvip on the array
        res = fb.network_interfaces.create_network_interfaces(
            names=["myvip"],
            network_interface=NetworkInterface(address='1.2.3.101',
                                               services=["data"],
                                               type="vip"))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating network interface: %s\n" % e)

    try:
        # create a replication vip named replvip on the array
        res = fb.network_interfaces.create_network_interfaces(
            names=["replvip"],
            network_interface=NetworkInterface(address='1.2.3.101',
                                               services=["replication"],
                                               type="vip"))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating network interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **network_interface** | [**NetworkInterface**](NetworkInterface.md)| The attribute map used to create the network interface. | [optional] 

### Return type

[**NetworkInterfaceResponse**](NetworkInterfaceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_network_interfaces**
> delete_network_interfaces(ids=ids, names=names)



Delete a network interface.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # delete a network interface with name myvip
        fb.network_interfaces.delete_network_interfaces(names=["myvip"])
    except rest.ApiException as e:
        print("Exception when deleting network interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_network_interfaces**
> NetworkInterfaceResponse list_network_interfaces(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List network interfaces.

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
        # list all network interfaces
        res = fb.network_interfaces.list_network_interfaces()
        # list and sort by name in descendant order
        res = fb.network_interfaces.list_network_interfaces(limit=5, sort="name-")
        # list with page size 5
        res = fb.network_interfaces.list_network_interfaces(limit=5)
        # list all remaining network interfaces
        res = fb.network_interfaces.list_network_interfaces(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.network_interfaces.list_network_interfaces(filter='contains(services, \'replication\')')
    except rest.ApiException as e:
        print("Exception when listing network interfaces: %s\n" % e)
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

[**NetworkInterfaceResponse**](NetworkInterfaceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_network_interfaces**
> NetworkInterfaceResponse update_network_interfaces(ids=ids, names=names, network_interface=network_interface)



Update an existing network interface.

### Example 
```python
from purity_fb import PurityFb, NetworkInterface, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Update the existing network interface "myvip"
        # Change the address to "1.2.3.201"
        # Change the service type to "replication"
        res = fb.network_interfaces.update_network_interfaces(
            names=['myvip'], network_interface=NetworkInterface(address='1.2.3.201', services=['replication']))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating network interface: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **network_interface** | [**NetworkInterface**](NetworkInterface.md)| The attribute map used to update the network interface. | [optional] 

### Return type

[**NetworkInterfaceResponse**](NetworkInterfaceResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

