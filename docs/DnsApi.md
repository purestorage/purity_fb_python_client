# purity_fb_1dot9.DnsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_dns**](DnsApi.md#list_dns) | **GET** /1.9/dns | 
[**update_dns**](DnsApi.md#update_dns) | **PATCH** /1.9/dns | 


# **list_dns**
> DnsResponse list_dns()



list DNS configuration

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
        # list DNS configuration
        res = fb.dns.list_dns()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing DNS configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DnsResponse**](DnsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_dns**
> DnsResponse update_dns(dns_settings)



update DNS configuration

### Example 
```python
from purity_fb import PurityFb, Dns, rest

fb = PurityFb("10.255.9.28") # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update domain
        res = fb.dns.update_dns(dns_settings=Dns(domain='new_domain'))
        print(res)
        # update nameservers
        res = fb.dns.update_dns(dns_settings=Dns(nameservers=['126.24.5.1', '126.24.5.2']))
        print(res)
        # empty nameservers
        res = fb.dns.update_dns(dns_settings=Dns(nameservers=[]))
        print(res)
    except rest.ApiException as e:
        print("Exception when updating DNS configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_settings** | [**Dns**](Dns.md)| the new DNS configuration | 

### Return type

[**DnsResponse**](DnsResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

