import os
import openai
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
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
    chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": query}],stream = True)
    return chat.choices[0].message.content
def getDaVinviAnswer(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="explain "+prompt,
        temperature=1,
        max_tokens=4000
    )

    # Get the response text
    response_text = str(response['choices'][0]['text']).strip('\n\n')
    return response_text
def getGPTAnswer3():
    delay_time = 0.00 #  faster
    max_response_length = 4000
    answer = ''
    # ASK QUESTION
    prompt = input("Ask a question: ")
    start_time = time.time()

    response = openai.ChatCompletion.create(
        # CHATPG GPT API REQQUEST
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': f'{prompt}'}
        ],
        max_tokens=max_response_length,
        temperature=0,
        stream=True,  # this time, we set stream=True
    )

    for event in response:
        # STREAM THE ANSWER
        print(answer, end ='',flush= True) # Print the response
        # RETRIEVE THE TEXT FROM THE RESPONSE
        event_time = time.time() - start_time  # CALCULATE TIME DELAY BY THE EVENT
        event_text = event['choices'][0]['delta'] # EVENT DELTA RESPONSE
        answer = event_text.get('content', '') # RETRIEVE CONTENT
        time.sleep(delay_time)