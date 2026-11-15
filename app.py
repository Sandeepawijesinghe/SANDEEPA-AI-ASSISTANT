
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load API Key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("API Key not found! Check your .env file.")

# Connect to OpenAI
client = OpenAI(api_key=api_key)

# Conversation history
conversation = [
    {
        "role": "system",
        "content": (
            "You are SANDEEPA AI, a helpful and intelligent personal "
            "AI assistant. Reply naturally and clearly. "
            "Use Sinhala when the user speaks Sinhala."
        )
    }
]

# Welcome screen
print("\n" + "=" * 40)
print("       SANDEEPA AI ASSISTANT")
print("=" * 40)
print("AI Assistant is ready!")
print("Type 'exit' to close the assistant.")
print("-" * 40)

# Continuous chat
while True:
    try:
        user_message = input("\nYou: ").strip()

        if not user_message:
            continue

        if user_message.lower() in ["exit", "quit", "bye"]:
            print("\nSANDEEPA AI: Goodbye! See you again. 😊")
            break

        conversation.append({
            "role": "user",
            "content": user_message
        })

        response = client.responses.create(
            model="gpt-5.5",
            input=conversation
        )

        ai_reply = response.output_text

        print("\nSANDEEPA AI:", ai_reply)

        conversation.append({
            "role": "assistant",
            "content": ai_reply
        })

    except KeyboardInterrupt:
        print("\n\nSANDEEPA AI: Chat closed. Goodbye!")
        break

    except Exception as error:
        print("\nError:", error)
        print("Please try again.")

print("\nThank you for using SANDEEPA AI!")
