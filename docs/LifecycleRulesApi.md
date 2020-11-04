# purity_fb_1dot11.LifecycleRulesApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lifecycle_rules**](LifecycleRulesApi.md#create_lifecycle_rules) | **POST** /1.11/lifecycle-rules | 
[**delete_lifecycle_rules**](LifecycleRulesApi.md#delete_lifecycle_rules) | **DELETE** /1.11/lifecycle-rules | 
[**list_lifecycle_rules**](LifecycleRulesApi.md#list_lifecycle_rules) | **GET** /1.11/lifecycle-rules | 
[**update_lifecycle_rules**](LifecycleRulesApi.md#update_lifecycle_rules) | **PATCH** /1.11/lifecycle-rules | 


# **create_lifecycle_rules**
> LifecycleRuleResponse create_lifecycle_rules(rule)



Create a new object lifecycle rule for a specified bucket.

### Example 
```python
from purity_fb import PurityFb, rest, LifecycleRulePost, Reference

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # create a lifecycle rule 'myrule' for the bucket 'mybucket'.
        attr = LifecycleRulePost(bucket=Reference(name='mybucket'),
                                 rule_id='myrule',
                                 keep_previous_version_for=2*24*60*60*1000,
                                 prefix='myprefix')
        res = fb.lifecycle_rules.create_lifecycle_rules(rule=attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating lifecycle rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**LifecycleRulePost**](LifecycleRulePost.md)|  | 

### Return type

[**LifecycleRuleResponse**](LifecycleRuleResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_lifecycle_rules**
> delete_lifecycle_rules(bucket_ids=bucket_ids, bucket_names=bucket_names, names=names)



Delete an object lifecycle rule.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # Delete the lifecycle rule named 'oldrule' from bucket 'mybucket'
        res = fb.lifecycle_rules.delete_lifecycle_rules(names=['mybucket/oldrule'])
        print(res)
        # Delete all the lifecycle rules from bucket 'mybucket'
        res = fb.lifecycle_rules.delete_lifecycle_rules(bucket_names=['mybucket'])
        print(res)
        # Delete all the lifecycle rules from bucket with id '100abf42-0000-4000-8023-000det400090'
        res = fb.lifecycle_rules.delete_lifecycle_rules(bucket_ids=['100abf42-0000-4000-8023-000det400090'])
        print(res)
    except rest.ApiException as e:
        print('Exception when deleting lifecycle rule: %s\n' % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_ids** | **list[str]**| A comma-separated list of bucket IDs. If after filtering, there is not at least one resource that matches each of the elements of &#x60;bucket_ids&#x60;, then an error is returned. This cannot be provided together with the &#x60;bucket_names&#x60; query parameter. | [optional] 
 **bucket_names** | **list[str]**| A comma-separated list of bucket names. If there is not at least one resource that matches each of the elements of &#x60;bucket_names&#x60;, then an error is returned. This cannot be provided together with the &#x60;bucket_ids&#x60; query parameter. | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_lifecycle_rules**
> LifecycleRuleResponse list_lifecycle_rules(bucket_ids=bucket_ids, bucket_names=bucket_names, filter=filter, limit=limit, names=names, sort=sort, start=start, token=token)



List object lifecycle rules.

### Example 
```python
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # List all lifecycle rules
        res = fb.lifecycle_rules.list_lifecycle_rules()
        print(res)

        # List first two lifecycle rules in bucket 'mybucket'. Use default sorting.
        res = fb.lifecycle_rules.list_lifecycle_rules(limit=2, bucket_names=['mybucket'])
        print(res)

        # List the first lifecycle rule when sorting by prefix.
        res = fb.lifecycle_rules.list_lifecycle_rules(limit=1, sort='prefix')
        print(res)
    except rest.ApiException as e:
        print('Exception when listing lifecycle rules: %s\n' % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_ids** | **list[str]**| A comma-separated list of bucket IDs. If after filtering, there is not at least one resource that matches each of the elements of &#x60;bucket_ids&#x60;, then an error is returned. This cannot be provided together with the &#x60;bucket_names&#x60; query parameter. | [optional] 
 **bucket_names** | **list[str]**| A comma-separated list of bucket names. If there is not at least one resource that matches each of the elements of &#x60;bucket_names&#x60;, then an error is returned. This cannot be provided together with the &#x60;bucket_ids&#x60; query parameter. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**LifecycleRuleResponse**](LifecycleRuleResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_lifecycle_rules**
> LifecycleRuleResponse update_lifecycle_rules(rule, names=names)



Modify an object lifecycle rule.

### Example 
```python
from purity_fb import PurityFb, rest, LifecycleRulePatch, Reference

fb = PurityFb('10.255.9.28', version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print('Exception when logging in to the array: %s\n' % e)
if res:
    try:
        # modify the lifecycle rule 'myrule' for the bucket 'mybucket'.
        attr = LifecycleRulePatch(enabled=True,
                                  keep_previous_version_for=7*24*60*60*1000,
                                  prefix='mynewprefix')
        res = fb.lifecycle_rules.update_lifecycle_rules(names=['mybucket/myrule'], rule=attr)
        print(res)
    except rest.ApiException as e:
        print('Exception when updating lifecycle rule: %s\n' % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule** | [**LifecycleRulePatch**](LifecycleRulePatch.md)|  | 
 **names** | **list[str]**| A comma-separated list of resource names. This cannot be provided together with the ids query parameters. | [optional] 

### Return type

[**LifecycleRuleResponse**](LifecycleRuleResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

