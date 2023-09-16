import WakeWord.RunModel
import queries
import classifier
import clock
import speech
from WakeWord.RunModel import isWWDetected
import voice_input

while True:
    if(WakeWord.RunModel.isWWDetected()):
        print("Listening:")
        q=voice_input.listen_and_recognize()
        print("query: "+q )
        type=classifier.classifyType(q)
        print("query type: "+type )
        ans="hello sir"
        if(type=='time'):
            ans = clock.timeQuery(q)
        elif(type=='explain'):
            ans = queries.getDaVinviAnswer(q,'explain')
        elif(type=='short'):
            ans = queries.getDaVinviAnswer((q))
        elif(type=="music"):
            print('music work')
            ##do music work
        elif(type=='alarm'):
            print(" work")
            #do alarm work
        speech.say(ans)
    ##speech.say(clock.timeQuery("singapore time now"))
    ##speech.say(queries.getDaVinviAnswer("what is a diode"))





