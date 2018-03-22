# HardwareConnector

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**connector_type** | **str** | Form-factor of the interface (QSFP vs SFP vs RJ-45) | [optional] 
**lane_speed** | **int** | Configured speed of each lane in the connector in bits-per-second | [optional] 
**port_count** | **int** | Configured number of ports in the connector. (1/2/4 for QSFP) | [optional] 
**transceiver_type** | **str** | Details about the transceiver which is plugged into the connector port. Transceiver type will be read-only for Pureuser. If nothing is plugged into QSFP port, value will be “Unused”. If a transceiver is plugged in, and type cannot be auto-detected,  and internal user has not specified a type - value will be “Unknown”. If transceiver is plugged in, and type is auto-detected, and/or type has been explicitly set by internal user - that value will be shown. Transceiver type is not applicable for RJ-45 connectors. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


