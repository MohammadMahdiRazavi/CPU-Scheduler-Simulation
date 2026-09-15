import random
import PCB
import os

def generate_processes(n=100, workload='mixed'):
    processes = []
    time = 0
    for i in range(n):
        inter_arrival = int(random.expovariate(1/10))
        time += inter_arrival

        if workload == 'cpu':
            cpu = random.randint(80, 120)
            io = random.randint(10, 20)
        elif workload == 'io':
            cpu = random.randint(10, 20)
            io = random.randint(80, 120)
        else:
            cpu = max(1, int(random.gauss(50, 20)))
            io = random.randint(10, 100)


        priority = random.randint(1, 10)
        processes.append(PCB.PCB(i, time, cpu, io, priority))
    return processes

def save_trace(trace, workload, scheduler_name):
    os.makedirs('data/trace_files', exist_ok=True)

    filename = f'{workload}_{scheduler_name}_trace.txt'
    path = os.path.join('data', 'trace_files', filename)

    with open(path, 'w') as f:
        f.write('start end pid\n')
        for start, end, pid in trace:
            f.write(f'{start} {end} {pid}\n')