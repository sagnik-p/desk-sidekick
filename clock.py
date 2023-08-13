from datetime import *
from datetime import datetime, timedelta


def calculate_timezone_time(current_time, time_difference):
    try:
        current_time_obj = datetime.strptime(current_time, "%H%M")
        time_difference_obj = timedelta(hours=int(time_difference[:2]), minutes=int(time_difference[2:]))

        new_time_obj = current_time_obj + time_difference_obj

        new_time_formatted = new_time_obj.strftime("%H%M")

        return new_time_formatted
    except ValueError:
        return "Invalid time format. Please use HHMM format."


# Example usage
current_time = "2358"  # Replace this with your current time in HHMM format
time_difference = "0900"  # Replace this with the time difference in HHMM format

new_time = calculate_timezone_time(current_time, time_difference)
print(f"New time at the specified timezone: {new_time}")

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