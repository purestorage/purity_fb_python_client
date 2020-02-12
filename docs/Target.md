# Target

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A name chosen by the user. Can be changed. Must be locally unique. | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**address** | **str** | IP address or FQDN of the target system. | [optional] 
**ca_certificate_group** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | The group of CA certificates that can be used, in addition to well-known Certificate Authority certificates, in order to establish a secure connection to the target system. Defaults to a reference to the _default_replication_certs group. | [optional] 
**status** | **str** | Status of the connection. Valid values are connected and connecting. connected - The connection is OK. connecting - No connection exists and the array is trying to reconnect to the target. | [optional] 
**status_details** | **str** | Additional information describing any issues encountered when connecting, or null if the status is connected. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


