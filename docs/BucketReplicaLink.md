# BucketReplicaLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | [**Direction**](Direction.md) |  | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**lag** | **int** | Duration in milliseconds that represents how far behind the replication target is from the source. This is the time difference between current time and &#x60;recovery_point&#x60;. | [optional] 
**remote** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference to a remote target. | [optional] 
**status_details** | **str** | Detailed information about the status of the replica link. | [optional] 
**local_bucket** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference to a local bucket. | [optional] 
**paused** | **bool** | Is the replica link paused? | [optional] 
**recovery_point** | **int** | Time, in milliseconds since UNIX epoch, where all object changes before this time are guaranteed to have been replicated. Changes after this time may have been replicated. | [optional] 
**remote_bucket** | [**Reference**](Reference.md) | Reference to a remote bucket. | [optional] 
**remote_credentials** | [**Reference**](Reference.md) | Reference to a remote-credentials object to access the remote bucket. | [optional] 
**status** | **str** | Status of the replica link. Values include replicating, paused, and unhealthy. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


