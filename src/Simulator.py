import heapq
from Event import Event


class Simulator:
    def __init__(self, scheduler, context_switch=2, aging_interval=50):
        self.scheduler = scheduler
        self.context_switch = context_switch
        self.aging_interval = aging_interval

        self.clock = 0
        self.cpu_busy = 0
        self.completed = []
        self.trace = []

        self.last_aging = 0

    def run(self, processes):
        # reset
        self.clock = 0
        self.cpu_busy = 0
        self.completed = []
        self.trace = []
        self.last_aging = 0

        event_queue = []
        for p in processes:
            heapq.heappush(
                event_queue,
                Event(p.arrival_time, 'ARRIVAL', p)
            )

        current = None
        last_pid = None
        remaining = len(processes)

        while remaining > 0:

            #Aging (Priority)
            if hasattr(self.scheduler, 'age'):
                if self.clock - self.last_aging >= self.aging_interval:
                    self.scheduler.age()
                    self.last_aging = self.clock

            #Handle events
            while event_queue and event_queue[0].time <= self.clock:
                ev = heapq.heappop(event_queue)

                if ev.event_type == 'ARRIVAL':
                    self.scheduler.add_process(ev.process)

                elif ev.event_type == 'IO_COMPLETE':
                    # for MLFQ
                    if 'from_io' in self.scheduler.add_process.__code__.co_varnames:
                        self.scheduler.add_process(ev.process, from_io=True)
                    else:
                        self.scheduler.add_process(ev.process)

            #Arrival-based preemption (MLFQ)
            if current and hasattr(self.scheduler, 'higher_priority_exists'):
                lvl = self.scheduler.level[current.pid]
                if self.scheduler.higher_priority_exists(lvl):
                    current.state = 'READY'
                    self.scheduler.add_process(current)
                    current = None

            #Select next
            if current is None:
                next_proc = self.scheduler.get_next(self.clock)
                if next_proc is None:
                    self.clock += 1
                    continue

                #context switch
                if last_pid is not None and last_pid != next_proc.pid:
                    cs_start = self.clock
                    self.clock += self.context_switch
                    self.trace.append((cs_start, self.clock, 'CS'))

                current = next_proc
                last_pid = current.pid
                current.state = 'RUNNING'

                if current.start_time is None:
                    current.start_time = self.clock
                    current.response_time = self.clock - current.arrival_time

            #Execute
            ts = self.scheduler.get_time_slice(current)
            run = min(ts, current.remaining_time)

            start = self.clock
            self.clock += run
            self.cpu_busy += run
            current.remaining_time -= run
            self.trace.append((start, self.clock, current.pid))

            #IO block (MLFQ only)
            if (hasattr(current, 'io_burst') and
                current.io_burst > 0 and
                current.remaining_time > 0 and
                hasattr(self.scheduler, 'higher_priority_exists')):

                io_done = self.clock + current.io_burst
                heapq.heappush(
                    event_queue,
                    Event(io_done, 'IO_COMPLETE', current)
                )
                current.state = 'BLOCKED'
                current = None
                continue

            #Completion
            if current.remaining_time == 0:
                current.completion_time = self.clock
                self.completed.append(current)
                remaining -= 1
                current = None

            #Quantum expire / requeue
            else:
                current.state = 'READY'
                if hasattr(self.scheduler, 'on_quantum_expire'):
                    self.scheduler.on_quantum_expire(current)
                else:
                    self.scheduler.add_process(current)
                current = None

        return self.completed, self.cpu_busy, self.clock