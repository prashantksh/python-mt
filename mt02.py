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

    for i in range(5):
        t = threading.Thread(target=foo, args=(f'thread {i}',))
        logging.info(f"Invoking thread {i} from main thread")
        t.start()

    logging.info("Exiting the main thread")
