from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai


app=FastAPI()



class Prompt(BaseModel):
  prompt:str

def apple(pr):
  

  genai.configure(api_key="AIzaSyCK0cv5XIP4GA5wdldhDLXp0foJitgKaI8")
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(pr)
  return(response.text)
  


@app.post("/chat")
def banana(data:Prompt):
  orange=apple(data.prompt)
  return{"thammudu":orange}
