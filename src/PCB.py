class PCB:
    def __init__(self, pid, arrival, cpu_burst, io_burst, priority):
        self.pid = pid
        self.arrival_time = arrival
        self.cpu_burst = cpu_burst
        self.remaining_time = cpu_burst
        self.io_burst = io_burst
        self.priority = priority
        self.state = 'READY'


        # statistics
        self.start_time = None
        self.completion_time = None
        self.waiting_time = 0
        self.response_time = None