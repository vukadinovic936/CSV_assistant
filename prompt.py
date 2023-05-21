import os
import openai
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
import pandas as pd

# load api key
with open('openai_key.txt') as f:
    key = f.readlines()
os.environ['OPENAI_API_KEY'] = key[0]

# load csv file (ex: titanic.csv)
csv_path = input("Enter the path of your csv file \n")
agent = create_csv_agent(OpenAI(temperature=0), csv_path , verbose=True)

# ask the question ex: What is the average fare?
query = input("Enter your query\n")
agent.run(query)