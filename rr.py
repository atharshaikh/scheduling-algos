from typing import List

from task import Task


def get_completion_time(task_list: List[Task], time_quantum: int):
    current_time = 0
    task_queue = task_list[:]
    remaining_tasks = len(task_queue)
    ready_queue = []
    current_task = None
    while remaining_tasks > 0:
        while task_queue and task_queue[0].arrival_time <= current_time:
            ready_queue.append(task_queue.pop(0))
        if current_task and current_task.time_left != 0:
            ready_queue.append(current_task)
        if len(ready_queue) == 0:
            current_time += 1
            continue
        current_task = ready_queue.pop(0)
        if current_task.time_left == current_task.burst_time:
            current_task.first_cpu_time = current_time
        work_time = min(current_task.time_left, time_quantum)
        current_time += work_time
        current_task.time_left -= work_time
        if current_task.time_left == 0:
            current_task.completion_time = current_time
            remaining_tasks -= 1


def get_response_time(task_list: List[Task]) -> None:
    for task in task_list:
        task.response_time = task.first_cpu_time - task.arrival_time
