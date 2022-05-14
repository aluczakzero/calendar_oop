from custom_calendar import Calendar
from data.utils import EventGenerator
from pprint import pprint as pp

data = EventGenerator()
data.generate(500)
c = Calendar(data.events)

result = c.get_events_by_date('01-01-2023 00:00')
print(result, len(result))
c.remove_event('17-05-2022 9:00')
# pp(c)
