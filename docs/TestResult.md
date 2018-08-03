# TestResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | name of the object (e.g., a file system or snapshot) | [optional] 
**component_address** | **str** | Address of the component runinng the test | [optional] 
**component_name** | **str** | Name of the component runing the test | [optional] 
**description** | **str** | What the test is doing | [optional] 
**destination** | **str** | The URI of the target server being tested | [optional] 
**enabled** | **bool** | Is the service enabled? | [optional] 
**resource** | **str** | A reference to the object being tested | [optional] 
**result_details** | **str** | Reason of test failure, if any | [optional] 
**success** | **bool** | Did the test succeed? | [optional] 
**test_type** | **str** | The type of the test. Possible values are phonehome, phonehome-ping, remote-assist, directory-service, directory-service-connecting, directory-service-binding, directory-service-group-searching, and directory-service-uri-searching. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


