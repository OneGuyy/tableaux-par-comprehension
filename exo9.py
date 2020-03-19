liste = [((a*100) + (b*10) + a) / ((c*100) + (d*10) + c) for a in range(10) for b in range(10) for c in range(1, 10) for d in range(10) if str((a*100 + b*10 + a) / (c*100 + d*10 + c))[0:4] == "3.14"]

print(liste)