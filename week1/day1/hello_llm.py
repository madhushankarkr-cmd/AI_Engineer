import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv("GROQ_API_KEY")
    
if not my_api_key:
    raise ValueError("api error")

Client = Groq(api_key = my_api_key)
model = "llama-3.3-70b-versatile"


message = {
    "role": "user",
    "prompt": "Do you know Alex"
}

messages =[message]

# response = Client.chat.completions.create(model=model,messages=messages)
# print(response)


 