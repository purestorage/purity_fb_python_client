# FileSystemPatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_user_quota** | **int** | Default quota for a user under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system. | [optional] 
**default_group_quota** | **int** | Default quota for a group under this file system. Modifiable. Default is 0, meaning no quota, when creating a new file-system. | [optional] 
**destroyed** | **bool** | Is the file system destroyed? False by default. Modifiable. | [optional] 
**fast_remove_directory_enabled** | **bool** | Is fast remove directory enabled? Modifiable. Default false when creating a new file-system. | [optional] 
**hard_limit_enabled** | **bool** | Is the file system&#39;s size a hard limit quota. Modifiable. Default is false. | [optional] 
**http** | [**ProtocolRule**](ProtocolRule.md) | HTTP configuration. Modifiable. | [optional] 
**multi_protocol** | [**MultiProtocolRule**](MultiProtocolRule.md) | Configuration options governing the interactions of different protocols when multiple are enabled on the file system. | [optional] 
**nfs** | [**NfsRulePatch**](NfsRulePatch.md) | NFS configuration. Modifiable. | [optional] 
**provisioned** | **int** | The provisioned size of the file system in bytes. Modifiable. Default is 0 when creating a new file-system. | [optional] 
**requested_promotion_state** | **str** | Possible values are &#x60;promoted&#x60; and &#x60;demoted&#x60;. The &#x60;demoted&#x60; state is used for replication targets and is only allowed to be set if the file system is in a replica-link relationship. The additional query param &#x60;discard-non-snapshotted-data&#x60; must be set to &#x60;true&#x60; when demoting a file system. The default for new file systems is &#x60;promoted&#x60;. | [optional] 
**smb** | [**SmbRule**](SmbRule.md) | SMB configuration. Modifiable. | [optional] 
**snapshot_directory_enabled** | **bool** | Is snapshot directory enabled? Modifiable. Default false when creating a new file-system. | [optional] 
**writable** | **bool** | -&gt; Is the file system writable? True by default. Cannot be True when &#x60;promoted&#x60; is False. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


