# FileSystemSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**destroyed** | **bool** | Is the file system snapshot destroyed? False by default. | [optional] 
**policy** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference of the associated policy. | [optional] 
**source** | **str** | The name of the source file system. | [optional] 
**source_destroyed** | **bool** | Is the source file system destroyed? | [optional] 
**source_id** | **str** | The id of the source file system. | [optional] 
**suffix** | **str** | The suffix of the snapshot, e.g., snap1 | [optional] 
**time_remaining** | **int** | Time in milliseconds before the file system snapshot is eradicated. Null if not destroyed. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


