import boto3
  
def stop_ec2_instance():
        try:
            print ("Stop EC2 instance")
            instance_id = describe_ec2_instance()
            resource_ec2 = boto3.client("ec2")
            print(resource_ec2.stop_instances(InstanceIds=[instance_id]))
        except Exception as e:
            print(e)

def terminate_ec2_instance():
     try:
         print ("Terminate EC2 instance")
         instance_id = "i-06cb3ef33cbf6b8c4"
         resource_ec2 = boto3.client("ec2")
         print(resource_ec2.terminate_instances(InstanceIds=[instance_id]))
     except Exception as e:
         print(e)

terminate_ec2_instance()
stop_ec2_instance()
