from typing import List

from task import Task


def get_completion_time(task_list: List[Task]):
    total_tasks = len(task_list)
    for cur_task in range(total_tasks):
        start_time = max(task_list[cur_task].arrival_time, task_list[cur_task - 1].completion_time)
        task_list[cur_task].completion_time = start_time + task_list[cur_task].burst_time
