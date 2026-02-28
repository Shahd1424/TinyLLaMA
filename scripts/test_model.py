
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

model_path = r"E:\Graduation Project\Falcon 7B-Instruct\models\tinyllama"

tokenizer = LlamaTokenizer.from_pretrained(model_path, local_files_only=True)

# نستخدم map_location لتحديد CPU (أو GPU لو متاح)
state_dict = torch.load(f"{model_path}/pytorch_model.bin", map_location="cpu", weights_only=False)

# نمرر الـ state_dict مباشرة عند إنشاء الموديل
model = LlamaForCausalLM.from_pretrained(
    model_path,
    state_dict=state_dict,
    torch_dtype=torch.float32,
    device_map="auto",
    local_files_only=True
)

# اختبار سريع
prompt = "You are a medical assistant. Explain what is a fever."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=150)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))