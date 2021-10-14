import sys
import os
import random


def parent(n):
    for i in range(1, int(n)):
        pid = os.fork()
        child_process = pid == 0
        if child_process:
            new_arg = random.randint(5, 10)
            sys.argv = ['Children.py', new_arg]
            exec(open("Children.py").read())
        else:
            info = os.wait()
            print(f"Дочерний процесс с PID {pid} завершился. Статус завершения {info[1]}.")


if __name__ == '__main__':
    args = sys.argv
    parent(args[1])

