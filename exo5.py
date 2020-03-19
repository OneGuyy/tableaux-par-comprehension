liste = [i**2 + j**2 for i in range(10) for j in range(10)]

for i in range(len(liste)):
	if(i % 10 == 0):
		print()
	print(liste[i], end=" ; ")

print()
