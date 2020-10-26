# NfsRulePatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Is the NFSv3 protocol enabled? Default is false (deprecated). | [optional] 
**rules** | **str** | NFS rules. | [optional] 
**v3_enabled** | **bool** | Is the NFSv3 protocol enabled? Default is false. | [optional] 
**v4_1_enabled** | **bool** | Is the NFSv4.1 protocol enabled? Default is false. | [optional] 
**add_rules** | **str** | The rules which will be added to the existing NFS export rules for the file system. | [optional] 
**remove_rules** | **str** | The rules which will be removed from the existing NFS export rules for the file system. Only the first occurrence of the &#x60;remove_rules&#x60; will be removed. | [optional] 
**after** | **str** | The &#x60;after&#x60; field can be used with &#x60;add_rules&#x60; or &#x60;remove_rules&#x60; or both. If used with &#x60;add_rules&#x60;, then the &#x60;add_rules&#x60; string will be inserted after the first occurrence of the &#x60;after&#x60; string. If used with &#x60;remove_rules&#x60;, then remove the first occurrence of &#x60;remove_rules&#x60; after the first occurrence of the &#x60;after&#x60; string. The &#x60;remove_rules&#x60; will be processed before the &#x60;add_rules&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


