import boto3
  
ec2=boto3.resource('ec2', 'us-west-2')
response = ec2.create_snapshot(
        VolumeId="vol-08044d6c5e1dc65c2"
        )
