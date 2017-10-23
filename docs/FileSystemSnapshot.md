# FileSystemSnapshot

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**suffix** | **str** | the suffix of the snapshot, e.g., snap1 | [optional] 
**source** | **str** | the name of the source file system | [optional] 
**destroyed** | **bool** | is the file system snapshot destroyed? False by default. Modifiable. | [optional] 
**source_destroyed** | **bool** | is the source file system destroyed? | [optional] 
**time_remaining** | **int** | time in milliseconds before the file system snapshot is eradicated. Null if not destroyed. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


