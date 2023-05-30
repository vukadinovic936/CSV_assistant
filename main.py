import openai
from langchain.llms import OpenAI
import pandas as pd
import os
from csv_chatbot import create_csv_chatbot

def read_from_txt(path):
    with open(path) as f:
        text = f.readlines()
    return text[0]

# load api key
os.environ['OPENAI_API_KEY'] = read_from_txt("openai_key.txt")

welcome_text=read_from_txt("welcome.txt")

user_input = input(welcome_text+"\n")
csv_names = [pd.read_csv(df_path) for df_path in user_input.replace(" ",'').split(",")]

agent = create_csv_chatbot(OpenAI(temperature=0), csv_names, verbose=True)

# ask the question ex: What is the average fare?
while((query:=input("Enter your query\n"))!="exit"):
   agent.run(query) 