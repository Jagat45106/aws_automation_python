import boto3

aws_mgmt_console = boto3.session.Session(profile_name="boto_profile")
ec2_console = aws_mgmt_console.client("ec2")
print("\n")
print("************** EC2 creation tool - Windows or Linux *****************\n")

# Take the inputs
ami_id = input("Enter the image id: ")
instance_type = input("Enter the instance type e.g t2.micro: ")
keypair_name = input("Enter the key pair name: ")
instance_count = int(input("How many instance you want?: "))
sg_id = input("Enter the security group id: ")
print("\n")
print(f"Creating {instance_count} instances as per your input...\n")
response = ec2_console.run_instances(
    BlockDeviceMappings=[
        {
            "DeviceName": "/dev/sda1",
            "Ebs": {
                "VolumeSize": 30,
                "DeleteOnTermination": True | False,
                "VolumeType": "gp2",
            },
        },
    ],
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=keypair_name,
    MaxCount=instance_count,
    MinCount=1,
    SecurityGroupIds=[sg_id],
    InstanceInitiatedShutdownBehavior="stop",
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "Python-Jagat",
                },
            ],
        },
    ],
)
print("Waiting for instance status = Running...\n")

for each_inc in response["Instances"]:
    waiter = ec2_console.get_waiter("instance_running")
    waiter.wait(InstanceIds=[each_inc["InstanceId"]])
    instance_id = each_inc["InstanceId"]
    print(f"Instance {instance_id} is running now")
