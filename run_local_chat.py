# # run_local_chat.py

# from core.llm_client import generate_response
# from services.symptom_reasoning import reason_symptoms
# from services.lab_explanation import explain_labs
# from services.next_steps import generate_next_steps

# # مثال للأعراض والتحاليل
# user_input = {
#     "symptoms": {"headache": "mild", "fever": "low"},
#     "labs": {"WBC": 8000, "RBC": 4.5}
# }

# # 1️⃣ تحليل الأعراض
# symptom_context = reason_symptoms(user_input["symptoms"])

# # 2️⃣ شرح التحاليل
# lab_context = explain_labs(user_input["labs"])

# # 3️⃣ توليد الخطوات القادمة
# next_steps_context = generate_next_steps(symptom_context, lab_context)

# # 4️⃣ توليد رد من الـ LLM
# prompt = f"""
# Symptoms: {user_input['symptoms']}
# Symptom reasoning: {symptom_context}
# Lab reasoning: {lab_context}
# Next steps suggestions: {next_steps_context}
# """
# response = generate_response(prompt, context={})

# print("=== Response ===")
# print(response)

# run_local_chat.py
from core.llm_client import generate_response

def main():
    print("Local TinyLlama chat. اكتب 'exit' للخروج.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = generate_response(user_input)
        print(f"TinyLlama: {response}\n")

if __name__ == "__main__":
    main()