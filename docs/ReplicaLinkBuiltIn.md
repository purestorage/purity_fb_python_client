# ReplicaLinkBuiltIn

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**Direction**](Direction.md) |  | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**lag** | **int** | Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and &#x60;recovery_point&#x60;. | [optional] 
**remote** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference to a remote target. | [optional] 
**status_details** | **str** | Detailed information about the status of the replica link. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


