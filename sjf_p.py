from typing import List

from genfunc import show_table, get_waiting_time, get_turnaround_time
from task import Task


def get_completion_time(task_list: List[Task]) -> None:
    current_time = 0
    task_queue = task_list[:]
    remaining_tasks = len(task_queue)
    ready_queue = []
    while remaining_tasks > 0:
        while task_queue and task_queue[0].arrival_time <= current_time:
            ready_queue.append(task_queue.pop(0))
        ready_queue.sort(key=lambda x: (x.time_left, x.arrival_time))
        if len(ready_queue) == 0:
            current_time += 1
            continue
        current_task = ready_queue.pop(0)
        if current_task.time_left == current_task.burst_time:
            current_task.first_cpu_time = current_time
        current_time += 1
        current_task.time_left -= 1
        if current_task.time_left > 0:
            ready_queue.append(current_task)
        elif current_task.time_left == 0:
            current_task.completion_time = current_time
            remaining_tasks -= 1


def get_response_time(task_list: List[Task]) -> None:
    for task in task_list:
        task.response_time = task.first_cpu_time - task.arrival_time


if __name__ == "__main__":
    times = ((0, 5), (1, 3), (2, 4), (4, 1))
    tasks = [Task(arrival_time=i, burst_time=j, time_left=j) for i, j in times]
    tasks.sort(key=lambda x: x.arrival_time)
    get_completion_time(tasks)
    get_turnaround_time(tasks)
    get_waiting_time(tasks)
    get_response_time(tasks)
    show_table(tasks, "SJF-P")
