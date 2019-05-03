import threading

class Call(threading.Thread):
	def run(self):
		for _ in range(10):
			print(threading.currentThread().getName())
obj= Call(name ='Sending Message')
obj1=Call(name ='rec. msg byeee')
obj.start()
obj1.start()