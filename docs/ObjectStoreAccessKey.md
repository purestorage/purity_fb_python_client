# ObjectStoreAccessKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot) | [optional] 
**created** | **int** | Creation timestamp of the object | [optional] 
**user** | [**Reference**](Reference.md) | Reference to the associated user. | [optional] 
**enabled** | **bool** | Is the access key enabled? Default is true. | [optional] 
**secret_access_key** | **str** | The secret access key, only populated on creation if it is not imported from another FlashBlade. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


