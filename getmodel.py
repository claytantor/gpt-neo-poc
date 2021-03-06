from transformers import pipeline
from transformers import GPTNeoForCausalLM, GPT2Tokenizer


model = GPTNeoForCausalLM.from_pretrained("EleutherAI/gpt-neo-1.3B")
model.save_pretrained('./model')
tokenizer = GPT2Tokenizer.from_pretrained("EleutherAI/gpt-neo-1.3B")
tokenizer.save_pretrained('./model')
