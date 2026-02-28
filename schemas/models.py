# schemas/models.py
from pydantic import BaseModel
from typing import Dict

class SymptomRequest(BaseModel):
    symptoms: Dict[str, str]

class LabRequest(BaseModel):
    labs: Dict[str, float]

class NextStepsRequest(BaseModel):
    info: Dict[str, str]