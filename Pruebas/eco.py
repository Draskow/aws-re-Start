exit = "salir"

while exit != True:
    word = input("Escriba lo que usted desee aqui: ")
    if str(word) == exit:
        print("Hasta la próxima")
        
        break
    else:
        print(word)