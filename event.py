class Event:
    def __init__(self, title, location, start_time, duration, owner, participants):
        self.title = title
        self.duration = duration
        self.start_time = start_time
        self.location = location
        self.owner = owner
        self.participants = participants

