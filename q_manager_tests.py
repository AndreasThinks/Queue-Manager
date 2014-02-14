__author__ = 'Andreas'
import unittest
import time
from queue_manager import Task, Queue


class QueueManagerTests(unittest.TestCase):
    def test_create_task(self):
        passport = Task(20, "passport", "Bob")
        self.assertTrue(isinstance(passport, Task))  # could this test be more elaborate?
        # TODO -->
        # For example
        # self.assertEquals(passport.time, 20)
        # self.assertEquals(task_type, "passport")

    def test_create_queue(self):
        new_queue = Queue()
        self.assertTrue(isinstance(new_queue.startTime, float))

    def test_add_to_queue(self):
        new_queue = Queue()
        passport = Task(20, "passport", "Bob")
        new_queue.add_to_queue(passport)
        self.assertTrue(passport in new_queue.tasks)

    def test_check_time_pass(self):
        new_queue = Queue()
        time.sleep(0.5)
        self.assertTrue(new_queue.startTime < time.time())

    def test_estimate_queue_time(self):
        new_queue = Queue()
        passport1 = Task(30,"passport","Bob")
        passport2 = Task(20,"passport","Bob")
        passport3 = Task(20,"passport","Bob")
        new_queue.add_to_queue(passport1)
        new_queue.add_to_queue(passport2)
        new_queue.add_to_queue(passport3)
        self.assertEqual(new_queue.estimate_time(), 70)

    def test_list_tasks(self):
        new_queue = Queue()
        passport1 = Task(30,"passport","Bob")
        passport2 = Task(20,"passport","Bob")
        passport3 = Task(20,"passport","Bob")
        new_queue.add_to_queue(passport1)
        new_queue.add_to_queue(passport2)
        new_queue.add_to_queue(passport3)
        new_queue.list_tasks()

    def test_activate_task(self):
        new_queue = Queue()
        passport1 = Task(30,"passport","Bob")
        passport2 = Task(20,"passport","Bob")
        passport3 = Task(20,"passport","Bob")
        new_queue.add_to_queue(passport1)
        new_queue.add_to_queue(passport2)
        new_queue.add_to_queue(passport3)
        new_queue.activate_task(passport1)
        self.assertEqual(new_queue.current_task, passport1)


