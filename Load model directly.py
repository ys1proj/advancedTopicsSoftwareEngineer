from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch

# Check PyTorch installation
print("CUDA available:", torch.cuda.is_available())
print("PyTorch version:", torch.__version__)

# Authenticate using your Hugging Face token
login("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")

# Load the tokenizer and models
tokenizer = AutoTokenizer.from_pretrained("finegptproject/fine-tuned-gpt2")
fine_tuned_model = AutoModelForCausalLM.from_pretrained("finegptproject/fine-tuned-gpt2")
base_model = AutoModelForCausalLM.from_pretrained("gpt2")

def get_response(model, tokenizer, input_text):
    # Encode the input text and generate the attention mask
    inputs = tokenizer.encode_plus(input_text, return_tensors='pt', padding=True, truncation=True)
    
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Generate text using the model
    output = model.generate(
    input_ids,
    attention_mask=attention_mask,
    max_length=300,
    num_return_sequences=1,
    do_sample=True,          # Enable sampling
    temperature=0.7          # Use temperature to control randomness
)


    # Decode the output
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return output_text


function_prompt = """You are a Python code generation model. Given the following problem description, write a Python function to solve it.

Problem:
    Define a function `largest_divisor(n: int) -> int` that finds the largest integer less than `n` that divides `n` evenly.

Function Signature:
    def largest_divisor(n: int) -> int:

Examples:
    >>> largest_divisor(15)
    5
    >>> largest_divisor(28)
    14
    >>> largest_divisor(1)
    0
    >>> largest_divisor(12)
    6

Instructions:
    - The function should return the largest integer less than `n` that divides `n` evenly.
    - If no such divisor exists (i.e., when `n` is less than 2), return 0.
"""

# Generate responses from both models
fine_tuned_response = get_response(fine_tuned_model, tokenizer, function_prompt)
base_model_response = get_response(base_model, tokenizer, function_prompt)
     
# Print the responses
print("\n\nFine-tuned GPT-2 Response:\n", fine_tuned_response)
print("\n\nBase GPT-2 Response:\n", base_model_response)