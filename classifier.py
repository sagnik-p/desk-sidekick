import string
def doesContain(st1,st2):
    '''use DL edit distance algorithm to find the similarity between two strings'''

def classifyType(query):
    '''Categories
    short: basic question
    explain: explain in detail
    music: control music actions
    time: ask for time of different countries
    alarm: manage alarms'''
    for i in ["alarm","set an alarm","timer"]:
        if(query.index(i)):
            return "alarm"
    for i in ["time","what is the time"]:
        if(query.index(i)):
            return "alarm"
    for i in ["explain","detail","describe","why"]:
        if(query.index(i)):
            return "explain"
    for i in ["what","how","when"]:
        if(query.index(i)):
            return "short"
    for i in ["play","music","song"]:
        if(query.index(i)):
            return "song"