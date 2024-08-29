import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "finegptproject/humaneval_SFTTrainer_model"

# Load tokenizer and model
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Now you can use the model for inference
test_input = "What is the capital of France?"
input_ids = tokenizer(test_input, return_tensors="pt").input_ids
output_ids = model.generate(input_ids, max_new_tokens=100)
response = tokenizer.decode(output_ids[0], skip_special_tokens=True)
print("Test Output:", response)
