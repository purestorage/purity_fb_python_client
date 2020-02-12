# DirectoryserviceManagement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_login_attribute** | **str** | User login attribute in the structure of the configured LDAP servers. Typically the attribute field that holds the user’s unique login name. Defaults to &#x60;sAMAccountName&#x60; for Active Directory servers, or &#x60;uid&#x60; for all other directory server types.  | [optional] 
**user_object_class** | **str** | Value of the object class for a management LDAP user. Defaults to &#x60;User&#x60; for Active Directory servers, &#x60;posixAccount&#x60; or &#x60;shadowAccount&#x60; for OpenLDAP servers dependent on the server&#39;s group type, or &#x60;person&#x60; for all other directory servers.  | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


