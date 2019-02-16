# purity_fb_1dot6.SubnetsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subnets**](SubnetsApi.md#create_subnets) | **POST** /1.6/subnets | 
[**delete_subnets**](SubnetsApi.md#delete_subnets) | **DELETE** /1.6/subnets | 
[**list_subnets**](SubnetsApi.md#list_subnets) | **GET** /1.6/subnets | 
[**update_subnets**](SubnetsApi.md#update_subnets) | **PATCH** /1.6/subnets | 


# **create_subnets**
> SubnetResponse create_subnets(names=names, subnet=subnet)



Create a new subnet

### Example 
```python
from purity_fb import PurityFb, rest, Subnet

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post the subnet object mysubnet on the array
        res = fb.subnets.create_subnets(names=["mysubnet"],
                                        subnet=Subnet(prefix='1.2.3.0/24'))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **subnet** | [**Subnet**](Subnet.md)| The attribute map used to create the subnet | [optional] 

### Return type

[**SubnetResponse**](SubnetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_subnets**
> delete_subnets(names=names)



Delete a subnet by name

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
        # delete a subnet with name myobjsubnet
        fb.subnets.delete_subnets(names=["myobjsubnet"])
    except rest.ApiException as e:
        print("Exception when deleting subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_subnets**
> SubnetResponse list_subnets(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token)



List subnets

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
        # list all subnets
        res = fb.subnets.list_subnets()
        # list and sort by name in descendant order
        res = fb.subnets.list_subnets(limit=5, sort="name-")
        # list with page size 5
        res = fb.subnets.list_subnets(limit=5)
        # list all remaining subnets
        res = fb.subnets.list_subnets(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.subnets.list_subnets(filter='vlan=8')
    except rest.ApiException as e:
        print("Exception when listing subnets: %s\n" % e)```

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

[**SubnetResponse**](SubnetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_subnets**
> SubnetResponse update_subnets(names=names, subnet=subnet)



Update an existing subnet

### Example 
```python
from purity_fb import PurityFb, rest, Subnet

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        res = fb.subnets.update_subnets(
            names=['myobjsubnet'], subnet=Subnet(gateway='1.2.3.1'))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating subnet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **subnet** | [**Subnet**](Subnet.md)| the attribute map used to update the subnet | [optional] 

### Return type

[**SubnetResponse**](SubnetResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

