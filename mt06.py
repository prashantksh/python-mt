# Race condition and thread safety
import unittest
import threading
import time


class Sample:
    def __init__(self):
        self.index = 0
        # self._mutex_lock = threading.Lock()

    def increment_mt(self):
        self.index = self.index + 1

    def decrement_mt(self):
        self.index = self.index - 1

    def increment_st(self):
        self.index = self.index + 1

    def decrement_st(self):
        self.index = self.index - 1


class TestSample(unittest.TestCase):

    def test_initially_index_is_zero(self):
        sample = Sample()
        self.assertEqual(sample.index, 0)

    def test_single_threaded_index_is_zero(self):
        sample = Sample()
        for _ in range(100):
            sample.increment_st()
            sample.decrement_st()

        self.assertEqual(sample.index, 0)

    def test_multi_threaded_index_is_zero(self):
        sample = Sample()
        n_threads = 5
        lock = threading.Lock()
        threads = []

        for _ in range(n_threads):
            t = threading.Thread(target=self.operate, args=(sample, lock))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        self.assertEqual(sample.index, 0)

    def operate(self, sample, lock):
        rl = threading.RLock()
        for _ in range(100000):
            with lock:
                sample.increment_mt()
                sample.decrement_mt()
            # lock.release()


if __name__ == '__main__':
    unittest.main()

# to run the tests with verbose messages, use python mt06.py -v
