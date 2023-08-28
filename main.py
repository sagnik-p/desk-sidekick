import queries
import spacy
import speech
import clock
def extract_country_names(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geo-Political Entity label includes countries
            return ent.text
    return

def timeQuery(query):
    gmt_time = clock.get_current_gmt_time_hhmm()
    country_name_extracted = extract_country_names(query)
    speech.say("In " + country_name_extracted + " it is currently " + clock.strTime(clock.calculate_timezone_time(gmt_time, clock.utc_diff[country_name_extracted])))






#timeQuery("france time now")
speech.say(queries.getDaVinviAnswer("what is a diode"))









