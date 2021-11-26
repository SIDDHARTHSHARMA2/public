import boto3
s3 = boto3.client('s3')
s3.create_bucket(Bucket='mybucket-sidhu19', CreateBucketConfiguration={'LocationConstraint': 'us-west-2'})

def upload_to_aws(local_file, bucket, s3_file):
        s3 = boto3.client('s3')


        try:
            s3.upload_file(local_file, bucket, s3_file)
            print("Upload Successful")
            return True
        except FileNotFoundError:
            print("The file was not found")
            return False
        except NoCredentialsError:
            print("Credentials not available")
            return False


upload_to_aws('/home/cloudshell-user/public/aws02.py', 'mybucket-sdfslkjd', 'ques2.py')


