item=[12,21,36,12]
sqr=[]
for x in item:
	sqr.append(x*2)
print(sqr)
def sqr(x):
	return x*2
new=list(map(sqr, item))
print(new)