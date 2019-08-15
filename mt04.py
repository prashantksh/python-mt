# Daemons

import logging
import threading
import time


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

    threads = []

    for i in range(5):
        t = threading.Thread(target=foo, args=(f'thread {i}',), daemon=True)
        logging.info(
            f"Creating thread {i} from main thread and pushing it to the pool")
        threads.append(t)

    logging.info('Starting all threads from the pool')

    for t in threads:
        t.start()

    # logging.info('Joining all threads to the main')

    # for t in threads:
    #     t.join()

    # Program doesn't wait till all threads are done with. It just comes to an end.
    logging.info("Exiting the main thread")
