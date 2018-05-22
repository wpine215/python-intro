import random, time
from threading import BoundedSemaphore, Thread

# Initialize the maximum items/connections for the semaphore
max_items = 5

# Initialize bounded semaphore object to variable 'container'
container = BoundedSemaphore(max_items)

def randsleep():
	time.sleep(random.randrange(2, 5))

def producer(n):
	"""
	A function that 'produces' (releases) connections from the semaphore.
	It increments the semaphore counter.
	If the counter reaches max_items, there are no more connections to free up.
	"""
	for i in range(n):
		randsleep()
		print(time.ctime(), end = ": ")

		try:
			container.release()
			print("Produced an item.")
		except ValueError:
			print("Full; production skipped.")

def consumer(n):
	"""
	A function that 'consumes' (acquires) connections to the semaphore.
	It decrements the semaphore counter. 
	If the counter reaches zero (all connections used up), it prints empty.
	"""
	for i in range(n):
		randsleep()
		print(time.ctime(), end = ": ")

		# Disable default blocking behavior
		if container.acquire(False):
			print("Consumed an item.")
		else:
			print("Empty; consumption skipped.")


# Create a list to hold the threads to be created
threads = []

# Initialize number of iterations the producer/consumer functions should run for
prod_loops = random.randrange(3, 6)
cons_loops = random.randrange(prod_loops, prod_loops + max_items + 2)

# Add producer and consumer threads to list
threads.append(Thread(target = producer, args = (prod_loops,)))
threads.append(Thread(target = consumer, args = (cons_loops,)))

# Start all threads in list
for thread in threads:
	thread.start()

# Wait for all threads to complete
for thread in threads:
	thread.join()

print("Done executing.")