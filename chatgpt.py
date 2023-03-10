import os
import sys
import time
import openai
from dotenv import load_dotenv


load_dotenv()  # Load environment variables from .env file

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable in your code



systemPrompt = { "role": "system", "content": "Use triple backticks with the language name for every code block in your markdown response, if any." }
data = []

def get_response(incoming_msg):
    if incoming_msg == "clear":
        data.clear()
        data.append({"role": "assistant", "content": 'hello'})
    else:  
        data.append({"role": "assistant", "content": incoming_msg})

    messages = [ systemPrompt ]
    messages.extend(data)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        content = response["choices"][0]["message"]["content"]
        return content
    except openai.error.RateLimitError as e:
        print(e)
        return ""