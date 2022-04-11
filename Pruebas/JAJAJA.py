print("Notas de AWS re/Start")
print("Instere las notas en los siguientes puntos:")

no1 = input("Nota 1: ")

no2 = input("Nota 2: ")

no3 = input("Nota 3: ")

no4 = input("Nota 4: ")

no5 = input("Nota 5: ")

no6 = input("Nota 6: ")

no7 = input("Nota 7: ")

no8 = input("Nota 8: ")

no9 = input("Nota 9: ")

no10 = input("Nota 10: ")

n1 = int(no1)

n2 = int(no2)

n3 = int(no3)

n4 = int(no4)

n5 = int(no5)

n6 = int(no6)

n7 = int(no7)

n8 = int(no8)

n9 = int(no9)

n10 = int(no10)

gradeTotal = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10

grade = sum(gradeTotal)/len(gradeTotal)

if (grade < 70):
    print("Tu promedio es: " + grade + "no aprobaste u.u")

else:
    print("Tu promedio es: " + grade + "aprobaste :D")