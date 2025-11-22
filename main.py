import os
from google import genai
from google.genai.types import GenerateContentConfig

try:
    client = genai.Client()
except Exception:
    print("Error: The GEMINI_API_KEY environment variable is not set or invalid.")
    print("Please set your API key to run the code.")
    exit()

SYSTEM_INSTRUCTION = (
    "You are a helpful, professional, and empathetic AI medical assistant. "
    "Your task is to conduct a **10-question diagnostic interview** to determine "
    "the most likely condition based on the user's symptoms. "
    "Start by asking the first question. After each of the first 9 user responses, "
    "you MUST ask the next question. Do NOT provide a diagnosis until after the "
    "user has answered the 10th question. After the 10th answer, you MUST provide "
    "your final assessment, including the **most likely disease**, a **brief explanation** "
    "of why you concluded that, and a **strong disclaimer** that you are not a real doctor "
    "and the user MUST consult a healthcare professional. "
    "Ensure your questions are focused on common symptoms and medical history."
)

config = GenerateContentConfig(
    system_instruction=SYSTEM_INSTRUCTION,
    temperature=0.2 
)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=config
)

def run_disease_detector():
    """Runs the 10-question diagnostic chat session."""
    print("--- 🩺 AI Symptom Checker: 10 Questions to a Possible Diagnosis ---")
    print("Please answer the questions honestly. Remember, this is NOT medical advice.")
    print("-" * 60)
    
    initial_response = chat.send_message("Start the 10-question interview.")
    print(f"AI: {initial_response.text}")

    for i in range(1, 11):
        try:
            user_input = input(f"Your Answer ({i}/10): ")
            ai_response = chat.send_message(user_input)
            print(f"AI: {ai_response.text}")

            if i == 10:
                print("\n--- Diagnostic Session Complete ---")
                break 
            
        except Exception as e:
            print(f"\nAn error occurred during the conversation: {e}")
            break

if __name__ == "__main__":
    run_disease_detector()
