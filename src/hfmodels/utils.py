import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,AutoModel,CodeGenForCausalLM


def load_artefacts(model_path, model_class=AutoModel):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = model_class.from_pretrained(model_path)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    #model.eval()
    return model, tokenizer, device


def generate_tokens(model, tokenizer, device,input_text):
    input_ids = tokenizer.encode(input_text, return_tensors="pt").to(device)
    with torch.no_grad():
        output_ids = model.generate(input_ids, max_length=50, num_return_sequences=1)
    generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
    return {"generated_text": generated_text}
    

