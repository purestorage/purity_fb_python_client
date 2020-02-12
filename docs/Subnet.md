# Subnet

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**enabled** | **bool** | Indicates if subnet is enabled (true) or disabled (false). Enabled by default. | [optional] 
**gateway** | **str** | The IPv4 or IPv6 address of the gateway through which the specified subnet is to communicate with the network. | [optional] 
**interfaces** | [**list[Reference]**](Reference.md) | List of network interfaces associated with this subnet. | [optional] 
**link_aggregation_group** | [**Reference**](Reference.md) | reference of the associated LAG. | [optional] 
**mtu** | **int** | Maximum message transfer unit (packet) size for the subnet in bytes. MTU setting cannot exceed the MTU of the corresponding physical interface. 1500 by default. | [optional] 
**prefix** | **str** | The IPv4 or IPv6 address to be associated with the specified subnet. | [optional] 
**services** | **list[str]** | The services provided by this subnet, as inherited from all of its interfaces. | [optional] 
**vlan** | **int** | VLAN ID | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


