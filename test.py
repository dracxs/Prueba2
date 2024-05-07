#1)	Escriba un programa que permita almacenar 3 nombres solicitados por pantalla en una lista, luego el sistema deberá mostrar el nombre que tenga mayor cantidad de caracteres en un mensaje de salida por pantalla.
'''
nombres = []
for i in range(3):
    nombres.append(input("Ingrese un nombre: "))
mayor = ""
for nombre in nombres:
    if len(nombre) > len(mayor):
        mayor = nombre
print("El nombre con mayor cantidad de caracteres es:", mayor)
'''
#2)	Cree 2 listas, en las cuales se guardará 3 nombres y 3 apellidos (1 lista para nombres y una 1 lista para apellidos), el sistema deberá mostrar de forma ordenada los nombres y apellidos.
'''
nombres = []
apellidos = []
for i in range(3):
    nombres.append(input("Ingrese un nombre: "))
    apellidos.append(input("Ingrese un apellido: "))
for i in range(3):
    print(nombres[i], apellidos[i])
'''
#3)	Cree una lista y comience a almacenar nombres, cada vez que se agregue un nombre nuevo, el sistema preguntará si desea agregar otro nombre, deberá agregar nombres hasta que la respuesta sea “no”, “No”, “nO” o “NO” (use funciones lower() y upper() ) . Una vez ingresa n nombres, deberán eliminar el nombre con la menor cantidad de caracteres.
'''
nombres = []
while True:
    nombres.append(input("Ingrese un nombre: "))
    if input("Desea agregar otro nombre? (si/no): ").lower() == "no":
        break
menor = nombres[0]
for nombre in nombres:
    if len(nombre) < len(menor):
        menor = nombre
nombres.remove(menor)
print(nombres)
'''
#4)Cree un menú para registrar usuarios e iniciar sesión, también el menú tendrá la opción de eliminar usuarios, para ello, utilice el nombre de usuario, además para confirmar la eliminación, deberán escribir la contraseña correspondiente de cada usuario
'''
usuario = []
contrasena = []

while True:
    print("*" * 20)
    print("1) Registrar usuario")
    print("2) Iniciar sesión")
    print("3) Eliminar usuario")
    print("4) Salir")
    print("*" * 20)
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        usuario.append(input("Ingrese un nombre de usuario: "))
        contrasena.append(input("Ingrese una contraseña: "))
    elif opcion == "2":
        input_usuario = input("Ingrese un nombre de usuario: ")
        input_contrasena = input("Ingrese una contraseña: ")
        if input_usuario in usuario and contrasena[usuario.index(input_usuario)] == input_contrasena:
            print("Inicio de sesión correcto")
        else:
            print("Usuario o contraseña incorrectos")
    elif opcion == "3":
        usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")
    elif opcion == "4":
        break
    else:
        print("Opción incorrecta")
'''
