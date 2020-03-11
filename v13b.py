jakvaett = []
neikvaett = []
jTal = 0
nTal = 0

jf = open("jakvaed.txt", "r")
for ord in jf.read().split():
	jakvaett.append(ord)
jf.close()

nf = open("neikvaett.txt", "r")
for ord in nf.read().split():
	neikvaett.append(ord)
nf.close()

f=open("frett1.txt", "r", encoding="UTF-8")

for ord in f.read().split():
	if ord in jakvaett:
		#print("Jakvaett:", ord)
		jTal += 1
	elif ord in neikvaett:
		#print("Neikvaett:", ord)
		nTal += 1
	#print(ord)

f.close()

print("Jakvaed:", jTal)
print("Neikvaed:", nTal)

if jTal > nTal:
	print("Jakvaed grein")
elif jTal < nTal:
	print("Neikvaed grein")
else:
	print("jafnt")
