"""
example_3.py

Just a short example demonstraing a simple state machine in Python
However, this one has delays that affect it
"""

import time
import queue
from lib.elapsed_time import ET


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        et = ET()
        for x in range(count):
            print(f'Task {name} running')
            time.sleep(1)
            total += 1
            yield
        print(f'Task {name} total: {total}')
        print(f'Task {name} total elapsed time: {et():.1f}')


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)


    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]
    # run the scheduler to run the tasks
    et = ET()
    done = False
    while not done:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
            if len(tasks) == 0:
                done = True

    print()
    print('Total elapsed time: {}'.format(et()))


if __name__ == '__main__':
    main()
