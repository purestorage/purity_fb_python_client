# DirectoryService

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**base_dn** | **str** | Base of the Distinguished Name (DN) of the directory service groups. | [optional] 
**bind_password** | **str** | Obfuscated password used to query the directory. | [optional] 
**bind_user** | **str** | Username used to query the directory. | [optional] 
**ca_certificate** | [**Reference**](Reference.md) | CA certificate used to validate the authenticity of the configured servers. | [optional] 
**ca_certificate_group** | [**Reference**](Reference.md) | Certificate group containing CA certificates that can be used to validate the authenticity of the configured servers. | [optional] 
**enabled** | **bool** | Is the directory service enabled or not? | [optional] 
**services** | **list[str]** | Services that the directory service configuration is used for. | [optional] 
**uris** | **list[str]** | List of URIs for the configured directory servers. | [optional] 
**smb** | [**DirectoryserviceSmb**](DirectoryserviceSmb.md) |  | [optional] 
**nfs** | [**DirectoryserviceNfs**](DirectoryserviceNfs.md) |  | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


