import re

# Base de datos de usuarios y notas
usuarios = {}
notas = {}

# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 2) if notas else 0

# Validación de contraseña segura
def contraseña_segura(contraseña):
    return bool(re.match(r'^(?=.*[A-Za-z])(?=.*\d).{6,}$', contraseña))

# Registro de un nuevo usuario
def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print("❌ El usuario ya existe. Intente con otro nombre.")
        return
    while True:
        password = input("Ingrese una contraseña (mínimo 6 caracteres, debe incluir letras y números): ")
        if not contraseña_segura(password):
            print("⚠️ La contraseña debe contener al menos 6 caracteres e incluir letras y números.")
            continue
        confirmar_contraseña = input("Confirme la contraseña: ")
        if password != confirmar_contraseña:
            print("❌ Las contraseñas no coinciden. Intente de nuevo.")
            continue
        break
    tipo = seleccionar_tipo_usuario()
    if tipo:
        usuarios[usuario] = {"password": password, "tipo": tipo}
        if tipo == "estudiante":
            notas[usuario] = {}
        print("✅ Usuario registrado con éxito!")
    else:
        print("Registro cancelado.")

# Selección del tipo de usuario
def seleccionar_tipo_usuario():
    print("Seleccione el tipo de usuario:")
    print("1. Administrador")
    print("2. Profesor")
    print("3. Estudiante")
    tipos = {"1": "admin", "2": "profesor", "3": "estudiante"}
    return tipos.get(input("Ingrese el número de la opción: "))

# Cambio de contraseña
def cambiar_contraseña():
    print("\n===== CAMBIO DE CONTRASEÑA =====")
    usuario = input("Ingrese su nombre de usuario: ")
    if usuario not in usuarios:
        print("❌ El usuario no existe.")
        return
    if input("Ingrese su contraseña actual: ") != usuarios[usuario]["password"]:
        print("❌ Contraseña incorrecta.")
        return
    while True:
        nueva_contraseña = input("Ingrese la nueva contraseña: ")
        if not contraseña_segura(nueva_contraseña):
            print("⚠️ La contraseña debe contener al menos 6 caracteres e incluir letras y números.")
            continue
        if nueva_contraseña != input("Confirme la nueva contraseña: "):
            print("❌ Las contraseñas no coinciden. Intente de nuevo.")
            continue
        usuarios[usuario]["password"] = nueva_contraseña
        print("✅ Contraseña cambiada con éxito.")
        break

# Inicio de sesión
def login():
    print("\n===== INICIO DE SESIÓN =====")
    usuario = input("Usuario: ")
    if usuario in usuarios and usuarios[usuario]["password"] == input("Contraseña: "):
        print("Inicio de sesión exitoso!")
        {"admin": menu_admin, "profesor": menu_profesor, "estudiante": menu_estudiante}.get(usuarios[usuario]["tipo"], lambda: print("Tipo de usuario inválido."))(usuario)
    else:
        print("Usuario o contraseña incorrectos.")

# Menú principal
def menu_principal():
    while True:
        print("\n=== SISTEMA DE GESTIÓN DE NOTAS ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Cambiar contraseña")
        print("4. Salir")
        {"1": registrar_usuario, "2": login, "3": cambiar_contraseña, "4": exit}.get(input("Seleccione una opción: "), lambda: print("❌ Opción no válida."))()

# Ejecución del programa
if __name__ == "__main__":
    input("Presiona Enter para iniciar...")
    menu_principal()
