from genfunc import show_table
from task import Task

times = ((0, 5), (1, 3), (2, 4), (4, 1))
task_list = [Task(arrival_time=i, burst_time=j, time_left=j) for i, j in times]
task_list.sort(key=lambda x: x.arrival_time)

current_time = 0
task_queue = task_list[:]
remaining_tasks = len(task_queue)
ready_queue = []
while remaining_tasks > 0:
    while task_queue and task_queue[0].arrival_time <= current_time:
        ready_queue.append(task_queue.pop(0))
    ready_queue.sort(key=lambda x: x.time_left)
    if len(ready_queue) == 0:
        current_time += 1
        continue
    current_task = ready_queue.pop(0)
    current_task.time_left -= 1
    if current_task.time_left > 0:
        task_queue.append(current_task)
    elif current_task.time_left == 0:
        current_task.completion_time = current_time
        remaining_tasks -= 1
    current_time += 1

show_table(task_list, "SJF-P")
