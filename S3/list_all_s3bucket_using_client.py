import boto3
aws_mgmt_console = boto3.session.Session(profile_name='boto_profile')
s3_console = aws_mgmt_console.client('s3')
result = s3_console.list_buckets()
for each_bkt in result['Buckets']:
  print(each_bkt['Name'])
