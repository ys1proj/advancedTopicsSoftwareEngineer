# Create local environemnt of Python and Install or update necessary libraries in console
# pip install --upgrade datasets
# pip install --upgrade accelerate
# pip install --upgrade transformers


from transformers import AutoTokenizer, AutoModelForCausalLM
from huggingface_hub import login
import torch

# Load the fine-tuned model and tokenizer

#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 is the write token (in case we want to change train model)

# Check PyTorch installation
print("CUDA available:", torch.cuda.is_available())
print("PyTorch version:", torch.__version__)

# Authenticate using your Hugging Face token
login("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")

# Load the tokenizer and models
tokenizer = AutoTokenizer.from_pretrained("./fine-tuned-gpt2-refined")
fine_tuned_model = AutoModelForCausalLM.from_pretrained("finegptproject/fine-tuned-gpt2-refined")
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

#Framing effect check (humaneval #56)

function_prompt = """ def correct_bracketing(brackets: str): 

    This function checks if the string is a palindrome.

    brackets is a string of "<" and ">".
    return True if every opening bracket has a corresponding closing bracket.
    
    >>> correct_bracketing("<") False
    >>> correct_bracketing("<>") True
    >>> correct_bracketing("<<><>>") True
    >>> correct_bracketing("><<>") False
    """


# Generate responses from both models
fine_tuned_response = get_response(fine_tuned_model, tokenizer, function_prompt)
base_model_response = get_response(base_model, tokenizer, function_prompt)
     
# Print the responses
print("\n\nFine-tuned GPT-2 Response:\n", fine_tuned_response)
print("\n\nBase GPT-2 Response:\n", base_model_response)