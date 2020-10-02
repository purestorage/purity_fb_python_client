# LifecycleRulePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | [**Reference**](Reference.md) | The bucket name for lifecycle rule creation. | 
**rule_id** | **str** | Identifier for the rule that is unique to the bucket that it applies to. Can have a maximum length of 255 characters. If not specified, an id unique to the bucket will be generated in the format &#x60;fbRuleId&lt;number&gt;&#x60; where number increments, starting at 1. | [optional] 
**keep_previous_version_for** | **int** | Time after which previous versions will be marked expired. Measured in milliseconds. Must be a multiple of 86400000 to represent a whole number of days. | 
**prefix** | **str** | Object key prefix identifying one or more objects in the bucket. Can have a maximum length of 1024 characters. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


