import os
import openai
file_path = "S:/key.txt"
if os.path.isfile(file_path):
    text_file = open(file_path, "r")
    data = text_file.read()
    text_file.close()
else:
    data = input("File not found, Enter API key")
openai.api_key= data
def getGPTAnswer(query,type):
    if(type == "explain"):
        query = " in simple words, explain in details " + query
    elif(type == "short"):
        query = " in short, explain " + query
    print(query)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
    return chat.choices[0].message.content