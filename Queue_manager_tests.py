__author__ = 'Andreas'
import unittest
from Queue_manager import *

class QueueManagerTests(unittest.TestCase):
    def test_create_task(self):
        passport = Task(20,"passport","Bob")
        self.assertTrue(isinstance(passport, Task))

    def test_create_queue(self):
        new_queue = Queue()
        self.assertTrue(isinstance(new_queue.startTime, float) )

    def test_add_to_queue(self):
        new_queue = Queue()
        passport = Task(20,"passport","Bob")
        new_queue.add_to_queue(passport)
        self.assertTrue(passport in new_queue.tasks)