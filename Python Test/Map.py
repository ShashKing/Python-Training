item=[12,21,36,12]
sqr=[]
for x in item:
	sqr.append(x*2)
print(sqr)
def sqr(x):
	return x*2
new=list(map(sqr, item))

print(item[0:-1])
print(new)
print(item[::2])
print(item.reverse())