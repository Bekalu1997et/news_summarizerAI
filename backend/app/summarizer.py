
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-4k-instruct")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-3-mini-4k-instruct")
summarizer = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_summary(text: str, length: str = "medium") -> str:
    prompts = {
        "short": "Summarize the following article in 1-2 sentences: \n\n",
        "medium": "Provide a concise 1-paragraph summary of the following articles \n\n",
        "long": "Provide a detailed multi-paragraph summary of the following articles \n\n"
    }
    prompt = prompts.get(length, prompts["medium"]) + text
    result = summarizer(prompt, max_new_tokens=300, temperature=0.7)[0]["generated_text"]
    return result