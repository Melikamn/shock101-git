def reply(text: str) -> str:
    message = text.strip().lower()

    if not message:
        return "Please say something."

    if message in ("hello", "hi", "hey", "salam", "سلام"):
        return "Hello! How can I help you?"

    if "name" in message:
        return "My name is Echo-lite."

    if "help" in message:
        return "I can answer simple messages."

    return "I am still learning."
    
if __name__ == "__main__":
    user_input = input("You: ")
    print("Echo:", reply(user_input))
