# api/routes.py
from fastapi import FastAPI
from schemas.models import SymptomRequest, LabRequest, NextStepsRequest
from services import symptom_reasoning, lab_explanation, next_steps

app = FastAPI(title="Medical Reasoning API")

@app.post("/reasoning/symptoms")
def symptoms_endpoint(req: SymptomRequest):
    return {"response": symptom_reasoning.reason_symptoms(req.symptoms)}

@app.post("/reasoning/labs")
def labs_endpoint(req: LabRequest):
    return {"response": lab_explanation.explain_labs(req.labs)}

@app.post("/reasoning/full")
def full_endpoint(req: NextStepsRequest):
    return {"response": next_steps.safe_next_steps(req.info)}