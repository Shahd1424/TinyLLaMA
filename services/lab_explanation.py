# services/lab_explanation.py
from core.llm_client import LocalLLM
from core.prompts import LAB_PROMPT

llm = LocalLLM()

def explain_labs(lab_results: dict):
    prompt = f"{LAB_PROMPT}\nLab Results: {lab_results}"
    return llm.generate_response(prompt, context=lab_results)