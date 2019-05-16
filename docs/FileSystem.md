# FileSystem

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**created** | **int** | creation timestamp of the object | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**default_user_quota** | **int** | Default quota for a user under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system. | [optional] 
**default_group_quota** | **int** | Default quota for a group under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system. | [optional] 
**destroyed** | **bool** | Is the file system destroyed? False by default. Modifiable. | [optional] 
**fast_remove_directory_enabled** | **bool** | Is fast remove directory enabled? Modifiable. Default false when creating a new file-system. | [optional] 
**hard_limit_enabled** | **bool** | Is the file system&#39;s size a hard limit quota. Modifiable. Default is false. | [optional] 
**http** | [**ProtocolRule**](ProtocolRule.md) | HTTP configuration. Modifiable. | [optional] 
**nfs** | [**NfsRule**](NfsRule.md) | NFS configuration. Modifiable. | [optional] 
**provisioned** | **int** | The provisioned size of the file system in bytes. Modifiable. Default is 0 when creating a new file-system. | [optional] 
**snapshot_directory_enabled** | **bool** | Is snapshot directory enabled? Modifiable. Default false when creating a new file-system. | [optional] 
**smb** | [**SmbRule**](SmbRule.md) | SMB configuration. Modifiable. | [optional] 
**space** | [**Space**](Space.md) | the space specification of the file system | [optional] 
**time_remaining** | **int** | Time in milliseconds before the file system is eradicated. Null if not destroyed. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


