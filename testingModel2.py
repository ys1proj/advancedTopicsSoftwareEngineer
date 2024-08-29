import torch
from transformers import LlamaForCausalLM, LlamaTokenizer, GPT2LMHeadModel, GPT2Tokenizer
from typing import List

# Define the function to test
def string_sequence(n: int) -> str:
    """
    Return a string containing space-delimited numbers starting from 0 up to n inclusive.

    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    return ' '.join(str(i) for i in range(n + 1))

# Load the tokenizer and model
#model_name = "finegptproject/humaneval_SFTTrainer_model"
#tokenizer = LlamaTokenizer.from_pretrained(model_name)
#model = LlamaForCausalLM.from_pretrained(model_name)
model_name = "gpt2" 
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Function to get model output
def get_model_output(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_new_tokens=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# Define test cases
test_cases = [
    (0, '0'),            # Simple case
    (5, '0 1 2 3 4 5'),  # Typical case
    (1, '0 1'),          # Small range
    (10, '0 1 2 3 4 5 6 7 8 9 10')  # Larger range
]

# Prepare prompts and compare outputs
for n, expected in test_cases:
    # Create the prompt for the model
    prompt = f"Generate a space-delimited sequence of numbers from 0 to {n} inclusive."
    
    # Get model output
    model_output = get_model_output(prompt)
    
    # Print results
    print(f"Input: {n}")
    print(f"Model Output: {model_output}")
    print(f"Expected: {expected}")
    print(f"Pass: {model_output == expected}")
    print()
