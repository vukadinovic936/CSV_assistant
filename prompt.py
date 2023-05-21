import os
import openai
from langchain.llms import OpenAI
from langchain.agents import create_csv_agent
import pandas as pd


os.environ['OPENAI_API_KEY'] = "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"
agent = create_csv_agent(OpenAI(temperature=0), 'titanic.csv', verbose=True)
agent.run("Fit a linear regression with Age column as a predictor and Fare column as a criterion and tell me what is the p-value, and thecorrelation coefficient")