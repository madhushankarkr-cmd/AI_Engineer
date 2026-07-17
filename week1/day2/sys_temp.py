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

role = "user"
prompt = "Suggest a nmae for my food company"

message_System = {
    "role" : "system",
    "content" : "You are my brand manager who supposed to give me name in one word "
}
message = {
    "role": role,
    "content": prompt
}

messages =[message_System, message]

#temperature default = 0 i change to 1

response = Client.chat.completions.create(model=model,messages=messages, temperature=1)
#print(response)

print("###########################")


answer = response.choices[0].message.content
print(answer)

 
