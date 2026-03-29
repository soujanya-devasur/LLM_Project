from llm import ask_llm

def ai_agent(user_input):

    if "add" in user_input:
        numbers = [int(s) for s in user_input.split() if s.isdigit()]
        if len(numbers) >= 2:
            return str(numbers[0] + numbers[1])

    return ask_llm(user_input)