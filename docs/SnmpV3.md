# SnmpV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_passphrase** | **str** | Passphrase used by Purity to authenticate the array with the specified managers. | [optional] 
**auth_protocol** | **str** | Hash algorithm used to validate the authentication passphrase. Valid values are &#x60;MD5&#x60; and &#x60;SHA&#x60;. | [optional] 
**privacy_passphrase** | **str** | Passphrase used to encrypt SNMP messages. A passphrase must be at least 8 characters in length, and may be at most 63 characters in length. | [optional] 
**privacy_protocol** | **str** | Encryption protocol for SNMP messages. Valid values are &#x60;AES&#x60; and &#x60;DES&#x60;. | [optional] 
**user** | **str** | User ID recognized by the specified SNMP managers which Purity is to use in communications with them. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


