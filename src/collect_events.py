import datetime as _dt
from typing import Iterator, Dict
import scraper as _scraper
import json as _json

def _date_range(start_date: _dt.date, end_date: _dt.date) -> Iterator[_dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + _dt.timedelta(n)

def create_events_dict() -> Dict:
    events = dict()
    start_date = _dt.date(2020, 1, 1)
    end_date = _dt.date(2021, 1, 1)

    for date in _date_range(start_date, end_date):
        # print(date)
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()

        events[month][date.day] = _scraper.events_of_the_day(month, date.day)
    return events
# create_events_dict()
# print(create_events_dict())
if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", mode="w", encoding="utf-8") as events_file:
        _json.dump(events, events_file, ensure_ascii=False)