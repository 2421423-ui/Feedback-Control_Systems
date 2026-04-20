# local_chatbot.py

from openai import OpenAI

# Connect to LM Studio (local server)
client = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"  # any string works
)

MODEL_NAME = "google/gemma-4-4b"

# Store conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful and friendly AI assistant. "
            "The user's name is Samuel Sariola. "
            "Greet the user naturally and respond clearly and concisely."
        )
    }
]

print("💬 Chatbot started (type 'exit' to quit)\n")

# Initial greeting
print("AI: Hi, Samuel Sariola! Nice to meet you 😊")
print("AI: What would you like to do today?\n")

while True:
    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("AI: Goodbye! Have a great day 👋")
        break

    # Save user message
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:
        # Generate response
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"⚠️ Error: {e}"

    # Print AI response
    print("AI:", reply)

    # Save AI response
    messages.append({
        "role": "assistant",
        "content": reply
    })
