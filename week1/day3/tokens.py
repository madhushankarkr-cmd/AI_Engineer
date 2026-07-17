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
# 3 prompts
prompt1 = "Hi!"
prompt2 = "explain time travel in details"
prompt3 = "write 1000 words essay on machine learning"

prompts = [prompt1,prompt2,prompt3]
for prompt in prompts:
    message = {
    "role": role,
    "content": prompt
    }
    messages =[message]
    response = Client.chat.completions.create(model=model,messages=messages)
    usage = response.usage
    print(f"Prompt: {prompt} --> your tokens: {usage.prompt_tokens}  --> completition_tokens: {usage.completion_tokens} total tokens: {usage.total_tokens}")
# prompt = "Do you know Ms Dhoni"


# print(response)

# print("###########################")


# answer = response.choices[0].message.content
# print(answer)

 
