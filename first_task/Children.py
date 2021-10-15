import os
import random
import sys
import time
import os


def child(arg):
    pid = os.getpid()
    print(f"Запущена программа Child в процессе с PID {pid} с аргументом {arg}.")
    time.sleep(arg)
    code = random.randint(0, 1)
    sys.exit(code)


if __name__ == '__main__':
    args = sys.argv
    child(int(args[1]))