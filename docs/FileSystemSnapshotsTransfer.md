# FileSystemSnapshotsTransfer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**completed** | **int** | A timestamp at which the replication of the snapshot completed. | [optional] 
**data_transferred** | **int** | The amount of data transferred to the target, in bytes. | [optional] 
**direction** | [**Direction**](Direction.md) |  | [optional] 
**progress** | **float** | A percentage that indicates how much progress has been made on the transfer. | [optional] 
**remote** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | The array where the remote file system snapshot is located. | [optional] 
**remote_snapshot** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | A reference to the associated remote file system snapshot. | [optional] 
**started** | **int** | A timestamp at which the replication of the snapshot started. | [optional] 
**status** | **str** | The status of current replication. Valid values are &#x60;completed&#x60;, &#x60;in-progress&#x60;, and &#x60;queued&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


