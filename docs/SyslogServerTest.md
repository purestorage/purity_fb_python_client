# SyslogServerTest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**component_address** | **str** | Address of the component running the test. | [optional] 
**component_name** | **str** | Name of the component running the test. | [optional] 
**description** | **str** | What the test is doing. | [optional] 
**destination** | **str** | The URI of the target syslog server being tested. | [optional] 
**details** | **str** | The output of the test. | [optional] 
**success** | **bool** | Returns a value of &#x60;true&#x60; if the specified test succeeded. Returns a value of &#x60;false&#x60; if the specified test failed. | [optional] 
**test_type** | **str** | Displays the type of test being performed.  The returned values are determined by the syslog connection being tested and its configuration. Possible values include &#x60;connecting&#x60; and &#x60;message-sending&#x60;. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


