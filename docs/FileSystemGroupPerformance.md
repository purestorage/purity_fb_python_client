# FileSystemGroupPerformance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the object (e.g., a file system or snapshot) | [optional] 
**bytes_per_op** | **float** | Average operation size (read bytes+write bytes/read ops+write ops). | [optional] 
**bytes_per_read** | **float** | Average read size in bytes per read operation. | [optional] 
**bytes_per_write** | **float** | Average write size in bytes per write operation. | [optional] 
**file_system** | [**FixedReference**](FixedReference.md) |  | [optional] 
**group** | [**FilesystemgroupperformanceGroup**](FilesystemgroupperformanceGroup.md) |  | [optional] 
**others_per_sec** | **float** | Other operations processed per second. | [optional] 
**read_bytes_per_sec** | **float** | Bytes read per second. | [optional] 
**reads_per_sec** | **float** | Read requests processed per second. | [optional] 
**time** | **int** | Sample time in milliseconds since UNIX epoch. | [optional] 
**usec_per_other_op** | **float** | Average time, measured in microseconds, it takes the array to process other operations. | [optional] 
**usec_per_read_op** | **float** | Average time, measured in microseconds, it takes the array to process a read request. | [optional] 
**usec_per_write_op** | **float** | Average time, measured in microseconds, it takes the array to process a write request. | [optional] 
**write_bytes_per_sec** | **float** | Bytes written per second. | [optional] 
**writes_per_sec** | **float** | Write requests processed per second. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


