import boto3
client=boto3.client('s3')

client.upload_file('./goals.docx','ravi-quote-bucket','goals.docx')