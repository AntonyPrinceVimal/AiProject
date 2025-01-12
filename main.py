from fastapi import FastAPI
from pydantic import BaseModel



app=FastAPI()



class Prompt(BaseModel):
  prompt:str

def apple(pr):
  import google.generativeai as genai

  genai.configure(api_key="AIzaSyCK0cv5XIP4GA5wdldhDLXp0foJitgKaI8")
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(pr)
  return(response.text)
  
apply=apple("give one word starts with w")
print(apply)

@app.post("/chat")
def banana(data:Prompt):
  orange=apple(data.prompt)
  return{"thammudu":orange}
