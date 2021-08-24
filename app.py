import sys, os
import json

from transformers import pipeline
path = "/media/clay/81dddd61-d829-4504-b0b8-9bb627b6c6a7/home/clay/data/github.com/huggingface"
generator = pipeline('text-generation', model='{}/gpt-neo-2.7B'.format(path))

def handler(event, context):

    result = generator(event['message'], do_sample=True, min_length=150)
    indexval = len(event['message'])
    result[0]['generated_text'] = result[0]['generated_text'][indexval:].replace("\n", "")


    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "response ": result[0]['generated_text'],
        })
    }