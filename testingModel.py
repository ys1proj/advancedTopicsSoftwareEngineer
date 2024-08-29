import torch
from transformers import LlamaForCausalLM, LlamaTokenizer

# Load the tokenizer and model
model_name = "finegptproject/humaneval_SFTTrainer_model"
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

# Function to get model output
def get_model_output(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_new_tokens=100)  # Increase token limit
    return tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

# Define test cases
test_cases = [
    ('xyzXYZ', 3),  # Case with mixed case characters
    ('Jerry', 4),   # Case with mixed case characters
    ('aabbcc', 3),  # Case with repeated characters
    ('AaBbCc', 3),  # Case with case-insensitive unique characters
    ('hello', 4)    # Case with standard characters
]

# Prepare prompts and compare outputs
for string, expected in test_cases:
    # Create the prompt for the model
    prompt = f"How many distinct characters are there in the string '{string}', ignoring case?"
    
    # Get model output
    model_output = get_model_output(prompt)
    
    # Print results for debugging
    print(f"Prompt: {prompt}")
    print(f"Model Output: {model_output}")
    
    # Parse the model output (assuming it will be a number in string form)
    try:
        model_output = int(model_output)
    except ValueError:
        model_output = None
    
    # Print results
    print(f"Input String: '{string}'")
    print(f"Expected: {expected}")
    print(f"Pass: {model_output == expected}")
    print()
