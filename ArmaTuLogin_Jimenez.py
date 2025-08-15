users={}
current_user=None

def register_user():
    username=input("📝 Ingresa un nombre de usuario: ").strip()
    if username in users:
        print("⚠️ El usuario ya existe. Elige otro.\n")
        return
    
    password=input("🔒 Ingresa una contraseña: ").strip()
    users[username]=password
    print(f"✅ Usuario '{username}' registrado con éxito.\n")


def show_users():
    if not users:
        print("📭 No hay usuarios registrados.\n")
        return
    
    print("👥 Usuarios registrados:")
    for username in users:
        print(f"   • {username}")
    print()


def login():
    global current_user
    if current_user:
        print(f"⚠️ Ya hay una sesión iniciada con '{current_user}'. "
                f"Cierra sesión antes de iniciar con otro.\n")
        return

    username=input("👤 Usuario: ").strip()
    password=input("🔑 Contraseña: ").strip()

    if username in users:
        if users[username]==password:
            current_user=username
            print(f"🎉 ¡Bienvenido, {username}! Sesión iniciada con éxito.\n")
        else:
            print("❌ Contraseña incorrecta.\n")
    else:
        print("🚫 El usuario no existe.\n")


def logout():
    global current_user
    if current_user:
        print(f"👋 Sesión de '{current_user}' cerrada.\n")
        current_user = None
    else:
        print("⚠️ No hay ninguna sesión activa.\n")

def menu():
    while True:
        print("====== 📋 MENÚ PRINCIPAL ======")
        
        if current_user:
            print(f"🔐 Sesión iniciada como: **{current_user}**\n")
        else:
            print("🔓 Ningún usuario ha iniciado sesión.\n")

        print("1️⃣  Registrar usuario")
        print("2️⃣  Mostrar usuarios")

        if not current_user:
            print("3️⃣  Iniciar sesión")
            print("4️⃣  Salir")
        else:
            print("3️⃣  Cerrar sesión")
            print("4️⃣  Salir")

        option=input("👉 Selecciona una opción: ").strip()

        if option=="1":
            register_user()
        elif option=="2":
            show_users()
        elif option=="3":
            if current_user:
                logout()
            else:
                login()
        elif option=="4":
            print("👋 Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.\n")

menu()