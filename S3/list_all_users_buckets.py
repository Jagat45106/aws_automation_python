import boto3

# Get all the IAM user list
get_in_aws_console = boto3.session.Session(profile_name='boto_profile')
get_in_iam = get_in_aws_console.resource('iam')
print("All IAM user list are below:")
print("-----------------------------")

for each_user in get_in_iam.users.all():
  print(each_user.name)
  
 # Get all the S3 bucket list
get_in_s3 = get_in_aws_console.resource('s3')
print("\n")
print("All Bucket list are below:")
print("--------------------------")
for each_bucket in get_in_s3.buckets.all():
   print(each_bucket.name)
