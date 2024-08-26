from threading import Thread, Lock, Event
from time import sleep

# Shared variables and Lock
turn = 1
turn_lock = Lock()
stop_event = Event()  # Event to signal threads to stop
process_1 = 1
process_2 = 2
class Process(Thread):
    def __init__(self, id):
        super().__init__()
        self.id = id

    def run(self):
        global turn  # Declare global variable at the beginning of the function
        while not stop_event.is_set():
            # Non-critical section
            print(f"Process {self.id}: In non-critical section")
            sleep(1)

            # Wait for turn
            with turn_lock:  # Acquire lock before checking and waiting
                print(f"Process {self.id}: Waiting for turn {turn}")
                while turn != self.id:
                    turn_lock.release()  # Release lock to allow other threads to run
                    sleep(0.1)
                    turn_lock.acquire()  # Re-acquire lock to check turn again

            # Critical section
            print(f"Process {self.id}: In critical section")
            sleep(1)

            # Change turn
            with turn_lock:  # Acquire lock before changing the turn
                if self.id == 1:
                    turn = 2
                else:
                    turn = 1

# Create processes with numeric IDs
p = Process(process_1)
q = Process(process_2)
z = Process(3)

# Start processes
p.start()
q.start()
z.start()

# Let the processes run for a specific time
sleep(10)  # Run for 10 seconds (adjust as needed)

# Signal the threads to stop
stop_event.set()

# Wait for processes to finish
p.join()
q.join()
z.join()