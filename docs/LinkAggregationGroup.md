# LinkAggregationGroup

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**lag_speed** | **int** | Combined speed of all ports in the LAG in bits-per-second. | [optional] 
**mac_address** | **str** | Unique MAC address assigned to the LAG | [optional] 
**ports** | [**list[Reference]**](Reference.md) | Ports associated with the LAG | [optional] 
**port_speed** | **int** | Configured speed of each port in the LAG in bits-per-second | [optional] 
**status** | **str** | Health status of the LAG. Possible values are critical, healthy, identifying, unclaimed, unhealthy, unrecognized and unused. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


