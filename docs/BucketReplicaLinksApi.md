# purity_fb_1dot12.BucketReplicaLinksApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bucket_replica_links**](BucketReplicaLinksApi.md#create_bucket_replica_links) | **POST** /1.12/bucket-replica-links | 
[**delete_bucket_replica_links**](BucketReplicaLinksApi.md#delete_bucket_replica_links) | **DELETE** /1.12/bucket-replica-links | 
[**list_bucket_replica_links**](BucketReplicaLinksApi.md#list_bucket_replica_links) | **GET** /1.12/bucket-replica-links | 
[**update_bucket_replica_links**](BucketReplicaLinksApi.md#update_bucket_replica_links) | **PATCH** /1.12/bucket-replica-links | 


# **create_bucket_replica_links**
> BucketReplicaLinkResponse create_bucket_replica_links(bucket_replica_link, local_bucket_names=local_bucket_names, remote_bucket_names=remote_bucket_names, remote_credentials_names=remote_credentials_names)



Create new bucket replica links.

### Example 
```python
from purity_fb import PurityFb, BucketReplicaLink, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # create a replica link from a specified local bucket, to a specified remote bucket
    # on the remote corresponding to the remote credentials
    local_bucket_names = ["localbucket"]
    remote_bucket_names = ["remotebucket"]
    remote_credentials_names = ["remote/credentials"]
    my_replica_link = BucketReplicaLink(paused=False)
    try:
        # post the bucket replica link object on the local array
        res = fb.bucket_replica_links.create_bucket_replica_links(local_bucket_names=local_bucket_names,
                                                                  remote_bucket_names=remote_bucket_names,
                                                                  remote_credentials_names=remote_credentials_names,
                                                                  bucket_replica_link=my_replica_link)
        print(res)
    except rest.ApiException as e:
        print("Exception when creating creating bucket replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_replica_link** | [**BucketReplicaLinkPost**](BucketReplicaLinkPost.md)| Bucket replica link create parameters. | 
 **local_bucket_names** | **list[str]**| A comma-separated list of local bucket names. This cannot be provided together with &#x60;local_bucket_ids&#x60; query parameter. | [optional] 
 **remote_bucket_names** | **list[str]**| A comma-separated list of remote bucket names. | [optional] 
 **remote_credentials_names** | **list[str]**| A comma-separated list of remote credentials names. | [optional] 

### Return type

[**BucketReplicaLinkResponse**](BucketReplicaLinkResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **delete_bucket_replica_links**
> delete_bucket_replica_links(local_bucket_ids=local_bucket_ids, local_bucket_names=local_bucket_names, remote_bucket_names=remote_bucket_names, remote_ids=remote_ids, remote_names=remote_names)



Delete a bucket replica link.

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
        # delete the replica link on the local bucket with the name 'my-connected-array'
        fb.bucket_replica_links.delete_bucket_replica_links(local_bucket_names=['localbucket'],
                                                            remote_bucket_names=['remotebucket'],
                                                            remote_names=['my-connected-array'])

        # delete the replica link on the local bucket with id '10314f42-020d-7080-8013-000ddt400090'
        fb.bucket_replica_links.delete_bucket_replica_links(local_bucket_ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                            remote_bucket_names=['remotebucket'],
                                                            remote_ids=['10314f42-020d-7080-8013-000ddt400012'])
    except rest.ApiException as e:
        print("Exception when deleting replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_bucket_ids** | **list[str]**| A comma-separated list of local bucket IDs. This cannot be provided together with the &#x60;local_bucket_names&#x60; query parameter. | [optional] 
 **local_bucket_names** | **list[str]**| A comma-separated list of local bucket names. This cannot be provided together with &#x60;local_bucket_ids&#x60; query parameter. | [optional] 
 **remote_bucket_names** | **list[str]**| A comma-separated list of remote bucket names. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

void (empty response body)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_bucket_replica_links**
> BucketReplicaLinkResponse list_bucket_replica_links(ids=ids, filter=filter, limit=limit, local_bucket_ids=local_bucket_ids, local_bucket_names=local_bucket_names, remote_bucket_names=remote_bucket_names, remote_ids=remote_ids, remote_names=remote_names, sort=sort, start=start, token=token)



List bucket replica links.

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
        # list all replica links
        fb.bucket_replica_links.list_bucket_replica_links()
        # list first five replica links using default sort
        res = fb.bucket_replica_links.list_bucket_replica_links(limit=5)
        print(res)
        # list first five replica links and sort by remote
        res = fb.bucket_replica_links.list_bucket_replica_links(limit=5, sort='remote')
        print(res)
        # list replica links on the remote 's3target'
        res = fb.bucket_replica_links.list_bucket_replica_links(remote_names=['s3target'])
        print(res)
        # list all remaining replica links
        res = fb.bucket_replica_links.list_bucket_replica_links(token=res.pagination_info.continuation_token)
        print(res)
        # list with filter to see only replica links that are paused
        res = fb.bucket_replica_links.list_bucket_replica_links(filter='paused')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing replica links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **list[str]**| A comma-separated list of resource IDs. This cannot be provided together with the name or names query parameters. | [optional] 
 **filter** | **str**| The filter to be used for query. | [optional] 
 **limit** | **int**| limit, should be &gt;&#x3D; 0 | [optional] 
 **local_bucket_ids** | **list[str]**| A comma-separated list of local bucket IDs. This cannot be provided together with the &#x60;local_bucket_names&#x60; query parameter. | [optional] 
 **local_bucket_names** | **list[str]**| A comma-separated list of local bucket names. This cannot be provided together with &#x60;local_bucket_ids&#x60; query parameter. | [optional] 
 **remote_bucket_names** | **list[str]**| A comma-separated list of remote bucket names. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 
 **sort** | **str**| Sort the response by the specified fields (in descending order if &#39;-&#39; is appended to the field name). | [optional] 
 **start** | **int**| The offset of the first resource to return from a collection. | [optional] 
 **token** | **str**| An opaque token used to iterate over a collection. The token to use on the next request is returned in the &#x60;continuation_token&#x60; field of the result. | [optional] 

### Return type

[**BucketReplicaLinkResponse**](BucketReplicaLinkResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_bucket_replica_links**
> BucketReplicaLinkResponse update_bucket_replica_links(bucket_replica_link, local_bucket_ids=local_bucket_ids, local_bucket_names=local_bucket_names, remote_bucket_names=remote_bucket_names, remote_ids=remote_ids, remote_names=remote_names)



Update bucket replica links.

### Example 
```python
from purity_fb import PurityFb, BucketReplicaLink, ObjectStoreRemoteCredentials, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    # Pause an existing bucket replica link
    # Also change the remote credentials we're using for replication to the credentials named "remote/name"
    new_attr = BucketReplicaLink(paused=True, remote_credentials=ObjectStoreRemoteCredentials(name="remote/name"))
    try:
        # Update the existing replica link on the specified local bucket, to the specified remote bucket on the remote
        # Use the attribute map from before to pause the link and change credentials
        res = fb.bucket_replica_links.update_bucket_replica_links(local_bucket_names=['localbucket'],
                                                                  remote_names=['remote'],
                                                                  remote_bucket_names=['remotebucket'],
                                                                  bucket_replica_link=new_attr)
        print(res)

        # Update the existing replica link on the specified local bucket, to the specified remote bucket on the remote (by ids)
        # Use the attribute map from before to pause the link and change credentials
        res = fb.bucket_replica_links.update_bucket_replica_links(local_bucket_ids=['10314f42-020d-7080-8013-000ddt400090'],
                                                                  remote_ids=['10314f42-020d-7080-8013-000ddt400045'],
                                                                  remote_bucket_names=['remotebucket'],
                                                                  bucket_replica_link=new_attr)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating replica link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_replica_link** | [**BucketReplicaLink**](BucketReplicaLink.md)| The attribute map used to update the bucket replica link. | 
 **local_bucket_ids** | **list[str]**| A comma-separated list of local bucket IDs. This cannot be provided together with the &#x60;local_bucket_names&#x60; query parameter. | [optional] 
 **local_bucket_names** | **list[str]**| A comma-separated list of local bucket names. This cannot be provided together with &#x60;local_bucket_ids&#x60; query parameter. | [optional] 
 **remote_bucket_names** | **list[str]**| A comma-separated list of remote bucket names. | [optional] 
 **remote_ids** | **list[str]**| A comma-separated list of remote array IDs. This cannot be provided together with the &#x60;remote_names&#x60; query parameter. | [optional] 
 **remote_names** | **list[str]**| A comma-separated list of remote array names. This cannot be provided together with &#x60;remote_ids&#x60; query parameter. | [optional] 

### Return type

[**BucketReplicaLinkResponse**](BucketReplicaLinkResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

