import boto3
client=boto3.client('s3')

response=client.create_bucket(
    Bucket='ravi-quote-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

print(response)