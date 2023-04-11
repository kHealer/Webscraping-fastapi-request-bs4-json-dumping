from typing import Dict
import json as _json
import datetime as _dt

def get_all_events()-> Dict:
    with open("events.json", encoding="utf-8") as events_file:
        data = _json.load(events_file)
    return data

def get_month_events(month:str)-> Dict:
    # with open("events.json", encoding="utf-8") as
    events = get_all_events()
    month = month.lower()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "this month isnt real you fool"
    
def get_events_of_day(month:str, day:int)-> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        day_events = events[month][str(day)]
        return day_events
    except KeyError:
        return "this day and month not valid"
    
def get_today():
    today = _dt.date.today()
    month = today.strftime("%B").lower()
    return get_events_of_day(month, today.day)