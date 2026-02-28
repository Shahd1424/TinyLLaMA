# config.py
import os

# MODEL_NAME = os.getenv("MODEL_NAME", "models/falcon-7b-instruct")
# MAX_TOKENS = int(os.getenv("MAX_TOKENS", 150))
# TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))

# config.py
MODEL_NAME = "models/tinyllama"  # المسار المحلي للنموذج
MAX_TOKENS = 256
TEMPERATURE = 0.7