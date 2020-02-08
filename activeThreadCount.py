import threading
import time

def add():
	for i in range(5):
		thread = threading.Thread(target = hold, args=(i,))
		thread.start()
		thread.join()
		time.sleep(1)


def hold(first):
	while True:
		time.sleep(1)
		print('===>>>',threading.activeCount())
		print(first)

	
if __name__ == '__main__':
	thread = threading.Thread(target=add)
	thread.start()

