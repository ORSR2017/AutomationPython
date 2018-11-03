# coding: utf-8
import boto3
session = boto3.Session(profile_name='pythonAutomation'
)
s3 = session.resorce('s3')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
s3.create_bucket(Bucket='orsr-newbucket')
new_bucket = s3.create_bucket(Bucket='orsr-newbucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2})
)
new_bucket = s3.create_bucket(Bucket='orsr-newbucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2})
new_bucket = s3.create_bucket(Bucket='orsr-newbucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2})
new_bucket = s3.create_bucket(Bucket='orsr-newbucket', CreateBucketConfiguration={'LocationConstraint':'us-east-2})
