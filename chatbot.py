
import re

responses = {
    "greeting": "Hello! Welcome to our chatbot.",
    "hours": "Our business hours are 9 AM to 6 PM.",
    "product": "We provide quality products at affordable prices.",
    "return": "Products can be returned within 7 days.",
    "thanks": "You're welcome! Have a nice day."
}

print("===== Welcome to Chatbot =====")
print("Type 'bye' or 'exit' to stop.")

while True:
    user = input("\nYou: ").lower().strip()

    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    if re.search(r"\b(hello|hi|hey)\b", user):
        print("Bot:", responses["greeting"])

    elif re.search(r"\b(hours|time|open|close)\b", user):
        print("Bot:", responses["hours"])

    elif re.search(r"\b(product|products|price)\b", user):
        print("Bot:", responses["product"])

    elif re.search(r"\b(return|refund)\b", user):
        print("Bot:", responses["return"])

    elif re.search(r"\b(thanks|thank you)\b", user):
        print("Bot:", responses["thanks"])

    else:
        print("Bot: Sorry, I don't understand. Please try again.")
