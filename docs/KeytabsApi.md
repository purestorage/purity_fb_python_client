# purity_fb_1dot11.KeytabsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_keytabs**](KeytabsApi.md#delete_keytabs) | **DELETE** /1.11/keytabs | 
[**download_keytab_file**](KeytabsApi.md#download_keytab_file) | **GET** /1.11/keytabs/download | 
[**list_keytabs**](KeytabsApi.md#list_keytabs) | **GET** /1.11/keytabs | 
[**upload_keytab_file**](KeytabsApi.md#upload_keytab_file) | **POST** /1.11/keytabs/upload | 


# **delete_keytabs**
> delete_keytabs(ids=ids, names=names)



Delete a keytab.

### Example 
```python
from purity_fb import PurityFb, Keytab, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # delete the keytab with the name 'oldkeytab.1'
        fb.keytabs.delete_keytabs(names=['oldkeytab.1'])

        # delete the keytab with id '10314f42-020d-7080-8013-000ddt400090'
        fb.keytabs.delete_keytabs(ids=['10314f42-020d-7080-8013-000ddt400090'])

        # delete all keytabs that were encrypted with older aes128 ciphers
        res = fb.keytabs.list_keytabs(filter='contains(encryption_type, "aes128")')
        print(res)
        for keytab in res.items:
            name_to_delete = keytab.name
            fb.keytabs.delete_keytabs(names=[name_to_delete])
    except rest.ApiException as e:
        print("Exception when deleting keytabs: %s\n" % e)
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

# **download_keytab_file**
> KeytabDownloadUploadResponse download_keytab_file(keytab_ids=keytab_ids, keytab_names=keytab_names)



Download a keytab file.

### Example 
```python
import codecs
from purity_fb import PurityFb, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all keytabs on the system as a single file
        res = fb.keytabs.list_keytab_files()
        print(res)

        # export all keytabs on the system with a certain encryption type, and write their binary
        # to a file
        desired_encryption_type = 'aes256-cts-hmac-sha1-96'
        filter_str = 'encryption_type="{}"'.format(desired_encryption_type)
        res = fb.keytabs.list_keytabs(filter=filter_str)
        # get the names from our results
        names_to_export = []
        for keytab_entry_obj in res.items:
            names_to_export.append(keytab_entry_obj.name)

        # download file composed of the keytabs we gathered, encoded in binary
        keytab_file_contents = fb.keytabs.download_keytab_file(keytab_names=names_to_export)
        # unlike our json-based apis, our file apis return file contents, rather than a json
        # object model. so we then just write the contents to our keytab file

        # write the binary data to your keytab file
        with open('/etc/krb5.keytab', 'wb') as my_keytab_file:
            my_keytab_file.write(keytab_file_contents)
    except rest.ApiException as e:
        print("Exception when downloading keytabs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keytab_ids** | **list[str]**| A comma-separated list of keytab ids. This cannot be provided together with the keytab names query parameters. | [optional] 
 **keytab_names** | **list[str]**| A comma-separated list of keytab names. This cannot be provided together with the keytab ids query parameters. | [optional] 

### Return type

[**KeytabDownloadUploadResponse**](KeytabDownloadUploadResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, text/plain, application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_keytabs**
> KeytabResponse list_keytabs(filter=filter, ids=ids, limit=limit, names=names, sort=sort, start=start, token=token, total_only=total_only, total=total)



List keytabs.

### Example 
```python
from purity_fb import PurityFb, Keytab, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # list all keytabs on the system
        res = fb.keytabs.list_keytabs()
        print(res)

        # list first five keytabs using default sort. only looking for ones beginning with 'kt1.'
        res = fb.keytabs.list_keytabs(limit=5, names=["kt1.*"])
        print(res)

        # list first five keytabs, sorting by the key version number used to generate them
        res = fb.keytabs.list_keytabs(limit=5, sort="kvno")
        print(res)

        # list all keytabs, filtering only for keytabs with aes256 in their encryption type
        res = fb.keytabs.list_keytabs(filter='contains(encryption_type, "aes256")')
        print(res)
    except rest.ApiException as e:
        print("Exception when listing keytabs: %s\n" % e)
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
 **total_only** | **bool**| Return only the total object. | [optional] [default to false]
 **total** | **bool**| Return a total object in addition to the other results. | [optional] [default to false]

### Return type

[**KeytabResponse**](KeytabResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **upload_keytab_file**
> KeytabDownloadUploadResponse upload_keytab_file(keytab_file, name_prefixes=name_prefixes)



Upload a keytab file.

### Example 
```python
import codecs
from purity_fb import PurityFb, Keytab, rest

fb = PurityFb("10.255.9.28", version=__version__) # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # read the binary data from your keytab file
        with open('/etc/krb5.keytab', 'rb') as binary_keytab_file:
            my_binary_keytab_data = binary_keytab_file.read()

        # upload the binary data. we use a tuple of (filename, file contents) as the keytab file to
        # upload in order to be generically compatible across different python versions
        res = fb.keytabs.upload_keytab_file(name_prefixes=['binary-uploaded-krb5'],
                                            keytab_file=('krb5.keytab', my_binary_keytab_data))
        # our result is the contents of the file we just uploaded
        print(res)

        # we can also upload a base64 encoded keytab file, in case we were sent a keytab
        # through some medium where binary wasn't feasible (e.g. copied into a bash terminal,
        # sent as text over an internal corporate messaging system)
        with open('/etc/krb5.txt', 'r') as base64_keytab_file:
            my_base64_keytab_data = base64_keytab_file.read()

        res = fb.keytabs.upload_keytab_file(name_prefixes=['base64-uploaded-krb5'],
                                            keytab_file=('krb5.txt', my_base64_keytab_data))
        # our result is the contents of the file we just uploaded
        print(res)
    except rest.ApiException as e:
        print("Exception when uploading keytab files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keytab_file** | **str**| The attribute map containing the data of the file of keytabs being imported. | 
 **name_prefixes** | **list[str]**| The prefix to use for the names of all kerberos keytab entry objects that are being created. | [optional] 

### Return type

[**KeytabDownloadUploadResponse**](KeytabDownloadUploadResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream, text/plain, application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

