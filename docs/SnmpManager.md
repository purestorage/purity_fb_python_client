# SnmpManager

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object | [optional] 
**id** | **str** | A unique ID chosen by the system. Cannot change. | [optional] 
**host** | **str** | DNS hostname or IP address of a computer that hosts an SNMP manager to which Purity is to send trap messages when it generates alerts. | [optional] 
**notification** | **str** | The type of notification the agent will send. Valid values are &#x60;inform&#x60; and &#x60;trap&#x60;. | [optional] 
**version** | **str** | Version of the SNMP protocol to be used by Purity in communications with the specified manager. Valid values are &#x60;v2c&#x60; and &#x60;v3&#x60;. | [optional] 
**v2c** | [**SnmpV2c**](SnmpV2c.md) |  | [optional] 
**v3** | [**SnmpV3**](SnmpV3.md) |  | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


