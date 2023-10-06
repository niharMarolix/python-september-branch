import datetime

class Employee:
    # def __init__(self, value):
    def punchIn(self):
        time = datetime.datetime.now()
        print(f"punched in at {time}")

    def lunchTime(self):
        time = "12:45pm"
        print(f"time for lunch is {time}")

Ram = Employee()
Ram.punchIn()
Ram.lunchTime()