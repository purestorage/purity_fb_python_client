# Keytab

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**encryption_type** | **str** | The encryption type used by the kerberos domain controller to generate the keytab. | [optional] 
**fqdn** | **str** | The fully qualified domain name to which the keytab was issued. | [optional] 
**kvno** | **int** | The key version number of the key used to generate the keytab. | [optional] 
**prefix** | **str** | The prefix in the name of the keytab object. This is the same for all keytab objects created from a single keytab file. The name of a keytab entry is created in the format &#x60;&lt;prefix&gt;.&lt;suffix&gt;&#x60; for all entries. | [optional] 
**principal** | **str** | The service name for which the keytab was issued. | [optional] 
**realm** | **str** | The kerberos realm that issued the keytab. | [optional] 
**suffix** | **int** | The suffix in the name of the keytab object, determined at creation time using the slot number of the keytab entry in a file and the number of existing entries with the same prefix. The name of a keytab entry is created in the format &#x60;&lt;prefix&gt;.&lt;suffix&gt;&#x60; for all entries. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


