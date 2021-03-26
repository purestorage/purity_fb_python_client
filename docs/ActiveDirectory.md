# ActiveDirectory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**computer_name** | **str** | The common name of the computer account to be created in the Active Directory domain. If not specified, defaults to the name of the Active Directory configuration. | [optional] 
**directory_servers** | **list[str]** | A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. | [optional] 
**domain** | **str** | The Active Directory domain to join. | [optional] 
**encryption_types** | **list[str]** | The encryption types that are supported for use by clients for Kerberos authentication. | [optional] 
**join_ou** | **str** | The relative distinguished name of the organizational unit in which the computer account was created when joining the domain. | [optional] 
**kerberos_servers** | **list[str]** | A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS. | [optional] 
**service_principal_names** | **list[str]** | A list of service principal names registered for the machine account, which can be used for the creation of keys for Kerberos authentication. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


