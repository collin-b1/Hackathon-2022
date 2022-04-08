import time


class Student:
    def __init__(self):
        self.start_time = int(time.time())

    # Time started in line
    def get_start_time(self):
        return self.start_time

    # Amount of time spent in line in seconds
    def get_time_in_line(self):
        return int(time.time()) - self.start_time
