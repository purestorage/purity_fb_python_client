# CertificateUse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**group** | [**FixedReferenceWithId**](FixedReferenceWithId.md) | A reference to a certificate-group that is being used, if any, where this certificate is a member of the certificate-group. This field is null if the referenced use object is not using a group, but is rather using this certificate directly. | [optional] 
**use** | [**FixedReferenceWithRemote**](FixedReferenceWithRemote.md) | A reference to an object using this certificate. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


