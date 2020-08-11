# Policy

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**enabled** | **bool** | Indicates if policy is enabled (true) or disabled (false). Enabled by default. | [optional] 
**is_local** | **bool** | -&gt; Returns a value of &#x60;true&#x60; if the policy is defined on the local array. Returns a value of &#x60;false&#x60; if the policy is defined on the remote array. | [optional] 
**location** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | Reference to the array where the policy is defined. | [optional] 
**rules** | [**list[PolicyRule]**](PolicyRule.md) |  | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


