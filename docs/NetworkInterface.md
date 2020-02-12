# NetworkInterface

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**address** | **str** |  | [optional] 
**enabled** | **bool** | Indicates if subnet is enabled (true) or disabled (false). Enabled by default. | [optional] 
**gateway** | **str** |  | [optional] 
**mtu** | **int** | Maximum message transfer unit (packet) size for the subnet in bytes. MTU setting cannot exceed the MTU of the corresponding physical interface. 1500 by default. | [optional] 
**netmask** | **str** |  | [optional] 
**services** | **list[str]** | Services and protocols that are enabled on the interface. | [optional] 
**subnet** | [**FixedReferenceWithId**](FixedReferenceWithId.md) |  | [optional] 
**type** | **str** | Possible values are vip. | [optional] 
**vlan** | **int** |  | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


