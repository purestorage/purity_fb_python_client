# QuotasGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot) | [optional] 
**file_system** | [**FixedReference**](FixedReference.md) |  | [optional] 
**file_system_default_quota** | **int** | File system&#39;s default group quota (in bytes). If it is 0, it means there is no default quota. This will be the effective group quota if the group doesn&#39;t have an individual quota. This default quota is set through the file-system endpoint. | [optional] 
**group** | [**QuotasgroupGroup**](QuotasgroupGroup.md) |  | [optional] 
**quota** | **int** | The space limit of the quota (in bytes) for the specified group, cannot be 0. Modifiable. If specified, this value will override the file system&#39;s default group quota. | [optional] 
**usage** | **int** | The usage of the file system (in bytes) by the specified group. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


