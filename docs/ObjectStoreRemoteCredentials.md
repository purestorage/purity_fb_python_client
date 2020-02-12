# ObjectStoreRemoteCredentials

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**access_key_id** | **str** | Access Key ID to be used when connecting to a remote object store. | [optional] 
**secret_access_key** | **str** | Secret Access Key to be used when connecting to a remote object store. After creation, listing will only show ****. | [optional] 
**remote** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference of the associated array connection or target. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


