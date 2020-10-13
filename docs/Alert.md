# Alert

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot) | [optional] 
**created** | **int** | Creation timestamp of the object | [optional] 
**index** | **int** | the unique index of the alert | [optional] 
**code** | **int** | alert code | [optional] 
**severity** | **str** | Severity of the alert. Possible values are info, warning and critical. | [optional] 
**component** | **str** | the component of the alert | [optional] 
**state** | **str** | The current state of the alert. Possible values are open, closing, closed and waiting to downgrade. | [optional] 
**flagged** | **bool** | whether the alert is flagged or not | [optional] 
**updated** | **int** | the last updated timestamp of the alert | [optional] 
**notified** | **int** | the last notification timestamp of the alert | [optional] 
**subject** | **str** | the subject of the alert | [optional] 
**description** | **str** | the description of the alert | [optional] 
**knowledge_base_url** | **str** | the kb url of the alert | [optional] 
**action** | **str** | the action of the alert | [optional] 
**variables** | **dict(str, str)** | key-value pairs of additional information of the alert | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


