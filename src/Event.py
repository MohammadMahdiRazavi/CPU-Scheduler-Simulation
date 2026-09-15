class Event:
    def __init__(self, time, event_type, process=None):
        self.time = time
        self.event_type = event_type
        self.process = process


    def __lt__(self, other):
        return self.time < other.time