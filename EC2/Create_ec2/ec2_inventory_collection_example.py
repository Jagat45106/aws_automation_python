# Established connection
import boto3

aws_console = boto3.session.Session(profile_name="boto_profile")
ec2_console = aws_console.resource("ec2")

"""
all_ec2 = ec2_console.instances.all()

for each_inc in all_ec2:
    print(each_inc)
"""

for each_inc_limit in ec2_console.instances.limit(3):
    print(each_inc_limit)
