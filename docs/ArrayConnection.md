# ArrayConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**ca_certificate_group** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | The group of CA certificates that can be used, in addition to well-known Certificate Authority certificates, in order to establish a secure connection to the target array. Defaults to a reference to the _default_replication_certs group if secure_connection is true, or null otherwise. | [optional] 
**management_address** | **str** | Management address of the target array. Settable on POST only. Modifiable only on the source. | [optional] 
**replication_addresses** | **list[str]** | IP addresses and/or FQDNs of the target arrays. Settable on POST only. If not set on POST, will be set to all the replication addresses available on the target array at the time of the POST. | [optional] 
**status** | **str** | Status of the connection. Valid values are &#x60;connected&#x60;, &#x60;partially_connected&#x60;, &#x60;connecting&#x60;, and &#x60;incompatible&#x60;. &#x60;connected&#x60; - The connection is OK. &#x60;partially_connected&#x60; - Some replication addresses are working, but others are not. &#x60;connecting&#x60; - No connection exists and the array is trying to reconnect. &#x60;incompatible&#x60; - The target array is not compatible. | [optional] 
**encrypted** | **bool** | If this is set to true, then all customer data replicated over the connection will be sent over an encrypted connection using TLS, or will not be sent if a secure connection cannot be established. If this is set to false, then all customer data replicated over the connection will be sent over an unencrypted connection. Defaults to false. | [optional] [default to False]
**remote** | [**FixedReferenceNoResourceType**](FixedReferenceNoResourceType.md) | The remote array. | [optional] 
**version** | **str** | The version of the target array. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


