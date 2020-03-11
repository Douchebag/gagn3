import csv

listi = []

f=open("tmp.txt", "r")

for ord in f.read().split():
	listi.append(ord)

f.close()

print(listi[0])
with open('test.csv','r', encoding="UTF-8") as csvinput:
	with open('output.csv', 'w', encoding="UTF-8") as csvoutput:
		writer = csv.writer(csvoutput, lineterminator='\n')
		reader = csv.reader(csvinput)

		all = []
		row = next(reader)
		teljari = 0
		for x in range(len(listi)):
			print(teljari)
			row.append(listi[teljari])
			all.append(row)
			teljari += 1

		for row in reader:
			row.append(row[0])
			all.append(row)


		writer.writerows(all)
