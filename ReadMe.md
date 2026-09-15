# 🖥️ CPU Scheduling Simulator

A **Discrete Event CPU Scheduling Simulator** designed for studying, comparing, and visualizing classical operating-system scheduling algorithms under different process workloads.

The simulator models process execution over simulated time and evaluates schedulers using both traditional CPU-scheduling metrics and higher-level system-performance indicators. It supports CPU-bound, I/O-bound, and mixed workloads and records execution traces that can be used to analyze scheduling behavior through Gantt charts.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Implemented Scheduling Algorithms](#-implemented-scheduling-algorithms)
- [Workload Generation](#-workload-generation)
- [Performance Metrics](#-performance-metrics)
- [Execution Traces](#-execution-traces)
- [Project Workflow](#-project-workflow)
- [How to Run](#-how-to-run)
- [Customizing the Simulation](#-customizing-the-simulation)
- [Output](#-output)
- [Why Discrete-Event Simulation?](#-why-discrete-event-simulation)
- [Use Cases](#-use-cases)
- [Conclusion](#-conclusion)

---

## 🔎 Overview

CPU scheduling is one of the fundamental responsibilities of an operating system. When multiple processes compete for CPU time, the scheduler determines **which process should run, when it should run, and for how long**.

Different scheduling policies optimize different objectives. For example:

- **FCFS** prioritizes simplicity and arrival order.
- **SJF** attempts to reduce average waiting time by favoring shorter jobs.
- **Priority Scheduling** favors processes according to their priority.
- **Round Robin** emphasizes fairness and responsiveness.
- **MLFQ** dynamically adapts scheduling decisions according to process behavior and queue priorities.

This project provides a controlled environment for observing these differences experimentally rather than studying the algorithms only theoretically.

---

## ✨ Features

- 📊 **Discrete-event simulation** of CPU scheduling
- ⚙️ Multiple scheduling algorithms in a common simulation framework
- 🧑‍💻 Support for different process/workload types
- 🔄 Both **preemptive and non-preemptive** scheduling strategies
- ⭐ Priority scheduling with **aging** to reduce starvation
- ⏱️ Configurable **Round Robin time quantum**
- 🔀 Dynamic **Multi-Level Feedback Queue (MLFQ)** scheduling
- 📈 Detailed performance metrics
- 📝 Persistent JSON results
- 🖼️ Execution traces suitable for Gantt-chart visualization
- ⚖️ Comparison of scheduler behavior under CPU-bound, I/O-bound, and mixed workloads

---

## 🧠 Implemented Scheduling Algorithms

### 1. FCFS — First-Come, First-Served

**Type:** Non-preemptive

FCFS schedules processes according to their arrival order. Once a process starts running, it continues until its CPU burst is completed.

**Characteristics:**

- Simple FIFO-based policy
- Low scheduling complexity
- Easy to understand and implement
- Can suffer from the **convoy effect**
- Long processes can make short processes wait for a significant amount of time

---

### 2. SJF — Shortest Job First

**Type:** Non-preemptive

SJF selects the available process with the shortest CPU burst.

**Characteristics:**

- Favors short CPU-bound jobs
- Can provide low average waiting time when burst lengths are known or estimated
- Long processes may experience starvation when short jobs continually arrive

---

### 3. Priority Scheduling

**Type:** Non-preemptive

Priority Scheduling selects processes according to their assigned priority.

The simulator also supports **aging**, which gradually improves the priority of waiting processes to reduce the possibility of starvation.

**Characteristics:**

- Useful when some processes are more important than others
- Can favor high-priority workloads
- Without aging, low-priority processes may wait indefinitely
- Aging provides a mechanism for improving fairness

---

### 4. Round Robin (RR)

**Type:** Preemptive

Round Robin assigns each runnable process a fixed **time quantum**. When the quantum expires, the scheduler can preempt the current process and give another process an opportunity to run.

**Characteristics:**

- Designed with fairness and responsiveness in mind
- Prevents a single process from continuously occupying the CPU
- Performance is strongly influenced by the selected time quantum
- Particularly useful for interactive or mixed workloads

---

### 5. MLFQ — Multi-Level Feedback Queue

**Type:** Dynamic / Preemptive

Multi-Level Feedback Queue uses multiple priority levels and dynamically changes scheduling decisions according to process behavior.

The simulator includes **priority boosting**, allowing waiting processes to move back toward higher-priority levels and helping prevent starvation.

**Characteristics:**

- Dynamically adapts to process behavior
- Can favor interactive or short-running work
- Uses multiple scheduling queues
- Priority boosting improves long-term fairness
- More complex than the other implemented policies

---

## 🧪 Workload Generation

The simulator can generate different types of workloads so that scheduling algorithms can be evaluated under different operating conditions.

### CPU-Bound Workload

CPU-bound workloads represent processes that spend most of their execution time performing CPU work.

```python
generate_processes(200, 'cpu')
```

### I/O-Bound Workload

I/O-bound workloads represent processes with more frequent interaction between CPU execution and I/O activity.

```python
generate_processes(200, 'io')
```

### Mixed Workload

Mixed workloads combine CPU-bound and I/O-bound behavior.

```python
generate_processes(200, 'mixed')
```

The number of generated processes can also be changed. For example:

```python
generate_processes(200, 'mixed')
```

creates a mixed workload containing 200 processes.

---

## 📈 Performance Metrics

The simulator evaluates scheduler behavior using several metrics.

### Turnaround Time

Measures the total time from a process's arrival until its completion.

**Conceptually:**

```text
Turnaround Time = Completion Time − Arrival Time
```

Lower turnaround time generally indicates that processes complete sooner relative to their arrival.

---

### Waiting Time

Measures the time a process spends waiting to receive CPU service.

For a process, waiting time represents time spent ready but not executing.

Lower waiting time is generally desirable, although minimizing it is not the only scheduling objective.

---

### Response Time

Measures how quickly a process first receives CPU service after arriving.

**Conceptually:**

```text
Response Time = First CPU Start Time − Arrival Time
```

Response time is particularly important for interactive workloads.

---

### CPU Utilization

Measures how effectively the simulated CPU is kept busy.

Higher CPU utilization generally means less simulated CPU idle time, although high utilization by itself does not guarantee good responsiveness or fairness.

---

### Throughput

Measures the amount of completed work over the simulated execution period.

A scheduler with higher throughput can complete more processes in a given amount of simulated time.

---

### Fairness

The simulator also evaluates **fairness**, allowing scheduling policies to be compared not only by speed and throughput but also by how evenly CPU access is distributed among processes.

---

## 🖼️ Execution Traces and Gantt Charts

In addition to numerical metrics, the simulator maintains an **execution trace**.

The trace records scheduling/execution behavior over simulated time and can be used to construct Gantt charts.

A Gantt chart makes it easier to visually inspect:

- Which process was running at a particular time
- When context switches occurred
- How long processes waited
- How preemptive schedulers behaved
- How different algorithms distribute CPU time
- How scheduling decisions change under different workloads

This provides a visual complement to the numerical performance metrics.

---

## 🔄 Project Workflow

The overall simulation workflow can be summarized as:

```text
                 ┌─────────────────────┐
                 │   Generate Workload │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Create Processes  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Run Scheduling      │
                 │ Algorithm           │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Discrete-Event      │
                 │ Simulation          │
                 └──────────┬──────────┘
                            │
                ┌───────────┴───────────┐
                ▼                       ▼
      ┌──────────────────┐    ┌──────────────────┐
      │ Performance      │    │ Execution Trace  │
      │ Metrics          │    │ / Gantt Data     │
      └────────┬─────────┘    └────────┬─────────┘
               │                       │
               └───────────┬───────────┘
                           ▼
                 ┌─────────────────────┐
                 │ Compare Schedulers  │
                 └─────────────────────┘
```

---

## 🚀 How to Run

Run the simulator from the project directory:

```bash
python main.py
```

After execution, the simulator prints the scheduler metrics to the console and stores generated results and execution traces in the project's data directories.

---

## 🛠️ Customizing the Simulation

The workload configuration can be changed in `main.py`.

For example:

```python
generate_processes(200, 'mixed')
```

The supported workload types are:

```text
cpu
io
mixed
```

You can therefore experiment with different workload sizes and workload characteristics and observe how the scheduling algorithms respond.

---

## 📁 Output

The simulator produces two main categories of output.

### Metrics

Scheduler performance results are stored as JSON files in:

```text
data/results/
```

These results can be used to compare the performance of the implemented scheduling policies.

### Execution Traces

Execution traces are stored in:

```text
data/trace/
```

These traces can be used for subsequent visualization, including Gantt-chart analysis.

---

## 🔬 Comparing Scheduling Algorithms

One of the main purposes of the project is to make scheduler trade-offs observable.

A useful experiment is to run the same workload through every scheduling algorithm and compare:

| Metric | What it helps evaluate |
|---|---|
| Turnaround Time | How quickly processes finish after arriving |
| Waiting Time | How long processes remain waiting for CPU time |
| Response Time | How quickly processes begin execution |
| CPU Utilization | How effectively the CPU remains active |
| Throughput | How much work is completed over time |
| Fairness | How evenly CPU access is distributed |

No single scheduling algorithm is optimal for every workload. The most appropriate policy depends on the desired balance between **throughput, latency, responsiveness, fairness, and scheduling behavior**.

---

## ⚡ Why Discrete-Event Simulation?

A discrete-event simulator advances the system through meaningful events rather than treating every point in time as an independent simulation step.

For a CPU scheduler, relevant events can include changes in process state, CPU execution, I/O-related activity, arrivals, completions, and scheduling/preemption decisions.

This approach makes it possible to model scheduling behavior over simulated time while collecting detailed execution information.

---

## 🎯 Use Cases

This simulator is suitable for:

### 📚 Operating Systems Education

- Understanding CPU scheduling concepts
- Studying preemptive vs. non-preemptive scheduling
- Observing starvation and fairness
- Learning the effect of time quantum and priority mechanisms

### 🧪 Algorithm Experiments

- Comparing scheduling policies
- Testing different workload types
- Investigating performance trade-offs
- Studying scheduler behavior using quantitative metrics

### 📊 Visualization

- Generating execution traces
- Building Gantt charts
- Connecting scheduling decisions with measurable performance

### 🔧 Experimental Framework

The common simulation environment makes it possible to evaluate several scheduling strategies under comparable workload conditions.

---

## 📝 Example Experiment

A simple experiment can be performed using a mixed workload:

```python
generate_processes(200, 'mixed')
```

Then run the simulator:

```bash
python main.py
```

The resulting metrics can be compared across:

```text
FCFS
SJF
Priority Scheduling
Round Robin
MLFQ
```

The corresponding execution traces in `data/trace/` can then be examined to understand *why* the algorithms produced different performance results.

---

## 🏁 Conclusion

This project provides a **discrete-event framework for studying CPU scheduling algorithms through simulation, measurement, and visualization**.

By combining:

- Multiple classical scheduling policies
- CPU-bound, I/O-bound, and mixed workloads
- Performance metrics
- Execution traces
- Gantt-chart-oriented data
- Priority aging and MLFQ priority boosting

the simulator goes beyond a basic scheduler implementation and provides an experimental environment for analyzing how scheduling policies behave under different workloads.

It is especially useful for understanding the trade-offs between **waiting time, turnaround time, response time, CPU utilization, throughput, and fairness**—and for connecting operating-system theory with observable scheduling behavior.
