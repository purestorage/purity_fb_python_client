# purity_fb.FileSystems1dot2Api

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_systems**](FileSystems1dot2Api.md#create_file_systems) | **POST** /1.2/file-systems | 
[**delete_file_systems**](FileSystems1dot2Api.md#delete_file_systems) | **DELETE** /1.2/file-systems | 
[**list_file_systems**](FileSystems1dot2Api.md#list_file_systems) | **GET** /1.2/file-systems | 
[**update_file_systems**](FileSystems1dot2Api.md#update_file_systems) | **PATCH** /1.2/file-systems | 


# **create_file_systems**
> FileSystemResponse create_file_systems(file_system)



Create a new file system

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
api_instance = purity_fb.FileSystems1dot2Api()
file_system = purity_fb.FileSystem() # FileSystem | the attribute map used to create the file system

try: 
    api_response = api_instance.create_file_systems(file_system)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystems1dot2Api->create_file_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_system** | [**FileSystem**](FileSystem.md)| the attribute map used to create the file system | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_file_systems**
> delete_file_systems(name)



Delete a file system by name

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
api_instance = purity_fb.FileSystems1dot2Api()
name = 'name_example' # str | name of the file system to be deleted

try: 
    api_instance.delete_file_systems(name)
except ApiException as e:
    print("Exception when calling FileSystems1dot2Api->delete_file_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| name of the file system to be deleted | 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_file_systems**
> FileSystemResponse list_file_systems(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)



List file systems

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
api_instance = purity_fb.FileSystems1dot2Api()
names = ['names_example'] # list[str] | A list of names. (optional)
filter = 'filter_example' # str | The filter to be used for query. (optional)
sort = 'sort_example' # str | The way to order the results. (optional)
start = 56 # int | start (optional)
limit = 56 # int | limit, should be >= 0 (optional)
token = 'token_example' # str | token (optional)
total = false # bool | return a total object in addition to the other results (optional) (default to false)
total_only = false # bool | return only the total object (optional) (default to false)

try: 
    api_response = api_instance.list_file_systems(names=names, filter=filter, sort=sort, start=start, limit=limit, token=token, total=total, total_only=total_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystems1dot2Api->list_file_systems: %s\n" % e)
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
 **total** | **bool**| return a total object in addition to the other results | [optional] [default to false]
 **total_only** | **bool**| return only the total object | [optional] [default to false]

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_file_systems**
> FileSystemResponse update_file_systems(name, attributes)



Update an existing file system

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
api_instance = purity_fb.FileSystems1dot2Api()
name = 'name_example' # str | the name of the file system to be updated
attributes = purity_fb.FileSystem() # FileSystem | the new attributes, only modifiable fields could be used.

try: 
    api_response = api_instance.update_file_systems(name, attributes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileSystems1dot2Api->update_file_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| the name of the file system to be updated | 
 **attributes** | [**FileSystem**](FileSystem.md)| the new attributes, only modifiable fields could be used. | 

### Return type

[**FileSystemResponse**](FileSystemResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

