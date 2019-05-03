# abb=('a':100, 'b':200, 'c':30, 'd':4, 'e':1)
# print(min(zip( abb.keys(), abb.values())))

d1 = {'a':21, 'b':54, 'c':4, 'd':15}
print(min(zip(d1.keys(), d1.values())))
print(max(zip(d1.keys(), d1.values())))
print(sorted(zip(d1.values(), d1.keys())))