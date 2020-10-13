# purity_fb_1dot10.SnmpAgentsApi

All URIs are relative to *https://purity_fb_server/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_snmp_agents**](SnmpAgentsApi.md#list_snmp_agents) | **GET** /1.10/snmp-agents | 
[**list_snmp_agents_mib**](SnmpAgentsApi.md#list_snmp_agents_mib) | **GET** /1.10/snmp-agents/mib | 
[**update_snmp_agents**](SnmpAgentsApi.md#update_snmp_agents) | **PATCH** /1.10/snmp-agents | 


# **list_snmp_agents**
> SnmpAgentResponse list_snmp_agents()



List SNMP agents.

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
        # list the array's snmp agents
        res = fb.snmp_agents.list_snmp_agents()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing snmp agents: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnmpAgentResponse**](SnmpAgentResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **list_snmp_agents_mib**
> SnmpAgentMibResponse list_snmp_agents_mib()



List the SNMP MIB text.

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
        # list the array's SNMP agent MIB
        res = fb.snmp_agents.list_snmp_agents_mib()
        print(res)
    except rest.ApiException as e:
        print("Exception when listing SNMP agent MIB: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnmpAgentMibResponse**](SnmpAgentMibResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

# **update_snmp_agents**
> SnmpAgentResponse update_snmp_agents(snmp_agent)



Update SNMP agents.

### Example 
```python
from purity_fb import PurityFb, rest, SnmpAgent, SnmpV2c, SnmpV3

fb = PurityFb("10.255.9.28", version=__version__)  # assume the array IP is 10.255.9.28
fb.disable_verify_ssl()
try:
    res = fb.login(API_TOKEN) # login to the array with your API_TOKEN
except rest.ApiException as e:
    print("Exception when logging in to the array: %s\n" % e)
if res:
    try:
        # update the snmp agent using snmpv2c to use snmpv3 with v3 attributes
        # there is only one snmp agent on the system
        new_v3_attrs = SnmpV3(auth_protocol='SHA', auth_passphrase='my-password-1!',
                              privacy_protocol='AES', privacy_passphrase='min8chars',
                              user='service-account-1')
        agent_v3_update_attrs = SnmpAgent(version='v3', v3=new_v3_attrs)
        # updating the agent to use v3 instead of v2c will automatically clear out v2c
        # attributes
        res = fb.snmp_agents.update_snmp_agents(snmp_agent=agent_v3_update_attrs)
        print(res)

        # update an snmp agent using snmpv3 to use snmpv2c with v2c attributes
        new_v2_attrs = SnmpV2c(community='community-for-informs-and-traps')
        agent_v2c_update_attrs = SnmpAgent(version='v2c', v2c=new_v2_attrs)
        # updating the agent to use v2c instead of v3 will automatically clear out v3
        # attributes
        res = fb.snmp_agents.update_snmp_agents(snmp_agent=agent_v2c_update_attrs)
        print(res)
    except rest.ApiException as e:
        print("Exception when updating snmp agent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snmp_agent** | [**SnmpAgent**](SnmpAgent.md)|  | 

### Return type

[**SnmpAgentResponse**](SnmpAgentResponse.md)

### Authorization

[AuthTokenHeader](index.md#AuthTokenHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](index.md#endpoint-properties) [[Back to Model list]](index.md#documentation-for-models) [[Back to Overview]](index.md)

