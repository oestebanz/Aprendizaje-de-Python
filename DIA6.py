print("Clasificador de edad")
edad = int(input("¿Cual es tu edad?"))
if edad <= 12:
    print("Eres un niño o niña 👩")
elif edad <= 17:
    print("Eres un adolescente 👨‍🦱")
elif edad <= 54:
    print("Eres un adulto 👨‍")
else:
    print("Eres un adulto mayor 👨‍🦳")

opcion = ""

while opcion != "3":
    print("\nBienvenido a la mini app")
    print("\nSelecciona una opcion:")
    print("1. Clasificar edad")
    print("2. Calcular edad en meses")
    print("3. Salir")

    opcion = input("Ingresa el numero de la opcion que deseas:")

    if opcion == "1":
        edad = int(input("¿Cual es tu edad?"))

        if edad <= 12:
            print("Eres un niño o niña 👩")
        elif edad <= 17:
            print("Eres un adolescente 👨‍🦱")
        elif edad <= 54:
            print("Eres un adulto 👨‍")
        else:
            print("Eres un adulto mayor 👨‍🦳")

    elif opcion == "2":
        cual = int(input("¿Cuantos años tienes?"))
        resultado = cual * 12
        print(f"Tu edad en meses es: {resultado} meses")

    elif opcion == "3":
        print("Gracias por usar la app. ¡Hasta pronto!")

    else:
        print("Opcion invalida. Debe ser 1, 2 o 3, intenta de nuevo")

