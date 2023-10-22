import WakeWord.RunModel
import queries
import classifier
import clock
import speech
import systemutil
import voice_input

while True:
    if(WakeWord.RunModel.isWWDetected()):
        print("Listening:")
        q=voice_input.listen_and_recognize()
        print("query heard: "+q )
        type=classifier.classifyType(q)
        print("query type: "+type )
        if(type=='time'):
            ans = clock.timeQuery(q)
        elif(type=='explain'):
            ans = queries.getDaVinviAnswer(q,'explain')
        elif(type=='short'):
            ans = queries.getDaVinviAnswer(q,'short')
        elif(type=='alarm'):
            print("alarm work")
            clock.alarmManager()
        elif(type=='system'):
            systemutil.openApp(q)
            ans='opened successfully'
        else:
            ans = "Sorry Sir, I didnt get you"
        speech.say(ans)




