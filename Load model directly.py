from transformers import AutoTokenizer, AutoModelForCausalLM

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("finegptproject/fine-tuned-gpt2")
model = AutoModelForCausalLM.from_pretrained("finegptproject/fine-tuned-gpt2")

# Encode the input text
input_text = "Once upon a time"
input_ids = tokenizer.encode(input_text, return_tensors='pt')

# Generate text
output = model.generate(input_ids, max_length=50, num_return_sequences=1)

# Decode the output
output_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(output_text)