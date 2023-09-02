from datetime import datetime
import spacy
import datetime
import pytz


alarms=[]
def get_current_gmt_time_hhmm():
    gmt_timezone = pytz.timezone("Etc/GMT")
    gmt_time = datetime.datetime.now(gmt_timezone)
    time_format = "%H%M"
    gmt_time_hhmm = gmt_time.strftime(time_format)
    return gmt_time_hhmm

def convert_local_to_gmt():
    local_timezone = "Asia/Kolkata"
    local_time_hhmm = get_local_time_hhmm()
    local_time_format = "%H%M"
    local_time = datetime.datetime.strptime(local_time_hhmm, local_time_format)

    local_timezone = pytz.timezone(local_timezone)
    local_time = local_timezone.localize(local_time)

    gmt_timezone = pytz.timezone("Etc/GMT")
    gmt_time = local_time.astimezone(gmt_timezone)

    gmt_time_hhmm = gmt_time.strftime(local_time_format)
    return gmt_time_hhmm


def calculate_timezone_time(current_time, time_difference):
    new_hours_str=""
    new_mins_str=""
    if(time_difference[0]=="-"):
        new_hours=int(current_time[:2])-int(time_difference[1:3])
        new_mins=int(current_time[3:])-int(time_difference[3:])
        if(new_mins<0):
            new_mins+=60
            new_hours-=1

        if (new_hours < 0):
            new_hours +=24
    else:
        new_hours=int(current_time[:2])+int(time_difference[1:3])
        new_mins=int(current_time[2:])+int(time_difference[3:])
        if(new_mins>60):
            new_mins-=60
            new_hours+=1

        if(new_hours > 24):
            new_hours-=24
    new_hours_str = str(new_hours)
    new_mins_str = str(new_mins)
    if(new_mins<10):
        new_mins_str="0" + str(new_mins)
    if(new_hours<10):
        new_hours_str="0" + str(new_hours)
    print(new_hours_str + new_mins_str)
    return new_hours_str + new_mins_str


def extract_country_names(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "GPE":  # Geo-Political Entity label includes countries
            return ent.text
    return



utc_diff = {
    "afghanistan": "+0430",
    "armenia": "+0400",
    "azerbaijan": "+0400",
    "bahrain": "+0300",
    "bangladesh": "+0600",
    "bhutan": "+0600",
    "brunei": "+0800",
    "cambodia": "+0700",
    "china": "+0800",
    "east_timor": "+0900",
    "georgia": "+0400",
    "india": "+0530",
    "iran": "+0330",
    "iraq": "+0300",
    "israel": "+0300",
    "japan": "+0900",
    "jordan": "+0300",
    "kazakhstan": "+0600",
    "kuwait": "+0300",
    "kyrgyzstan": "+0600",
    "laos": "+0700",
    "lebanon": "+0300",
    "malaysia": "+0800",
    "maldives": "+0500",
    "mongolia": "+0800",
    "myanmar": "+0630",
    "nepal": "+0545",
    "north_korea": "+0900",
    "oman": "+0400",
    "pakistan": "+0500",
    "philippines": "+0800",
    "qatar": "+0300",
    "saudi_arabia": "+0300",
    "singapore": "+0800",
    "south_korea": "+0900",
    "sri_lanka": "+0530",
    "syria": "+0300",
    "taiwan": "+0800",
    "tajikistan": "+0500",
    "thailand": "+0700",
    "turkmenistan": "+0500",
    "united_arab_emirates": "+0400",
    "uzbekistan": "+0500",
    "vietnam": "+0700",
    "yemen": "+0300",
    "indonesia": "+0700",
    "albania": "+0200",
    "andorra": "+0200",
    "austria": "+0200",
    "belarus": "+0300",
    "belgium": "+0200",
    "bosnia_and_herzegovina": "+0200",
    "bulgaria": "+0300",
    "croatia": "+0200",
    "cyprus": "+0300",
    "czech_republic": "+0200",
    "denmark": "+0200",
    "estonia": "+0300",
    "finland": "+0300",
    "france": "+0200",
    "germany": "+0200",
    "greece": "+0300",
    "hungary": "+0200",
    "iceland": "+0000",
    "ireland": "+0100",
    "italy": "+0200",
    "kosovo": "+0200",
    "latvia": "+0300",
    "liechtenstein": "+0200",
    "lithuania": "+0300",
    "luxembourg": "+0200",
    "malta": "+0200",
    "moldova": "+0300",
    "monaco": "+0200",
    "montenegro": "+0200",
    "netherlands": "+0200",
    "north_macedonia": "+0200",
    "norway": "+0200",
    "poland": "+0200",
    "portugal": "+0100",
    "romania": "+0300",
    "russia": "+0300",
    "san_marino": "+0200",
    "serbia": "+0200",
    "slovakia": "+0200",
    "slovenia": "+0200",
    "spain": "+0200",
    "sweden": "+0200",
    "switzerland": "+0200",
    "ukraine": "+0300",
    "united_kingdom": "+0100",
    "vatican_city": "+0200"
    # ... (add more countries)
}

def get_local_time_hhmm():
    now = datetime.datetime.now()
    time_format = "%H%M"
    local_time_hhmm = now.strftime(time_format)
    return local_time_hhmm


def strTime(time):
    hours_str=time[0:2]
    if(hours_str[0] == "0"):
        hours_str=hours_str[1]
    mins_str=time[2:]
    x=''
    if(int(hours_str)>12):
        x=' p m'
    else:
        x=' a m'
    return hours_str +' '+ mins_str + x

def timeQuery(query):
    gmt_time = get_current_gmt_time_hhmm()
    country_name_extracted = extract_country_names(query)
    return "In " + country_name_extracted + " it is currently " + strTime(calculate_timezone_time(gmt_time, utc_diff[country_name_extracted]))

def setAlarm(strtime):
    if((strtime in alarms)):
        return "Alarm already set for" + strTime(strtime)
    alarms.append(strtime)
    return "Your alarm is set for " + strTime(strtime)