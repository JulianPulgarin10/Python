# Base de datos de usuarios y notas
usuarios = {}
notas = {}

# Función para calcular el promedio de una lista de notas
def calcular_promedio(notas):
    return round(sum(notas) / len(notas), 2) if notas else 0

# Registro de un nuevo usuario
def registrar_usuario():
    print("\n===== REGISTRO DE USUARIO =====")
    usuario = input("Ingrese un nombre de usuario: ")
    if usuario in usuarios:
        print("El usuario ya existe. Intente con otro nombre.")
        return
    password = input("Ingrese una contraseña: ")
    tipo = seleccionar_tipo_usuario()
    if tipo:
        usuarios[usuario] = {"password": password, "tipo": tipo}
        if tipo == "estudiante":
            notas[usuario] = {}
        print("Usuario registrado con éxito!")
    else:
        print("Registro cancelado.")

# Función para seleccionar el tipo de usuario
def seleccionar_tipo_usuario():
    print("Seleccione el tipo de usuario:")
    print("1. Administrador")
    print("2. Profesor")
    print("3. Estudiante")
    tipo_opcion = input("Ingrese el número de la opción: ")
    tipos = {"1": "admin", "2": "profesor", "3": "estudiante"}
    return tipos.get(tipo_opcion)

# Menú del administrador
def menu_admin():
    while True:
        print("\n===== MENÚ ADMINISTRADOR =====")
        print("1. Ver usuarios registrados")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            print("\nUsuarios registrados:")
            for usuario, data in usuarios.items():
                print(f"Usuario: {usuario}, Tipo: {data['tipo']}")
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Menú del profesor
def menu_profesor():
    while True:
        print("\n===== MENÚ PROFESOR =====")
        print("1. Agregar nota a un estudiante")
        print("2. Ver notas de los estudiantes")
        print("3. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            ver_notas_estudiantes()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Agregar nota a un estudiante
def agregar_nota():
    estudiante = input("Ingrese el nombre del estudiante: ")
    if estudiante not in notas:
        print("El estudiante no está registrado.")
        return
    materia = input("Ingrese la materia: ")
    try:
        nota = float(input("Ingrese la nota: "))
        notas[estudiante].setdefault(materia, []).append(nota)
        print("Nota agregada correctamente.")
    except ValueError:
        print("Nota inválida. Asegúrese de ingresar un número.")

# Ver notas de todos los estudiantes
def ver_notas_estudiantes():
    for estudiante, materias in notas.items():
        print(f"\nNotas de {estudiante}:")
        for materia, calificaciones in materias.items():
            promedio = calcular_promedio(calificaciones)
            print(f"  {materia}: {calificaciones} - Promedio: {promedio}")

# Menú del estudiante
def menu_estudiante(usuario):
    while True:
        print("\n===== MENÚ ESTUDIANTE =====")
        print("1. Ver mis notas")
        print("2. Volver al menú principal")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_mis_notas(usuario)
        elif opcion == "2":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ver notas de un estudiante
def ver_mis_notas(usuario):
    if usuario not in notas or not notas[usuario]:
        print("No tiene notas registradas.")
        return
    while True:
        materias = list(notas[usuario].keys())
        print("\n=== MIS MATERIAS ===")
        for i, materia in enumerate(materias, start=1):
            print(f"{i}. {materia}")
        print(f"{len(materias) + 1}. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion.isdigit() and 1 <= int(opcion) <= len(materias):
            materia = materias[int(opcion) - 1]
            calificaciones = notas[usuario][materia]
            promedio = calcular_promedio(calificaciones)
            print(f"\n{materia}: {calificaciones} - Promedio: {promedio}")
        elif opcion == str(len(materias) + 1):
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Inicio de sesión
def login():
    print("\n===== INICIO DE SESIÓN =====")
    usuario = input("Usuario: ")
    password = input("Contraseña: ")
    if usuario in usuarios and usuarios[usuario]["password"] == password:
        print("Inicio de sesión exitoso!")
        tipo = usuarios[usuario]["tipo"]
        if tipo == "admin":
            menu_admin()
        elif tipo == "profesor":
            menu_profesor()
        elif tipo == "estudiante":
            menu_estudiante(usuario)
    else:
        print("Usuario o contraseña incorrectos.")

# Menú principal
def menu_principal():
    while True:
        print("\n=============================")
        print("  SISTEMA DE GESTIÓN DE NOTAS  ")
        print("=============================")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecución del programa
if __name__ == "__main__":
    menu_principal()
