__author__ = 'Andreas'
import unittest
from Queue_manager import *

class QueueManagerTests(unittest.TestCase):
    def test_create_task(self):
        passport = Task(20,"passport","Bob")
        self.assertTrue(isinstance(passport, Task))
