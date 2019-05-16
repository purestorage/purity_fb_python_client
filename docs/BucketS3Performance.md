# BucketS3Performance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A non-modifiable, globally unique ID chosen by the system. | [optional] 
**name** | **str** | The name of the object (e.g., a file system or snapshot). | [optional] 
**others_per_sec** | **int** | Other operations processed per second. | [optional] 
**read_buckets_per_sec** | **int** | Read buckets requests processed per second. | [optional] 
**read_objects_per_sec** | **int** | Read object requests processed per second. | [optional] 
**write_buckets_per_sec** | **int** | Write buckets requests processed per second. | [optional] 
**write_objects_per_sec** | **int** | Write object requests processed per second. | [optional] 
**time** | **int** | Sample time in milliseconds since UNIX epoch. | [optional] 
**usec_per_other_op** | **int** | Average time, measured in microseconds, it takes the array to process other operations. | [optional] 
**usec_per_read_bucket_op** | **int** | Average time, measured in microseconds, it takes the array to process a read bucket request. | [optional] 
**usec_per_read_object_op** | **int** | Average time, measured in microseconds, it takes the array to process a read object request. | [optional] 
**usec_per_write_bucket_op** | **int** | Average time, measured in microseconds, it takes the array to process a write bucket request. | [optional] 
**usec_per_write_object_op** | **int** | Average time, measured in microseconds, it takes the array to process a write object request. | [optional] 

[[Back to Model list]](index.md#documentation-for-models) [[Back to API list]](index.md#endpoint-properties) [[Back to Overview]](index.md)


