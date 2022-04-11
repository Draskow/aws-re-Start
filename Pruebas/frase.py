from collections import Counter

phrase = input("Escriba una frase: ")

letter = input("Elija una letra para ver su cantidad en la frase: ")

counter = Counter(phrase)

print("La letra {}, aparece {} veces en la frase {}".format(letter, counter[letter], phrase))