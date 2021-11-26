import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('mybucket-sdfslkjd')
for key in bucket.objects.all():
        key.delete()
bucket.delete()
