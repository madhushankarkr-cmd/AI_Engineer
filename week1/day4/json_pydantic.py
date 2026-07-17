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

#structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name : str
    email : str
    address : str
    contact_number : int
    issue: str
schema= Ticket.model_json_schema()

response_format={
    "type": "json_object"
}

system_prompt=f""" 
Extract the personal information from the ticket based on this schema and give me a json output
{schema}
"""

message_system={
    "role": "system",
    "content": system_prompt
}
text="hello my name is alex. i have an iphone which not working. My address is Patna.My email is dfghj@gmail.com.My contact number is 456789"
prompt = f"""
This is a customer ticket please extract the personal details from this.
{text}
"""

message = {
    "role": role,
    "content": prompt
}

messages =[message_system,message]

response = Client.chat.completions.create(model=model,messages=messages,response_format=response_format)


print("###########################")


answer = response.choices[0].message.content
print(answer)


#how to read

import json   
raw_json=answer
data_file=json.loads(raw_json)
ticket = Ticket(**data_file)

print(ticket.name)
print(ticket.email)
print(ticket.contact_number)
print(ticket.address)
print(ticket.issue)
 
