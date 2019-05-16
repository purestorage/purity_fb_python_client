# CertificatePost

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**certificate** | **str** | The text of the certificate. | [optional] 
**certificate_type** | **str** | The type of certificate. Possible values are &#x60;array&#x60; and &#x60;external&#x60;. Certificates of type &#x60;array&#x60; are used by the array to verify its identity to clients. Certificates of type &#x60;external&#x60; are used by the array to identify external servers to which it is configured to communicate. | [optional] 
**intermediate_certificate** | **str** | Intermediate certificate chains. | [optional] 
**passphrase** | **str** | The passphrase used to encrypt the private key. | [optional] 
**private_key** | **str** | The private key used to sign the certificate. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


