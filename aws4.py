import boto3

s3.create_bucket(Bucket='mybucketsidhu19')
s3.create_bucket(Bucket='mybucket', CreateBucketConfiguration={
    'LocationConstraint': 'us-west-2'})


def upload_aws(aws1.py, bucket_name='mybucketsidhu19'):
    s3 = boto3.client('s3', aws_access_key_id=access_key,
                      aws_secret_access_key=secret_key)

    
    s3.upload_file(aws1.py, bucket_name, aws_filename)
    print("Upload Successful!")
    return True


