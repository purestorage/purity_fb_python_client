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
**promotion_status** | **str** | Possible values are &#x60;promoted&#x60; and &#x60;demoted&#x60;. The current status of the file system with respect to replication. Changes via &#x60;requested_promotion_state&#x60;. The default for new file systems is &#x60;promoted&#x60;. | [optional] 
**requested_promotion_state** | **str** | Possible values are &#x60;promoted&#x60; and &#x60;demoted&#x60;. The &#x60;demoted&#x60; state is used for replication targets and is only allowed to be set if the file system is in a replica-link relationship. The additional query param &#x60;discard-non-snapshotted-data&#x60; must be set to &#x60;true&#x60; when demoting a file system. The default for new file systems is &#x60;promoted&#x60;. | [optional] 
**smb** | [**SmbRule**](SmbRule.md) | SMB configuration. Modifiable. | [optional] 
**snapshot_directory_enabled** | **bool** | Is snapshot directory enabled? Modifiable. Default false when creating a new file-system. | [optional] 
**source** | [**LocationReference**](LocationReference.md) | The source snapshot whose data is copied to the file system specified. | [optional] 
**space** | [**Space**](Space.md) | The space specification of the file system. | [optional] 
**time_remaining** | **int** | Time in milliseconds before the file system is eradicated. Null if not destroyed. | [optional] 
**writable** | **bool** | -&gt; Is the file system writable? True by default. Cannot be True when &#x60;promoted&#x60; is False. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


