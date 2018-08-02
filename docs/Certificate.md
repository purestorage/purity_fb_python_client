# Certificate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**certificate** | **str** | the text of the certificate | [optional] 
**common_name** | **str** | FQDN or management IP address of the current array | [optional] 
**country** | **str** | The country field listed in the certificate | [optional] 
**email** | **str** | The email field listed in the certificate | [optional] 
**intermediate_certificate** | **str** | intermediate certificate chains | [optional] 
**issued_by** | **str** | Who issued this certificate | [optional] 
**issued_to** | **str** | Who this certificate was issued to | [optional] 
**key_size** | **int** | The size of the private key for this certificate in bits | [optional] 
**locality** | **str** | The locality field listed in the certificate | [optional] 
**organization** | **str** | The organization field listed in the certificate | [optional] 
**organizational_unit** | **str** | The organizational unit field listed in the certificate | [optional] 
**state** | **str** | The state/province field listed in the certificate | [optional] 
**status** | **str** | The type of certificate. Possible values are self-signed and imported. | [optional] 
**valid_from** | **str** | The start date of when this certificate is valid | [optional] 
**valid_to** | **str** | The end date of when this certificate is valid | [optional] 
**passphrase** | **str** | the passphrase used to encrypt private_key | [optional] 
**private_key** | **str** | the private key used to sign the certificate | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


