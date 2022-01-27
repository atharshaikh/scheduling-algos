import sys

import fcfs
import sjf_np
from genfunc import generate_tasks, get_turnaround_time, get_waiting_time, show_table

if __name__ == "__main__":
    choice = int(input("Enter 1 for FCFS implementation, and 2 for SJF-NP implementation\n"))
    if choice not in [1, 2]:
        print("Invalid choice!!")
        sys.exit(-1)
    tasks = generate_tasks()
    if choice == 1:
        impl = "FCFS"
        fcfs.get_completion_time(tasks)
    elif choice == 2:
        impl = "SJF-NP"
        sjf_np.get_completion_time(tasks)
    get_turnaround_time(tasks)
    get_waiting_time(tasks)
    show_table(tasks, impl)
