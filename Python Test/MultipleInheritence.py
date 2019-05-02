class Father():
	def print(self):
		print("Hello Child")
class Mother():
	def printa(self):
		print("Hello My child")
class Child(Father, Mother):
	pass

obj = Child()
obj.print()
obj.printa()
