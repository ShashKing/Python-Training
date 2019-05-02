class Shashank():
	def print(self):
		print("Hello Shashank")
class Neha(Shashank):
	def printa(self):
		print("Hello Neha")
	def print(self):
		print("Hello  I am Neha's Print")

obj= Neha()
obj.printa()
obj.print()
