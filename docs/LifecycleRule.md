# LifecycleRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**bucket** | [**Reference**](Reference.md) | The bucket which this lifecycle rule is targeting. | [optional] 
**enabled** | **bool** | If set to &#x60;true&#x60;, this rule will be enabled. | [optional] 
**rule_id** | **str** | Unique identifier for the rule. Can have a maximum length of 255 characters. | [optional] 
**keep_previous_version_for** | **int** | Time after which previous versions will be marked expired. Measured in milliseconds. Must be a multiple of 86400000 to represent a whole number of days. | [optional] 
**prefix** | **str** | Object key prefix identifying one or more objects in the bucket. Can have a maximum length of 1024 characters. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


