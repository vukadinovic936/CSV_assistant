# CSV_assistant

To connect with OpenAI, create a file openai_key.txt and paste your api key there.

If you want to work with titanic.csv dataset you can download it from here https://github.com/datasciencedojo/datasets/blob/master/titanic.csv

Sample dataset is a simple two-liner, and you can download it from this repo sample.csv

For a demo usage run main.py file. Here is an example:
`python main.py`.

If you want to allow the assitant to make plots, change the first line of main.py to ALLOW_PLOTTING=True
and then run `python main.py`.
 


The following three interactions demonstrate features of CSV assistant.
Interaction 1 shows that the assistant acts as an agent, it has a memory buffer, it can load many csv files, acts as a chatbot, and can perform data science queries.
![alt text](https://github.com/vukadinovic936/CSV_assistant/blob/main/Interaction1.png)


Interaction 2 shows that the assistant can train and load machine learning models.
![alt text](https://github.com/vukadinovic936/CSV_assistant/blob/main/Interaction2.png)


Interaction 3 shows that the assistant can make plots.
![alt text](https://github.com/vukadinovic936/CSV_assistant/blob/main/Interaction3.png)