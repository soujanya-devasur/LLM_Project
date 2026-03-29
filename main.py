from agent import ai_agent

print("AI Assistant Ready (type 'exit' to stop)")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    answer = ai_agent(user_input)

    print("AI:", answer)