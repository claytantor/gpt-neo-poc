from transformers import pipeline
path = "/media/clay/81dddd61-d829-4504-b0b8-9bb627b6c6a7/home/clay/data/github.com/huggingface"

generator = pipeline('text-generation', model='{}/gpt-neo-2.7B'.format(path))

result = generator("EleutherAI has", do_sample=True, min_length=50)
print(result)
