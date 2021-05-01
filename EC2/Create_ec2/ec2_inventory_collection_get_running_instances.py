# Established connection
import boto3

aws_console = boto3.session.Session(profile_name="boto_profile")
ec2_console = aws_console.resource("ec2")

filter_list = {"Name": "instance-state-name", "Values": ["running"]}
running_instance = ec2_console.instances.filter(Filters=[filter_list])

for each_running_inst in running_instance:
    print(f"{each_running_inst}" + " " + "are running")