import sys, os
import json

from transformers import  pipeline
generator = pipeline('text-generation', model='./model')

def handler(event, context):

    print(event,event['message'])
    # body = json.loads(event['body'])
    result = generator(event['message'], do_sample=True, min_length=150)
    indexval = len(event['message'])
    result[0]['generated_text'] = result[0]['generated_text'][indexval:].replace("\n", "")

    try:
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                'Access-Control-Allow-Origin': '*'
            },
            "body": json.dumps({'answer': result[0]['generated_text']})
        }
    except Exception as e:
        print(repr(e))
        return {
            "statusCode": 500,
            "headers": {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            "body": json.dumps({"error": repr(e)})
        }        