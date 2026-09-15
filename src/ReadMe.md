# 🖥️ CPU Scheduling Simulator

## 📄 Abstract
This project is a **Discrete Event Simulator** for CPU scheduling algorithms. It allows users to simulate and compare multiple scheduling strategies such as **FCFS**, **SJF**, **Priority Scheduling**, **Round Robin (RR)**, and **Multi-Level Feedback Queue (MLFQ)**.  
The simulator generates realistic workloads with CPU-bound, I/O-bound, or mixed processes and provides detailed metrics including **Turnaround Time, Waiting Time, Response Time, CPU Utilization, Throughput, and Fairness**. 📊  

---

## 📝 Introduction
CPU scheduling is a fundamental concept in operating systems, responsible for deciding which process gets access to the CPU at any given time. Efficient scheduling improves system responsiveness and throughput, especially in multi-process environments.  

This simulator implements the following algorithms:  
- **FCFS (First-Come, First-Served)**: Non-preemptive, simple FIFO scheduling. 🕐  
- **SJF (Shortest Job First)**: Non-preemptive, schedules processes with the shortest CPU burst first. ✂️  
- **Priority Scheduling**: Assigns CPU based on process priority; supports aging to prevent starvation. ⭐  
- **Round Robin (RR)**: Preemptive, uses a fixed time quantum for fairness. ⏱️  
- **MLFQ (Multi-Level Feedback Queue)**: Dynamic, multi-level queues with feedback and priority boosting. 🔄  

The simulator also maintains a **trace of execution** for visualization of Gantt charts, helping to understand scheduling behavior. 🖼️

---

## 🚀 How to Run


1**Run the simulation**
```bash
python main.py
```

2**Output**
- Metrics for each scheduler are printed in the console.
- JSON result files are stored in `data/results/`.
- Execution traces for Gantt charts are stored in `data/trace/`.

3**Customization**
You can modify the workload type and number of processes in `main.py`:
```python
generate_processes(200, 'mixed')  # 'cpu', 'io', or 'mixed'
```

---

## 🏁 Conclusion
This project provides a **comprehensive framework for studying and analyzing CPU scheduling algorithms** in a simulated environment.  

It is well-suited for:
- Learning operating system scheduling concepts 📚  
- Comparing scheduler performance under different workloads ⚖️  
- Visualizing execution behavior through traces and metrics 🖌️  

By combining event-driven simulation, multiple scheduling policies, and performance evaluation, this simulator serves as both an educational and experimental platform. 🔧  

---

