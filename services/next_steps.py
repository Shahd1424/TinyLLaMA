# services/next_steps.py
from core.llm_client import LocalLLM
from core.prompts import NEXT_STEPS_PROMPT

llm = LocalLLM()

def safe_next_steps(info: dict):
    prompt = f"{NEXT_STEPS_PROMPT}\nPatient Info: {info}"
    return llm.generate_response(prompt, context=info)