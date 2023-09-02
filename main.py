import queries
import spacy
import classifier
import clock
import string
import speech
import voice_input




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
    print("music work")
    #do alarm work
speech.say(ans)
##speech.say(clock.timeQuery("singapore time now"))
##speech.say(queries.getDaVinviAnswer("what is a diode"))





