__author__ = 'Andreas'
import time
class Task:
    def __init__(self,time_estimate,type,customer):
        self.time_estimate = time_estimate
        self.type = type
        self.customer = customer

    def add_to_queue(self,queue):
        queue.add_to_queue(self)

class Queue:
    def __init__(self):
        self.tasks = []
        self.average_task_time = 0
        self.time_to_estimate = 0
        self.tasks_done = 0
        self.task_start = 0
        self.startTime = time.time()

    def add_to_queue(self,task):
        self.tasks.append(task)

    def estimate_time(self):
        queue_time_estimate = 0
        if self.tasks == []:
            return 0
        else:
            for task in self.tasks:
                queue_time_estimate += task.time_estimate
            return queue_time_estimate

    def list_tasks(self):
        print "Tasks in Queue:"
        for item in self.tasks:
            print "{0} for {1}, estimated time: {2} minutes".format(item.type,item.customer,item.time_estimate)

    def activate_task(self,task):
        self.task_start = time.time()
        self.current_task = self.tasks.pop(self.tasks.index(task))

    def finish_task(self):
        task_time = time.time() - self.task_start
        self.tasks_done += 1
        self.average_task_time = (task_time + self.average_task_time) / self.tasks_done
        task_time_to_estimate = self.current_task.time_estimate - task_time
        self.time_to_estimate = (task_time_to_estimate + self.time_to_estimate) / self.tasks_done
        print "Task completed in {t} seconds - {e} compared to time estimate. Current average task time compared to estimate:{tt}".format(task_time,task_time_to_estimate,self.time_to_estimate)
        self.current_task = None
        self.list_tasks()