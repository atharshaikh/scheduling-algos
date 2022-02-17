from dataclasses import dataclass


@dataclass
class Task:
    arrival_time: int
    burst_time: int
    first_cpu_time: int = 0
    time_left: int = 0
    completion_time: int = 0
    turn_around_time: int = 0
    waiting_time: int = 0
    response_time: int = 0
