from datetime import *
from datetime import datetime, timedelta
import datetime
import pytz
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


# Example usage




utc_diff = {
    "united states": "-0400",  # Eastern Daylight Time
    "canada": "-0400",  # Eastern Daylight Time
    "united kingdom": "+0100",  # British Summer Time
    "australia": "+1000",  # Australian Eastern Standard Time
    "india": "+0530",  # Indian Standard Time
    "germany": "+0200",  # Central European Summer Time
    "france": "+0200",  # Central European Summer Time
    "japan": "+0900",  # Japan Standard Time
    "china": "+0800",  # China Standard Time
    "brazil": "-0300",  # Brasília Time
    "mexico": "-0500",  # Central Daylight Time
    "russia": "+0300",  # Moscow Standard Time
    "south korea": "+0900",  # Korea Standard Time
    "italy": "+0200",  # Central European Summer Time
    "spain": "+0200",  # Central European Summer Time
    "canada": "-0600",  # Central Daylight Time
    "netherlands": "+0200",  # Central European Summer Time
    "turkey": "+0300",  # Turkey Time
    "australia": "+0800",  # Australian Western Standard Time
    "indonesia": "+0700",  # Western Indonesia Time
    "saudi arabia": "+0300",  # Arabian Standard Time
    "switzerland": "+0200",  # Central European Summer Time
    "argentina": "-0300",  # Argentina Time
    "sweden": "+0200",  # Central European Summer Time
    "belgium": "+0200",  # Central European Summer Time
    "austria": "+0200",  # Central European Summer Time
    "norway": "+0200",  # Central European Summer Time
    "uae": "+0400",  # Gulf Standard Time
    "poland": "+0200",  # Central European Summer Time
    "south africa": "+0200",  # South Africa Standard Time
    "thailand": "+0700",  # Indochina Time
    "malaysia": "+0800",  # Malaysia Standard Time
    "singapore": "+0800",  # Singapore Standard Time
    "greece": "+0300",  # Eastern European Summer Time
    "ukraine": "+0300",  # Eastern European Summer Time
    "philippines": "+0800",  # Philippine Time
    "portugal": "+0100",  # Western European Summer Time
    "egypt": "+0200",  # Eastern European Summer Time
    "hong kong": "+0800",  # Hong Kong Time
    "colombia": "-0500",  # Colombia Time
    "denmark": "+0200",  # Central European Summer Time
    "finland": "+0300",  # Eastern European Summer Time
    "chile": "-0400",  # Chile Standard Time
    "ireland": "+0100",  # Irish Standard Time
    "new zealand": "+1200",  # New Zealand Standard Time
    "peru": "-0500",  # Peru Time
    "vietnam": "+0700",  # Indochina Time
}
def get_local_time_hhmm():
    now = datetime.datetime.now()
    time_format = "%H%M"
    local_time_hhmm = now.strftime(time_format)
    return local_time_hhmm

def strTime(time):
    hours_str=time[0:2]
    mins_str=time[2:]
    x=''
    if(int(hours_str)>12):
        x=' p m'
    else:
        x=' a m'
    return hours_str +' '+ mins_str + x

