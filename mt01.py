import logging
import threading
import time


def foo(thread_name):
    logging.info(f"Run by {thread_name}")

    # Just halt this thread for 2 seconds
    time.sleep(2)
    logging.info(f"{thread_name} ends")


if __name__ == "__main__":
    format = "%(asctime)s >> %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S.%U")

    logging.info("Starting the main thread")

    # trailing comma in args tuple is required if there is only one argument
    t1 = threading.Thread(target=foo, args=('thread 01',))
    logging.info("Invoking thread 01 from main thread")
    t1.start()
    logging.info("After the invocation of thread 01")
    logging.info("Main thread waits for the thread 01 to finish")
    t1.join()
    logging.info("Exiting the main thread")
