# ActiveDirectoryPatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**directory_servers** | **list[str]** | A list of directory servers that will be used for lookups related to user authorization. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS and will only be communicated with over the secure LDAP (LDAPS) protocol. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. | [optional] 
**encryption_types** | **list[str]** | The encryption types that will be supported for use by clients for Kerberos authentication. Valid values include &#x60;aes256-cts-hmac-sha1-96&#x60;, &#x60;aes128-cts-hmac-sha1-96&#x60;, and &#x60;arcfour-hmac&#x60;. | [optional] 
**fqdns** | **list[str]** | A list of fully qualified domain names to use to register service principal names for the machine account. If specified, every service principal that is supported by the array will be registered for each fully qualified domain name specified. If neither &#x60;fqdns&#x60; nor &#x60;service_principal_names&#x60; is specified, the default &#x60;service_principal_names&#x60; are constructed using the &#x60;computer_name&#x60; and &#x60;domain&#x60; fields. Cannot be provided in combination with &#x60;service_principal_names&#x60;. | [optional] 
**join_ou** | **str** | The relative distinguished name of the organizational unit in which the computer account should be created when joining the domain. | [optional] 
**kerberos_servers** | **list[str]** | A list of key distribution servers to use for Kerberos protocol. Accepted server formats are IP address and DNS name. All specified servers must be registered to the domain appropriately in the array&#39;s configured DNS. If not specified, servers are resolved for the domain in DNS. The specified list can have a maximum length of 5. | [optional] 
**service_principal_names** | **list[str]** | A list of service principal names to register for the machine account, which can be used for the creation of keys for Kerberos authentication. If neither &#x60;service_principal_names&#x60; nor &#x60;fqdns&#x60; is specified, the default &#x60;service_principal_names&#x60; are constructed using the &#x60;computer_name&#x60; and &#x60;domain&#x60; fields. Cannot be provided in combination with &#x60;fqdns&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


