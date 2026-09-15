import heapq

class PriorityScheduler:
    def __init__(self):
      self.queue = []

    def add_process(self, pcb):
        heapq.heappush(self.queue, (pcb.priority, pcb.arrival_time, pcb.pid, pcb))

    def age(self):
        newq = []
        for pr, at, pid, pcb in self.queue:
            pcb.priority = max(1, pcb.priority - 1)
            heapq.heappush(newq, (pcb.priority, at, pid, pcb))
        self.queue = newq

    def get_next(self, time):
        if self.queue:
            return heapq.heappop(self.queue)[3]
        return None

    def get_time_slice(self, pcb):
        return pcb.remaining_time