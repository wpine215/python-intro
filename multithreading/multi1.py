import threading
import time

def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)
		count += 1
		print(threadName, time.ctime(time.time()))

# Create two threads
try:
	t1 = threading.Thread(target = print_time, args = ("Thread-1: ", 2,))
	t2 = threading.Thread(target = print_time, args = ("Thread-2: ", 4,))

	t1.start()
	t2.start()
except:
	print("Unable to start thread!")

# Thread Locking:
# Thread.Lock has two main functions: acquire and release
