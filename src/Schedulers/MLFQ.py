from collections import deque

class MLFQ:
    def __init__(self, boost_interval=1000):
        self.queues = [deque(), deque(), deque()]
        self.quantums = [5, 10, 20]
        self.level = {}          # pid -> level
        self.last_boost = 0
        self.boost_interval = boost_interval

    def add_process(self, pcb, from_io=False):
        pid = pcb.pid

        if pid not in self.level:
            self.level[pid] = 0
        elif from_io:
            #promotion after IO
            self.level[pid] = max(0, self.level[pid] - 1)

        self.queues[self.level[pid]].append(pcb)

    def get_next(self, time):
        self.priority_boost(time)
        for q in self.queues:
            if q:
                return q.popleft()
        return None

    def get_time_slice(self, pcb):
        return self.quantums[self.level[pcb.pid]]

    def on_quantum_expire(self, pcb):
        lvl = self.level[pcb.pid]
        if lvl < len(self.queues) - 1:
            self.level[pcb.pid] += 1
        self.queues[self.level[pcb.pid]].append(pcb)

    def priority_boost(self, time):
        if time - self.last_boost < self.boost_interval:
            return

        all_procs = []
        for q in self.queues:
            all_procs.extend(q)
            q.clear()

        for pcb in all_procs:
            self.level[pcb.pid] = 0
            self.queues[0].append(pcb)

        self.last_boost = time

    def higher_priority_exists(self, lvl):
        for i in range(lvl):
            if self.queues[i]:
                return True
        return False