# Bucket

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**space** | [**Space**](Space.md) | the space specification of the bucket | [optional] 
**account** | [**Reference**](Reference.md) | the account of the bucket | [optional] 
**destroyed** | **bool** | is the bucket destroyed? False by default. Modifiable. | [optional] 
**time_remaining** | **int** | time in milliseconds before the bucket is eradicated. Null if not destroyed. | [optional] 
**object_count** | **int** | the number of object within the bucket. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


