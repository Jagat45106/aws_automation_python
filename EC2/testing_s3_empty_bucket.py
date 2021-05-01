import boto3
import sys

aws_mgmt_console = boto3.session.Session(profile_name="boto_profile")
s3_console = aws_mgmt_console.resource('s3'
                                       )