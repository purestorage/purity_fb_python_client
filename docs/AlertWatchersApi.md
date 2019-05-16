# purity_fb_1dot8.AlertWatchersApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_watchers**](AlertWatchersApi.md#create_alert_watchers) | **POST** /1.8/alert-watchers | 
[**delete_alert_watchers**](AlertWatchersApi.md#delete_alert_watchers) | **DELETE** /1.8/alert-watchers | 
[**list_alert_watchers**](AlertWatchersApi.md#list_alert_watchers) | **GET** /1.8/alert-watchers | 
[**test_alert_watchers**](AlertWatchersApi.md#test_alert_watchers) | **GET** /1.8/alert-watchers/test | 
[**update_alert_watchers**](AlertWatchersApi.md#update_alert_watchers) | **PATCH** /1.8/alert-watchers | 


# **create_alert_watchers**
> AlertWatcherResponse create_alert_watchers(names=names)



Create alert watchers.

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
        # create an alert watcher with a given email address
        res = fb.alert_watchers.create_alert_watchers(names=['test@example.com'])
        print(res)
    except rest.ApiException as e:
        print("Exception when creating alert watchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**AlertWatcherResponse**](AlertWatcherResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_alert_watchers**
> delete_alert_watchers(names=names)



Delete alert watchers.

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
        # delete an alert watcher with a given email address
        res = fb.alert_watchers.delete_alert_watchers(names=['test@example.com'])
        print(res)
    except rest.ApiException as e:
        print("Exception when deleting alert watchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_alert_watchers**
> AlertWatcherResponse list_alert_watchers(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token)



List alert watchers.

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
        # create an alert watcher with a given email address
        res = fb.alert_watchers.list_alert_watchers(
            names=['*@example.com', '*@test.com'], sort='name-')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing alert watchers: %s\n" % e)
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

[**AlertWatcherResponse**](AlertWatcherResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **test_alert_watchers**
> AlertWatcherTestResponse test_alert_watchers(names=names)



Test alert watchers

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
        # test alert watchers with given email addresses
        res = fb.alert_watchers.test_alert_watchers(
            names=['test1@example.com', 'test2@example.com'])
        print(res)
    except rest.ApiException as e:
        print("Exception when testing alert watchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**AlertWatcherTestResponse**](AlertWatcherTestResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_alert_watchers**
> AlertWatcherResponse update_alert_watchers(watcher_settings, ids=ids, names=names)



Update alert watchers.

### Example 
```python
from purity_fb import PurityFb, AlertWatcher, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    watcher_settings = AlertWatcher(enabled=False)
    try:
        # disable an alert watcher with a given email address
        res = fb.alert_watchers.update_alert_watchers(
            names=['test@example.com'], watcher_settings=watcher_settings)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating alert watchers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **watcher_settings** | [**AlertWatcher**](AlertWatcher.md)|  | 
 **ids** | [**list[str]**](str.md)| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **names** | [**list[str]**](str.md)| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**AlertWatcherResponse**](AlertWatcherResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

