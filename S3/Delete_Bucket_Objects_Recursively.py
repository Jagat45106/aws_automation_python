import boto3

s3 = boto3.resource("s3")
bucket = s3.Bucket("aws-cloudtrail-logs-051134810526-ce792b6a")

"""
Prefix="AWSLogs/" - Folder and child folder will be deleted from AWSLogs onwards

"""

for obj in bucket.objects.filter(Prefix="AWSLogs/"):
    s3.Object(bucket.name, obj.key).delete()
    print("done")