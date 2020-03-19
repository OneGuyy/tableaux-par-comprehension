def nb1(x):
	nb = 0
	for i in x:
		if i == '1':
			nb += 1
	return nb

liste = [i for i in range(1, 1000) if i % nb1(bin(i)) == 0]

print(liste)
