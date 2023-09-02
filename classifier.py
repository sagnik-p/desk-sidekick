
from pyxdameraulevenshtein import damerau_levenshtein_distance, normalized_damerau_levenshtein_distance
def doesContain(st1,st2):
    '''use DL edit distance algorithm to find the similarity between two strings'''
    return damerau_levenshtein_distance(st1, st2)
def classifyType(query):
    '''Categories
    short: basic question
    explain: explain in detail
    music: control music actions
    time: ask for time of different countries
    alarm: manage alarms'''
    for i in ["alarm","set an alarm","timer"]:
        if (i in query):
            return "alarm"
    for i in ["time","what is the time"]:
        if (i in query):
            return "time"
    for i in ["explain","detail","describe","why"]:
        if (i in query):
            return "explain"
    for i in ["what","how","when"]:
        if(i in query):
            return "short"
    for i in ["play","music","song"]:
        if(i in query):
            return "music"
