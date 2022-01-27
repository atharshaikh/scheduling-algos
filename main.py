import sys

import fcfs
import sjf_np
import sjf_p
from genfunc import generate_tasks, get_turnaround_time, get_waiting_time, show_table

if __name__ == "__main__":
    choice = int(
        input("Enter 1 for FCFS implementation, 2 for SJF-NP implementation, and 3 for SJF-P implementation\n"))
    if choice not in [1, 2, 3]:
        print("Invalid choice!!")
        sys.exit(-1)
    tasks = generate_tasks()
    if choice == 1:
        impl = "FCFS"
        fcfs.get_completion_time(tasks)
    elif choice == 2:
        impl = "SJF-NP"
        sjf_np.get_completion_time(tasks)
    elif choice == 3:
        impl = "SJF-P"
        sjf_p.get_completion_time(tasks)
        sjf_p.get_response_time(tasks)

    get_turnaround_time(tasks)
    get_waiting_time(tasks)
    show_table(tasks, impl)
