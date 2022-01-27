import sys
from random import randint
from typing import List, Tuple

from rich import box
from rich.console import Console
from rich.table import Table

from task import Task


def generate_tasks() -> List[Task]:
    choice = int(input("Enter 1 to manually enter tasks, or 2 to generate tasks automatically\n"))
    if choice not in [1, 2]:
        print("Invalid option")
        sys.exit(-1)
    if choice == 1:
        task_list = user_tasks()
    else:
        task_list = random_tasks()
    return task_list


def random_tasks() -> List[Task]:
    print("Enter minimum and maximum values for arrival time")
    arrival_low = int(input())
    arrival_high = int(input())
    if arrival_high < arrival_low:
        print("Maximum value < minimum value")
        sys.exit(-1)
    print("Enter minimum and maximum values for burst time")
    burst_low = int(input())
    burst_high = int(input())
    if burst_high < burst_low:
        print("Maximum value < minimum value")
        sys.exit(-1)
    number = int(input("Enter total number of tasks\n"))
    times = [(randint(arrival_low, arrival_high), randint(burst_low, burst_high)) for _ in range(number)]
    return get_tasks_from_times(times)


def totally_random_tasks() -> List[Task]:
    times = [(randint(1, 10), randint(2, 5)) for _ in range(10)]
    return get_tasks_from_times(times)


def user_tasks() -> List[Task]:
    num_of_tasks: int = int(input("Enter the total number of tasks\n"))
    times: List[Tuple[int, int]] = []
    for i in range(num_of_tasks):
        arrival = int(input("Enter the arrival time for this task\n"))
        burst = int(input("Enter the burst time for this task\n"))
        times.append((arrival, burst))
    return get_tasks_from_times(times)


def get_tasks_from_times(times):
    task_list = [Task(arrival_time=i, burst_time=j, time_left=j) for i, j in times]
    task_list.sort(key=lambda x: x.arrival_time)
    return task_list


def get_turnaround_time(task_list: List[Task]):
    for task in task_list:
        task.turn_around_time = task.completion_time - task.arrival_time


def get_waiting_time(task_list: List[Task]):
    for task in task_list:
        task.waiting_time = task.turn_around_time - task.burst_time


def get_average_turnaround_time(task_list: List[Task]):
    avg_tat = sum([i.turn_around_time for i in task_list]) / len(task_list)
    return avg_tat


def get_average_wait_time(task_list: List[Task]):
    avg_wt = sum([i.waiting_time for i in task_list]) / len(task_list)
    return avg_wt


def show_table(task_list: List[Task], algo: str) -> None:
    table = Table(title=f"Implementation of {algo}",
                  box=box.ROUNDED)
    table.add_column("Task Number")
    table.add_column("Arrival Time")
    table.add_column("Burst Time")
    table.add_column("Completion Time")
    table.add_column("Turn Around Time")
    table.add_column("Waiting Time")
    table.add_column("Response Time")

    for num, task in enumerate(task_list):
        table.add_row(
            str(num + 1),
            str(task.arrival_time),
            str(task.burst_time),
            str(task.completion_time),
            str(task.turn_around_time),
            str(task.waiting_time),
            str(task.response_time),
        )

    console = Console()
    console.print(table)
    print(f"Average Turn Around Time: {get_average_turnaround_time(task_list)}")
    print(f"Average Waiting Time: {get_average_wait_time(task_list)}")
