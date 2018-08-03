# purity_fb_1dot4.LinkAggregationGroupsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_link_aggregation_groups**](LinkAggregationGroupsApi.md#create_link_aggregation_groups) | **POST** /1.4/link-aggregation-groups | 
[**delete_link_aggregation_groups**](LinkAggregationGroupsApi.md#delete_link_aggregation_groups) | **DELETE** /1.4/link-aggregation-groups | 
[**list_link_aggregation_groups**](LinkAggregationGroupsApi.md#list_link_aggregation_groups) | **GET** /1.4/link-aggregation-groups | 
[**update_link_aggregation_groups**](LinkAggregationGroupsApi.md#update_link_aggregation_groups) | **PATCH** /1.4/link-aggregation-groups | 


# **create_link_aggregation_groups**
> LinkAggregationGroupResponse create_link_aggregation_groups(link_aggregation_group=link_aggregation_group, names=names)



Create a new link aggregation group

### Example 
```python
from purity_fb import PurityFb, rest, LinkAggregationGroup

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN)  # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create lag named "mylag" with ports 'CH1.FM1.ETH4' and 'CH1.FM2.ETH4'
        res = fb.link_aggregation_groups.create_link_aggregation_groups(
            names=["mylag"],
            link_aggregation_group=LinkAggregationGroup(ports=[{'name': 'CH1.FM1.ETH4'}, {'name': 'CH1.FM2.ETH4'}]))
        print(res)
    except rest.ApiException as e:
        print("Exception when creating link aggregation group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_aggregation_group** | [**LinkAggregationGroup**](LinkAggregationGroup.md)| The attribute map used to create the link aggregation group | [optional] 
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 

### Return type

[**LinkAggregationGroupResponse**](LinkAggregationGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_link_aggregation_groups**
> delete_link_aggregation_groups(names=names)



Delete a link aggregation group by name

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
        # delete a link aggregation group with name mylag
        fb.link_aggregation_groups.delete_link_aggregation_groups(names=["mylag"])
    except rest.ApiException as e:
        print("Exception when deleting link aggregation group: %s\n" % e)
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

# **list_link_aggregation_groups**
> LinkAggregationGroupResponse list_link_aggregation_groups(filter=filter, sort=sort, start=start, limit=limit, token=token, names=names)



List link aggregation groups

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
        # list all link aggregation groups
        res = fb.link_aggregation_groups.list_link_aggregation_groups()
        # list and sort by name in descendant order
        res = fb.link_aggregation_groups.list_link_aggregation_groups(limit=5, sort="name-")
        # list with page size 5
        res = fb.link_aggregation_groups.list_link_aggregation_groups(limit=5)
        # list all remaining link aggregation groups
        res = fb.link_aggregation_groups.list_link_aggregation_groups(token=res.pagination_info.continuation_token)
        # list with filter
        res = fb.link_aggregation_groups.list_link_aggregation_groups(filter="mac_address=24:a9:37:11:f5:21")
    except rest.ApiException as e:
        print("Exception when listing link aggregation groups: %s\n" % e)```

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

[**LinkAggregationGroupResponse**](LinkAggregationGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_link_aggregation_groups**
> LinkAggregationGroupResponse update_link_aggregation_groups(names=names, link_aggregation_group=link_aggregation_group)



Update an existing link aggregation group

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
        res = fb.link_aggregation_groups.update_link_aggregation_groups(
            names=["mylag"], link_aggregation_group=LinkAggregationGroup(
                ports=[{"name": "CH1.FM1.ETH4"}, {"name": "CH1.FM2.ETH4"}]))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating link aggregation group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A list of names. | [optional] 
 **link_aggregation_group** | [**Linkaggregationgroup**](Linkaggregationgroup.md)| the attribute map used to update the link aggregation group | [optional] 

### Return type

[**LinkAggregationGroupResponse**](LinkAggregationGroupResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

