__author__ = 'Andreas'
import time
class Task:
    def __init__(self,time,type,customer):
        self.time = time
        self.type = type
        self.customer = customer

    def add_to_queue(self,queue):
        pass

class Queue:
    def __init__(self):
        self.tasks = []
        self.startTime = time.time()

    def add_to_queue(self,task):
        self.tasks.append(task)
