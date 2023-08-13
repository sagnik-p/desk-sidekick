import os
import openai
openai.api_key = "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"
def getGPTAnswer(query,type):
    if(type == "explain"):
        query = " in simple words, explain in details " + query
    elif(type == "short"):
        query = " in short, explain " + query
    print(query)
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}])
    return chat.choices[0].message.content

def getFinalAnswer(response):
    if(response.contains())