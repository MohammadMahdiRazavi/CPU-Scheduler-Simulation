import random
import copy

from Schedulers.PriorityScheduler import PriorityScheduler
from Schedulers.RoundRobin import RoundRobin
from Schedulers.FCFS import FCFS
from Schedulers.SJF import SJF
from Schedulers.MLFQ import MLFQ

import Simulator
from WorkloadGenerator import *
from Statistics import *


if __name__ == '__main__':
    random.seed(1)

    workloads = ['cpu', 'io', 'mixed']
    schedulers = {
        'FCFS': FCFS(),
        'SJF': SJF(),
        'PRIORITY': PriorityScheduler(),
        'RR': RoundRobin(quantum=20),
        'MLFQ': MLFQ()
    }

    for wl in workloads:
        print('\nWorkload:', wl)
        base = generate_processes(200, wl)

        for name, sch in schedulers.items():
            processes = copy.deepcopy(base)

            sim = Simulator.Simulator(sch)
            completed, busy, total = sim.run(processes)

            metrics = calculate_metrics(completed, busy, total)
            print(name, metrics)

            # save statistics
            save_results(wl, name, metrics)

            # save trace file
            save_trace(sim.trace, wl, name)

    #plots
    plots(workloads, ['Avg Turnaround', 'Avg Waiting', 'Avg Response', 'Fairness'])