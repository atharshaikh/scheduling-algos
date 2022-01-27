from typing import List

from task import Task


def get_completion_time(task_list: List[Task]):
    current_time = 0
    task_queue = task_list[:]
    remaining_tasks = len(task_queue)
    ready_queue = []
    while remaining_tasks > 0:
        while task_queue and task_queue[0].arrival_time <= current_time:
            ready_queue.append(task_queue.pop(0))
        if not ready_queue:
            current_time += 1
            continue
        ready_queue.sort(key=lambda x: x.burst_time)
        ready_queue[0].completion_time = current_time + ready_queue[0].burst_time
        current_time = ready_queue[0].completion_time
        ready_queue.pop(0)
        remaining_tasks -= 1
