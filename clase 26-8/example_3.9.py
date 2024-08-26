from threading import Thread
from time import sleep

turn = 1

class Process(Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        global turn  # Declare global variable at the beginning of the function
        while True:
            # Non-critical section
            print(f"Process {self.id}: In non-critical section")
            sleep(1)

            # Wait for turn
            print(f"Process {self.id}: Waiting for turn {turn}")
            while turn != self.id:
                sleep(0.1)

            # Critical section
            print(f"Process {self.id}: In critical section")
            sleep(1)

            # Change turn
            if self.id == 1:
                turn = 2
            else:
                turn = 1

# Create processes with numeric IDs
p = Process(1)
q = Process(2)

# Start processes
p.start()
q.start()

# Wait for processes to finish
p.join()
q.join()
