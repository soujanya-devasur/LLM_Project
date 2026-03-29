from groq import Groq
from config import API_KEY

client = Groq(api_key=API_KEY)

def ask_llm(question):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content