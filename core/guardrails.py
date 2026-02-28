def enforce_guardrails(text: str) -> str:
    disallowed_phrases = ["diagnosis", "treatment", "emergency", "prescribe"]
    for phrase in disallowed_phrases:
        text = text.replace(phrase, "[REDACTED]")

    text += "\n\nDisclaimer: This response is for informational purposes only."
    return text