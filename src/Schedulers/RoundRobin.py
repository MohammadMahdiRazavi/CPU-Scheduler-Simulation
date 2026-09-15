from collections import deque

class RoundRobin:
    def __init__(self, quantum):
        self.queue = deque()
        self.quantum = quantum

    def add_process(self, pcb):
        self.queue.append(pcb)

    def get_next(self, time):
        if self.queue:
            return self.queue.popleft()
        return None

    def get_time_slice(self, pcb):
        return min(self.quantum, pcb.remaining_time)