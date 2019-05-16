# ObjectStoreUser

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**account** | [**Reference**](Reference.md) | Reference to the associated account. | [optional] 
**access_keys** | [**list[FixedReferenceWithId]**](FixedReferenceWithId.md) | References to the user&#39;s access keys. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


