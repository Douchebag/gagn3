listi1 = {}

f=open("skra.txt", "r")

for ord in f.read().split():
	if ord not in listi1:
		listi1[ord] = 1
	else:
		listi1[ord] += 1

for x, y in listi1.items():
	print(x + ":", y)
f.close()
