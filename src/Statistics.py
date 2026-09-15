import json
import os
import matplotlib.pyplot as plt

def calculate_metrics(processes, cpu_busy, total_time):
    n = len(processes)

    avg_tat = sum(p.completion_time - p.arrival_time for p in processes) / n
    avg_wait = sum(
        p.completion_time - p.arrival_time - p.cpu_burst
        for p in processes
    ) / n
    avg_resp = sum(p.response_time for p in processes) / n
    cpu_util = (cpu_busy / total_time) * 100
    throughput = n / total_time

    norm = []
    for p in processes:
        if p.cpu_burst > 0:
            norm.append((p.completion_time - p.arrival_time) / p.cpu_burst)

    denom = sum(x * x for x in norm)

    if denom == 0:
        fairness = 1.0
    else:
        fairness = (sum(norm) ** 2) / (n * denom)

    return {
        'Avg Turnaround': avg_tat,
        'Avg Waiting': avg_wait,
        'Avg Response': avg_resp,
        'CPU Util': cpu_util,
        'Throughput': throughput,
        'Fairness': fairness
    }

def save_results(workload, scheduler, metrics):
    os.makedirs('data/results', exist_ok=True)
    path = f'data/results/{workload}.json'

    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
    else:
        data = {}

    data[scheduler] = metrics

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)


def plots(workloads, metrics):
    for wl in workloads:
        with open(f'data/results/{wl}.json') as f:
            data = json.load(f)

        for m in metrics:
            names = list(data.keys())
            values = [data[n][m] for n in names]

            plt.figure()
            plt.bar(names, values)
            plt.title(f'{m} - {wl}')
            plt.ylabel(m)
            plt.xlabel('Scheduler')
            plt.savefig(f'data/results/{wl}_{m}.png')
            plt.close()