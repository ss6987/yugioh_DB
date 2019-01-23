import time

start = time.time()


def setStart():
    global start
    start = time.time()


def sleep2sec():
    sleep_time = 2 - (time.time() - start)
    if sleep_time > 0:
        time.sleep(sleep_time)
