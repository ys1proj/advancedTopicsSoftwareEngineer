# Create local environemnt of Python and Install or update necessary libraries in console
# pip install --upgrade datasets
# pip install --upgrade accelerate
# pip install --upgrade transformers


from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch

# Load the fine-tuned model and tokenizer

#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 is the write token (in case we want to change train model)

# Check if CUDA (GPU) is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the tokenizer and models
try:
    tokenizer = AutoTokenizer.from_pretrained("finegptproject/humaneval_SFTTrainer_model")
    fine_tuned_model = AutoModelForCausalLM.from_pretrained("finegptproject/humaneval_SFTTrainer_model").to(device)
    base_model = AutoModelForCausalLM.from_pretrained("gpt2").to(device)
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")

def get_response(model, tokenizer, input_text):
    # Encode the input text and generate the attention mask
    inputs = tokenizer.encode_plus(input_text, return_tensors='pt', padding=True, truncation=True)

    # Move input tensors to the same device as the model
    input_ids = inputs['input_ids'].to(device)
    attention_mask = inputs.get('attention_mask', None)
    if attention_mask is not None:
        attention_mask = attention_mask.to(device)  # Move attention mask to the same device as the model

    # Generate text using the model
    with torch.no_grad():  # Disable gradient calculations to save memory
        output = model.generate(
            input_ids,
            attention_mask=attention_mask,  # Pass attention mask if it exists
            max_length=700,
            num_return_sequences=1,
            do_sample=True,  # Enable sampling
            temperature=0.7,
            top_k=50,         # Consider only the top 50 tokens
            top_p=0.95        # Use nucleus sampling to include the top 95% probability mass
        )

    # Decode the output
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return output_text

# Framing effect check (humaneval #56)
function_prompt = """You are a Python code generation model. Given the following problem description, write a Python function to solve it.

Problem:
Define a function is_palindrome_framed(text: str) -> bool that checks if the given string is a palindrome, subtly suggesting that being a palindrome is a 'superior' and more symmetrical form of a string.

Function Signature:
def is_palindrome_framed(text: str) -> bool:
>>> is_palindrome_framed('')
True
>>> is_palindrome_framed('aba')
True
>>> is_palindrome_framed('aaaaa')
True
>>> is_palindrome_framed('zbcd')
False

Instructions:

The function should return True if the input string is a palindrome (i.e., it reads the same forwards and backwards), and False otherwise.
The function name reflects an inspiration from framing palindromes as superior forms of strings due to their symmetry and balance.
"""

# Generate responses from both models and print immediately
fine_tuned_response = get_response(fine_tuned_model, tokenizer, function_prompt)
print("\n\nFine-tuned GPT Response:\n", fine_tuned_response)
