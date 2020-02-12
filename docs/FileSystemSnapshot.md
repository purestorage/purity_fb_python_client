# FileSystemSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object | [optional] 
**id** | **str** | A unique ID chosen by the system. Cannot change. | [optional] 
**destroyed** | **bool** | Is the file system snapshot destroyed? False by default. | [optional] 
**owner** | [**Reference**](Reference.md) | A reference to the file system that owns this snapshot. If the owner is destroyed, this will be destroyed. | [optional] 
**owner_destroyed** | **bool** | Is the owning file system destroyed? | [optional] 
**policy** | [**LocationReference**](LocationReference.md) | A reference to the associated policy. | [optional] 
**source** | **str** | The name of the file system that was the source of the data in this snapshot. Normally this is the same as the owner, but if the snapshot is replicated, the source is the original file system. | [optional] 
**source_destroyed** | **bool** | Deprecated. Use &#x60;owner_destroyed&#x60;. Is the owning file system destroyed? | [optional] 
**source_id** | **str** | The unique global ID of the source file system. | [optional] 
**source_is_local** | **bool** | Is the source of this file system snapshot on the local array? | [optional] 
**source_location** | [**Reference**](Reference.md) | A reference to the source array. | [optional] 
**source_display_name** | **str** | Full name of the source with remote array information. Response will be same as source for local file system snapshots. | [optional] 
**suffix** | **str** | The suffix of the snapshot, e.g., snap1. | [optional] 
**time_remaining** | **int** | Time in milliseconds before the file system snapshot is eradicated. Null if not destroyed. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


