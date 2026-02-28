# services/symptom_reasoning.py
from core.llm_client import LocalLLM
from core.prompts import SYMPTOM_PROMPT

llm = LocalLLM()

def reason_symptoms(symptoms: dict):
    prompt = f"{SYMPTOM_PROMPT}\nSymptoms: {symptoms}"
    return llm.generate_response(prompt, context=symptoms)