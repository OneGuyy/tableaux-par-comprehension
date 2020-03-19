liste = [str(a) + str(b) + str(c) for a in range(10) for b in range(1, 10) for c in range(10) if (a + c) % b == 0]

print(liste)