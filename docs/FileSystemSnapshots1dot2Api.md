# purity_fb.FileSystemSnapshots1dot2Api

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_system_snapshots**](FileSystemSnapshots1dot2Api.md#create_file_system_snapshots) | **POST** /1.2/file-system-snapshots | 
[**delete_file_system_snapshots**](FileSystemSnapshots1dot2Api.md#delete_file_system_snapshots) | **DELETE** /1.2/file-system-snapshots | 
[**list_file_system_snapshots**](FileSystemSnapshots1dot2Api.md#list_file_system_snapshots) | **GET** /1.2/file-system-snapshots | 
[**update_file_system_snapshots**](FileSystemSnapshots1dot2Api.md#update_file_system_snapshots) | **PATCH** /1.2/file-system-snapshots | 


# **create_file_system_snapshots**
> FileSystemSnapshotResponse create_file_system_snapshots(sources, suffix=suffix)



Create snapshots for the specified source file systems

### Example 
```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthTokenHeader
purity_fb.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# purity_fb.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = purity_fb.FileSystemSnapshots1dot2Api()
sources = ['sources_example'] # list[str] | a list of names of source file systems
suffix = purity_fb.SnapshotSuffix() # SnapshotSuffix | the suffix of the snapshot (optional)

try: 
    api_response = api_instance.create_file_system_snapshots(sources, suffix=suffix)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemSnapshots1dot2Api->create_file_system_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sources** | [**list[str]**](str.md)| a list of names of source file systems | 
 **suffix** | [**SnapshotSuffix**](SnapshotSuffix.md)| the suffix of the snapshot | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_system_snapshots**
> delete_file_system_snapshots(name)



Delete a file system snapshot by name

### Example 
```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthTokenHeader
purity_fb.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# purity_fb.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = purity_fb.FileSystemSnapshots1dot2Api()
name = 'name_example' # str | name of the file system snapshot to be deleted

try: 
    api_instance.delete_file_system_snapshots(name)
except ApiException as e:
    print("Exception when calling FileSystemSnapshots1dot2Api->delete_file_system_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system snapshot to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_system_snapshots**
> FileSystemSnapshotResponse list_file_system_snapshots(filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only, names_or_sources=names_or_sources)



List file system snapshots

### Example 
```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthTokenHeader
purity_fb.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# purity_fb.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = purity_fb.FileSystemSnapshots1dot2Api()
filter = 'filter_example' # str | The filter to be used for query. (optional)
sort = 'sort_example' # str | The way to order the results. (optional)
start = 56 # int | start (optional)
limit = 56 # int | limit, should be >= 0 (optional)
token = 'token_example' # str | token (optional)
total = false # bool | return a total object in addition to the other results (optional) (default to false)
total_only = false # bool | return only the total object (optional) (default to false)
names_or_sources = ['names_or_sources_example'] # list[str] | a list of names of snapshots or source file systems (optional)

try: 
    api_response = api_instance.list_file_system_snapshots(filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only, names_or_sources=names_or_sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemSnapshots1dot2Api->list_file_system_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| The filter to be used for query. | [optional] 
 **sort** | **str**| The way to order the results. | [optional] 
 **start** | **int**| start | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **token** | **str**| token | [optional] 
 **total** | **bool**| return a total object in addition to the other results | [optional] [default to false]
 **total_only** | **bool**| return only the total object | [optional] [default to false]
 **names_or_sources** | [**list[str]**](str.md)| a list of names of snapshots or source file systems | [optional] 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_system_snapshots**
> FileSystemSnapshotResponse update_file_system_snapshots(name, attributes)



Update an existing file system snapshot

### Example 
```python
from __future__ import print_function
import time
import purity_fb
from purity_fb.rest import ApiException
from pprint import pprint

# Configure API key authorization: AuthTokenHeader
purity_fb.configuration.api_key['x-auth-token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# purity_fb.configuration.api_key_prefix['x-auth-token'] = 'Bearer'

# create an instance of the API class
api_instance = purity_fb.FileSystemSnapshots1dot2Api()
name = 'name_example' # str | the name of the file system snapshot to be updated
attributes = purity_fb.FileSystemSnapshot() # FileSystemSnapshot | the new attributes, only modifiable fields could be used.

try: 
    api_response = api_instance.update_file_system_snapshots(name, attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystemSnapshots1dot2Api->update_file_system_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the file system snapshot to be updated | 
 **attributes** | [**FileSystemSnapshot**](FileSystemSnapshot.md)| the new attributes, only modifiable fields could be used. | 

### Return type

[**FileSystemSnapshotResponse**](FileSystemSnapshotResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

