import statistics
import DailyRecord

from Student import Student


class LunchLine:
    def __init__(self):
        self.students = []
        self.times = []  # In seconds

    # Creates a new student object and adds it to the students queue.
    def add_student(self):
        student = Student()
        self.students.append(student)

    # Removes the student from the front of the line and adds
    # their time to the times array as a tuple (start_time, time_in_line).
    def remove_student(self):
        if len(self.students) > 0:
            student = self.students.pop(0)
            self.times.insert(0, (student.get_start_time(), student.get_time_in_line()))

    def get_students(self):
        return self.students

    # Takes the average of the 10 most recent times and multiplies it by the num. students in line.
    def get_estimate(self):
        return self.get_avg(5) * len(self.students)

    # Find the average times from [0, amount].
    def get_avg(self, amount):
        recent = self.times[:amount]
        return statistics.mean([x[1] for x in recent])

    # Saves the daily record of times.
    def save_daily_data(self):
        DailyRecord.save_record(self.times)
