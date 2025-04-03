def hacer_menu():
    print("\n--- Menú Principal ---")
    print("1. Registrar usuario.")
    print("2. Agregar un atributo al usuario.")
    print("3. Modificar un atributo del usuario.")
    print("4. Eliminar un atributo del usuario.")
    print("5. Mostrar datos del usuario.")
    print("0. Salir del sistema.")
    opcion = int(input("Seleccione una opción: "))
    return opcion

def registrar_usuario():
    print("Registrar un único usuario.")
    nombre_usuario = input("Digite el nombre del usuario: ")
    return {"nombre": nombre_usuario}  # El usuario tendrá un diccionario con sus datos básicos.

def agregar_atributo(usuario):
    atributo = input("\nDigite el nombre del nuevo atributo (por ejemplo, edad, dirección, teléfono): ")
    valor = input(f"Digite el valor de {atributo}: ")
    usuario[atributo] = valor
    print(f"Atributo '{atributo}' agregado con éxito.")

def modificar_atributo(usuario):
    atributo = input("\nDigite el nombre del atributo a modificar: ")
    if atributo in usuario:
        nuevo_valor = input(f"Digite el nuevo valor para {atributo}: ")
        usuario[atributo] = nuevo_valor
        print(f"Atributo '{atributo}' modificado con éxito.")
    else:
        print(f"El atributo '{atributo}' no existe.")

def eliminar_atributo(usuario):
    atributo = input("\nDigite el nombre del atributo a eliminar: ")
    if atributo in usuario:
        del usuario[atributo]
        print(f"Atributo '{atributo}' eliminado con éxito.")
    else:
        print(f"El atributo '{atributo}' no existe.")

def mostrar_usuario(usuario):
    if not usuario:
        print("\nNo hay usuario registrado.")
    else:
        print("\n--- Datos del Usuario ---")
        for clave, valor in usuario.items():
            print(f"{clave.capitalize()}: {valor}")

# **** Zona de Código Principal ****
usuario = {}

while True:
    if not usuario:
        print("\nNo se ha registrado ningún usuario aún.")
    opcion = hacer_menu()
    
    if opcion == 1:
        if not usuario:
            usuario = registrar_usuario()
            print(f"Usuario '{usuario['nombre']}' registrado con éxito.")
        else:
            print("\nEl usuario ya ha sido registrado.")
    
    elif opcion == 2:
        if usuario:
            agregar_atributo(usuario)
        else:
            print("\nNo hay usuario registrado para agregar atributos.")
    
    elif opcion == 3:
        if usuario:
            modificar_atributo(usuario)
        else:
            print("\nNo hay usuario registrado para modificar atributos.")
    
    elif opcion == 4:
        if usuario:
            eliminar_atributo(usuario)
        else:
            print("\nNo hay usuario registrado para eliminar atributos.")
    
    elif opcion == 5:
        mostrar_usuario(usuario)
    
    elif opcion == 0:
        print("Saliendo del sistema...")
        break
    
    else:
        print("Opción inválida, intente nuevamente.")
