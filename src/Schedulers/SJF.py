import heapq

class SJF:
    def __init__(self):
        self.queue = []

    def add_process(self, pcb):
        heapq.heappush(self.queue, (pcb.remaining_time, pcb.arrival_time, pcb.pid, pcb))

    def get_next(self, time):
        if self.queue:
            return heapq.heappop(self.queue)[3]
        return None

    def get_time_slice(self, pcb):
        return pcb.remaining_time