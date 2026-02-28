from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "../models/falcon-7b-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    torch_dtype="auto",
    low_cpu_mem_usage=True
)

def medical_chatbot(user_input):
    system_prompt = "You are a helpful and safe medical assistant."
    prompt = f"{system_prompt}\nUser: {user_input}\nAssistant:"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=150)
    answer = tokenizer.decode(outputs[0])
    answer = answer.split("User:")[0].strip()
    return answer

# تجربة Chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", medical_chatbot(user_input))