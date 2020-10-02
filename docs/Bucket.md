# Bucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**created** | **int** | Creation timestamp of the object | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**space** | [**Space**](Space.md) | The space specification of the bucket. | [optional] 
**account** | [**Reference**](Reference.md) | The account of the bucket. | [optional] 
**destroyed** | **bool** | Is the bucket destroyed? | [optional] 
**time_remaining** | **int** | Time in milliseconds before the bucket is eradicated. Null if not destroyed. | [optional] 
**object_count** | **int** | The number of object within the bucket. | [optional] 
**versioning** | **str** | The versioning state for objects within the bucket. Valid values are &#x60;none&#x60;, &#x60;enabled&#x60;, and &#x60;suspended&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


