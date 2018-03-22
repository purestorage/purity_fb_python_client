# DirectoryService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**base_dn** | **str** | Base of the Distinguished Name (DN) of the directory service groups | [optional] 
**bind_password** | **str** | Obfuscated password used to query the directory | [optional] 
**bind_user** | **str** | Username used to query the directory | [optional] 
**enabled** | **bool** | Is the directory service enabled or not ? | [optional] 
**services** | **list[str]** | Services that the directory service configuration is used for | [optional] 
**uris** | **list[str]** | List of URIs for the configured directory servers | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


