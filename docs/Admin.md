# Admin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**api_token** | [**AdminApiToken**](AdminApiToken.md) |  | [optional] 
**create_api_token** | **bool** | Create a new API token. | [optional] 
**api_token_timeout** | **int** | Expire api-token after this period (in milliseconds). | [optional] 
**delete_api_token** | **bool** | Delete this user&#39;s API token. | [optional] 
**old_password** | **str** | Old user password. | [optional] 
**password** | **str** | User password. | [optional] 
**public_key** | **str** | Public key for SSH access. Supported key types are &#x60;Ed25519&#x60; and &#x60;RSA&#x60;. | [optional] 
**is_local** | **bool** | Returns a value of &#x60;true&#x60; if the user is local to the machine, otherwise &#x60;false&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


