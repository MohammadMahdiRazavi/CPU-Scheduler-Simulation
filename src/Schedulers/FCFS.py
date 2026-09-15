from collections import deque

class FCFS:
    def __init__(self):
        self.queue = deque()

    def add_process(self, pcb):
        self.queue.append(pcb)

    def get_next(self, time):
        if self.queue:
            return self.queue.popleft()
        return None

    def get_time_slice(self, pcb):
        return pcb.remaining_time