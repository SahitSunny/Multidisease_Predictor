from transformers import GPT2LMHeadModel, GPT2Tokenizer

def genAI_model(user_input):
    user_input_string = ''
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # Input prompt
    prompt = "how to install CUDA for machine learning proccess"

    # Encode input
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate text
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)

    # Decode output
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

