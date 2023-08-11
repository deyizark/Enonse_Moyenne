n = input("Konbyen not wap rantre : ")
while (not n.isdigit()):
    n = input("Konbyen not wap rantre : ")
n = int(n)

lis = []

for i in range(n):
    kantite = float(input(f"Rantre { i + 1 }e not la : "))
    lis.append(kantite)
    

moy = sum(lis) / n

if (moy >= 90):
    klas = "A"
elif (moy >=80 and moy < 90):
    klas = "B"
elif (moy >=70 and moy < 80):
    klas = "C"
elif (moy >=60 and moy <70):
    klas = "D"
else:
    klas = "F"

print("Mwayenn not yo se :", moy," \nklasifikasyon : ", klas)