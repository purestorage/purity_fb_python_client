# SmbRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | is the protocol enabled? Default false when creating a new rule | [optional] 
**acl_mode** | **str** | Valid values for existing file systems are &#x60;shared&#x60; and &#x60;native&#x60;, and the field can also be &#x60;null&#x60;. This field is deprecated in favor of the &#x60;access_control_style&#x60; field on file systems. Modification of this field is allowed and setting its value will change the &#x60;access_control_style&#x60; field&#39;s value to an equivalent value. This field will be &#x60;null&#x60; if the value of &#x60;access_control_style&#x60; does not match the behavior of this field being &#x60;shared&#x60; or &#x60;native&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


