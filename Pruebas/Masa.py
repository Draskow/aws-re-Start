altura = input("Introduzca su altura en metros: ")

peso = input("Introduzca su peso en kilogramos: ")

Peso = int(peso)

Altura = float(altura)

Altura = Altura * Altura

imc = Peso / Altura

print("Tu indice de masa corporal es:", round(imc,2))