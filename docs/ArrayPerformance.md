# ArrayPerformance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot) | [optional] 
**bytes_per_op** | **int** | Average operation size (read bytes+write bytes/(read ops+write ops)) | [optional] 
**bytes_per_read** | **int** | Average read size in bytes per read operation | [optional] 
**bytes_per_write** | **int** | Average write size in bytes per write operation | [optional] 
**others_per_sec** | **int** | Other operations processed per second | [optional] 
**read_bytes_per_sec** | **int** | Bytes read per second | [optional] 
**reads_per_sec** | **int** | Read requests processed per second | [optional] 
**time** | **int** | Sample time in milliseconds since UNIX epoch | [optional] 
**usec_per_other_op** | **int** | Average time, measured in microseconds, that the array takes to process other operations | [optional] 
**usec_per_read_op** | **int** | Average time, measured in microseconds, that the array takes to process a read request | [optional] 
**usec_per_write_op** | **int** | Average time, measured in microseconds, that the array takes to process a write request | [optional] 
**write_bytes_per_sec** | **int** | Bytes written per second | [optional] 
**writes_per_sec** | **int** | Write requests processed per second | [optional] 
**output_per_sec** | **int** | Bytes read per second | [optional] 
**input_per_sec** | **int** | Bytes written per second | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


