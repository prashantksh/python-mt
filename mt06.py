# Race condition and thread safety
import unittest
import threading
import time


class Sample:
    def __init__(self):
        self.index = 0

    def increment(self):
        self.index = self.index + 1
        time.sleep(0.01)

    def decrement(self):
        self.index = self.index - 1
        time.sleep(0.01)


class TestSample(unittest.TestCase):

    def test_initially_index_is_zero(self):
        sample = Sample()
        self.assertEqual(sample.index, 0)

    def test_single_threaded_index_is_zero(self):
        sample = Sample()
        for _ in range(100):
            sample.increment()
            sample.decrement()

        self.assertEqual(sample.index, 0)

    def test_multi_threaded_index_is_zero(self):
        sample = Sample()
        n_threads = 4
        for _ in range(n_threads):
            t = threading.Thread(target=self.operate, args=(sample,))
            t.start()

        self.assertEqual(sample.index, 0)

    def operate(self, sample):
        for _ in range(100):
            sample.increment()
            sample.decrement()


if __name__ == '__main__':
    unittest.main()

# to run the tests with verbose messages, use python mt06.py -v
