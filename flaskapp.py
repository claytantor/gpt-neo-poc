from flask import Flask, jsonify, request

from transformers import pipeline
path = "/media/clay/81dddd61-d829-4504-b0b8-9bb627b6c6a7/home/clay/data/github.com/huggingface"
generator = pipeline('text-generation', model='{}/gpt-neo-2.7B'.format(path))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/neo/text/generation', methods=['POST'])
def neo_text_generation():
    eval = request.get_json()
    result = generator(eval['message'], do_sample=True, min_length=150)
    indexval = len(eval['message'])
    result[0]['generated_text'] = result[0]['generated_text'][indexval:].replace("\n", "")
    return jsonify(result[0])
