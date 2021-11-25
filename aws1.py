def create_key_pair():
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    key_pair = ec2_client.create_key_pair(KeyName="ec2-key-pair")

    private_key = key_pair["KeyMaterial"]

    # write private key to file with 400 permissions
    with os.fdopen(os.open("/tmp/aws_ec2_key.pem", os.O_WRONLY | os.O_CREAT, 0o400), "w+") as handle:
        handle.write(private_key)

def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    instances = ec2_client.run_instances(
        ImageId="ami-0b0154d3d8011b0cd",
        MinCount=1,
        MaxCount=1,
        InstanceType="t4g.nano",
        KeyName="ec2-key-pair"
    )

    print(instances["Instances"][0]["InstanceId"])

def get_public_ip(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-west-2")
    reservations = ec2_client.describe_instances(InstanceIds=[instance_id]).get("Reservations")

    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get("PublicIpAddress"))




