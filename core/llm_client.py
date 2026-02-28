# core/llm_client.py
from transformers import LlamaForCausalLM, LlamaTokenizer
import torch
from core.guardrails import enforce_guardrails
from config import MODEL_NAME, MAX_TOKENS, TEMPERATURE

class LocalLLM:
    def __init__(self, model_name=MODEL_NAME):
        print(f"Loading model {model_name}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tokenizer = LlamaTokenizer.from_pretrained(model_name, local_files_only=True)
        
        # تحميل النموذج مع تجاوز weights_only=True الافتراضي
        self.model = LlamaForCausalLM.from_pretrained(
            model_name,
            device_map=None,
            torch_dtype=torch.float16,
            low_cpu_mem_usage=True,
            local_files_only=True,
            torch_load_args={"weights_only": False}  # مهم لتجنب pickle error
        ).to(self.device)

    def generate_response(self, prompt: str, context: dict = {}):
        full_prompt = f"{prompt}\nContext: {context}"
        inputs = self.tokenizer(full_prompt, return_tensors="pt").to(self.device)
        outputs = self.model.generate(**inputs, max_new_tokens=MAX_TOKENS)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return enforce_guardrails(response)


# إنشاء instance عالمي يمكن استدعاؤه
llm_instance = LocalLLM()

def generate_response(prompt: str, context: dict = {}):
    return llm_instance.generate_response(prompt, context)