b = 5
for a in range(10) :
	print(a)
	if a is b:
		break

print("Outside Break")
b = 5
for c in range(10) :
	print(c)
	if c is b:
		continue

print("Outside continue")