import json
import urllib.request
import boto3
import os

def lambda_handler(event, context):
    sns_topic_arn=os.getenv("SNS_TOPIC_ARN")
    sns_client=boto3.client('sns')

    quote=quote_function()

    try:
        sns_client.publish(
            TopicArn= sns_topic_arn,
            Message=quote,
            Subject="Your inspiration for the day"
        )
    except Exception as e:
        print("Error:",e)
        return {"statusCode":500, "body":"Failed to deliver quote"}
    
    return {"statusCode":200, "body":"Quote successfully delivered"}


def quote_function():
    api_url="https://zenquotes.io/api/random"
    try:
        with urllib.request.urlopen(api_url) as response:  
            text=json.loads(response.read())
            quote=text[0]['q']
            author=text[0]['a']

            return f"{quote} - {author}"
    except Exception as e:
        print("Error: ",e)
        return "Failed to inspire you today"