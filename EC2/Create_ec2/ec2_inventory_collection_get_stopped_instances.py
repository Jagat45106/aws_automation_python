import boto3

aws_console = boto3.session.Session(profile_name="boto_profile")
ec2_console = aws_console.resource("ec2")

filter_list = {"Name": "instance-state-name", "Values": ["stopped"]}
stopped_instance = ec2_console.instances.filter(Filters=[filter_list])

for each_stopped_inst in stopped_instance:
    print(f"{each_stopped_inst}" + " " + "are in stopped state")