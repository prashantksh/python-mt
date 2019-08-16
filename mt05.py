# Executor

import logging
import concurrent.futures
import time
import threading


def foo(thread_name):

    logging.info(f"Run by {thread_name}")

    # Just halt this thread for 2 seconds
    time.sleep(2)
    logging.info(f"Internal identity: {threading.get_ident()}")
    logging.info(f"{thread_name} ends")


if __name__ == "__main__":
    format = "%(asctime)s >> %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S.%U")

    logging.info("Starting the main thread")

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # foo will be called with 0, 1, 2 in this case
        # if we increase the range, the executor takes it by chunks
        # in this case, the executor starts 3 threads at a time, waits till they are finished, and then starts the news chunk
        executor.map(foo, range(10))

        # single invocation
        # task = executor.submit(foo, 'Thread')
        logging.info('after')
