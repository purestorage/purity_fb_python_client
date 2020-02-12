# purity_fb_1dot9.ArrayConnectionsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_array_connections**](ArrayConnectionsApi.md#create_array_connections) | **POST** /1.9/array-connections | 
[**create_array_connections_connection_keys**](ArrayConnectionsApi.md#create_array_connections_connection_keys) | **POST** /1.9/array-connections/connection-key | 
[**delete_array_connections**](ArrayConnectionsApi.md#delete_array_connections) | **DELETE** /1.9/array-connections | 
[**list_array_connections**](ArrayConnectionsApi.md#list_array_connections) | **GET** /1.9/array-connections | 
[**list_array_connections_connection_keys**](ArrayConnectionsApi.md#list_array_connections_connection_keys) | **GET** /1.9/array-connections/connection-key | 
[**list_array_connections_paths**](ArrayConnectionsApi.md#list_array_connections_paths) | **GET** /1.9/array-connections/path | 
[**list_array_connections_performance_replication**](ArrayConnectionsApi.md#list_array_connections_performance_replication) | **GET** /1.9/array-connections/performance/replication | 
[**update_array_connections**](ArrayConnectionsApi.md#update_array_connections) | **PATCH** /1.9/array-connections | 


# **create_array_connections**
> ArrayConnectionResponse create_array_connections(array_connection)



Create a new array connection.

### Example 
```python
from purity_fb import PurityFb, ArrayConnection, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # connect to an array with specified hostname, using a provided connection key
    hostname = "https://my.array.com"
    connection_key = "6207d123-d123-0b5c-5fa1-95fabc5c7123"
    myAC = ArrayConnection(management_address=hostname, connection_key=connection_key)
    try:
        # post the array connection object on the array we're connection from
        res = fb.array_connections.create_array_connections(array_connection=myAC)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating array connection: %s\n" % e)

    # connect to an array by ip address and specifying replication addresses, using a provided connection key
    mgmt_addr = "10.202.101.78"
    repl_addr = ["10.202.101.70"]
    connection_key = "6207d123-d123-0b5c-5fa1-95fabc5c7123"
    myAC = ArrayConnection(management_address=mgmt_addr, replication_addresses=repl_addr, connection_key=connection_key)
    try:
        # post the array connection object on the array we're connection from
        res = fb.array_connections.create_array_connections(array_connection=myAC)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating array connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **array_connection** | [**ArrayConnectionPost**](ArrayConnectionPost.md)| The attribute map used to create the array connection. | 

### Return type

[**ArrayConnectionResponse**](ArrayConnectionResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **create_array_connections_connection_keys**
> ArrayConnectionKeyResponse create_array_connections_connection_keys()



Create a new array connection key.

### Example 
```python
from purity_fb import PurityFb, ArrayConnectionKey, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # post to the array-connections/connection-key endpoint to get a connection key
        res = fb.array_connections.create_array_connections_connection_keys()
        print(res)
    except rest.ApiException as e:
        print("Exception when creating array connection key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayConnectionKeyResponse**](ArrayConnectionKeyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_array_connections**
> delete_array_connections(name, ids=ids)



Delete an array connection.

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
        # delete the keytab with the name 'my-connected-array'
        fb.array_connections.delete_array_connections(names=['my-connected-array'])

        # delete the array connection with id '10314f42-020d-7080-8013-000ddt400090'
        fb.array_connections.delete_array_connections(ids=['10314f42-020d-7080-8013-000ddt400090'])
    except rest.ApiException as e:
        print("Exception when deleting array connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file system or snapshot to be updated. | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_array_connections**
> ArrayConnectionResponse list_array_connections(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List array connections.

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
        # list all array connections
        fb.array_connections.list_array_connections()
        # list first five array connections using default sort
        res = fb.array_connections.list_array_connections(limit=5)
        print(res)
        # list first five array connections and sort by source in descendant order
        res = fb.array_connections.list_array_connections(limit=5, sort="version-")
        print(res)
        # list all remaining array connections
        res = fb.array_connections.list_array_connections(token=res.pagination_info.continuation_token)
        # list with filter to see only array connections on a specified version
        res = fb.array_connections.list_array_connections(filter='version=\'3.*\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing array connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**ArrayConnectionResponse**](ArrayConnectionResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_array_connections_connection_keys**
> ArrayConnectionKeyResponse list_array_connections_connection_keys()



List array connection keys.

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
        # list all connection keys
        res = fb.array_connections.list_array_connections_connection_keys()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing array connection key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ArrayConnectionKeyResponse**](ArrayConnectionKeyResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_array_connections_paths**
> ArrayConnectionPathResponse list_array_connections_paths(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List array connection paths.

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
        # list all array connection paths
        fb.array_connections.list_array_connections_paths()
        # list first five array connection paths using default sort
        res = fb.array_connections.list_array_connections_paths(limit=5)
        print(res)
        # list first five array connection paths and sort by source in descendant order
        res = fb.array_connections.list_array_connections_paths(limit=5, sort="source-")
        print(res)
        # list all remaining array connection paths
        res = fb.array_connections.list_array_connections_paths(token=res.pagination_info.continuation_token)
        # list with filter to see only array connection paths from a specified source ip
        res = fb.array_connections.list_array_connections_paths(filter='source=\'10.202.101.70\'')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing array connection paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **token** | **str**| token | [optional] 

### Return type

[**ArrayConnectionPathResponse**](ArrayConnectionPathResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_array_connections_performance_replication**
> RelationshipPerformanceReplicationResponse list_array_connections_performance_replication(end_time=end_time, filter=filter, ids=ids, limit=limit, names=names, resolution=resolution, sort=sort, start=start, start_time=start_time, token=token, total_only=total_only, type=type)



List instant or historical array connection replication specific performance.

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
        # list instantaneous replication performance for all array connections
        res = fb.array_connections.list_array_connections_performance_replication()
        print(res)

        # list instantaneous file-replication performance for all array connections
        res = fb.array_connections.list_array_connections_performance_replication(type='file-system')
        print(res)

        # list instantaneous file-replication performance for array connection with id '10314f42-020d-7080-8013-000ddt400090'
        res = fb.array_connections.list_array_connections_performance_replication(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                                                  type='file-system')
        print(res)

        # list historical object-replication performance for all array connections between some
        # start time and end time
        res = fb.array_connections.list_array_connections_performance_replication(
            start_time=START_TIME,
            end_time=END_TIME,
            type='object-store',
            resolution=30000)
        print(res)

        # list historical object-replication performance for array connection 'remote_array' between some
        # start time and end time
        res = fb.array_connections.list_array_connections_performance_replication(
            start_time=START_TIME,
            end_time=END_TIME,
            resolution=30000,
            type='object-store',
            names=['remote_array'])
        print(res)
    except rest.ApiException as e:
        print("Exception when listing array connection replication performance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_time** | **int**| Time to end sample in milliseconds since epoch. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **resolution** | **int**| sample frequency in milliseconds | [optional] [default to 30000]
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **start_time** | **int**| Time to start sample in milliseconds since epoch. | [optional] 
 **token** | **str**| token | [optional] 
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **type** | **str**| to sample space of either file systems, object store, or all | [optional] 

### Return type

[**RelationshipPerformanceReplicationResponse**](RelationshipPerformanceReplicationResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_array_connections**
> ArrayConnectionResponse update_array_connections(name, array_connection, ids=ids)



Update an existing array connection.

### Example 
```python
from purity_fb import PurityFb, ArrayConnection, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # Update the management and replication addresses of an array connection
    new_attr = ArrayConnection(management_address="10.202.101.70",
                               replication_addresses=["10.202.101.71", "10.202.101.72"])
    try:
        # update the array connection named otherarray
        res = fb.array_connections.update_array_connections(names=["otherarray"], array_connection=new_attr)
        print(res)

        # update the array connection with id '10314f42-020d-7080-8013-000ddt400090'
        res = fb.array_connections.update_array_connections(ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                            array_connection=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating array connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the file system or snapshot to be updated. | 
 **array_connection** | [**ArrayConnection**](ArrayConnection.md)| The attribute map used to update the array connection. | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 

### Return type

[**ArrayConnectionResponse**](ArrayConnectionResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

