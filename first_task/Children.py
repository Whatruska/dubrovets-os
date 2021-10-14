import os
import sys
import time


def child(arg):
    pid = os.getpid()
    print(f"Запущена программа Child в процессе с PID {pid} с аргументом {arg}.")
    time.sleep(arg)


if __name__ == '__main__':
    args = sys.argv
    child(args[1])