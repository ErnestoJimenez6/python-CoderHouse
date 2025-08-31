def mostrar_menu(sesion_activa):
    print("====== 📋 MENÚ PRINCIPAL ======")
    if sesion_activa:
        print(f"🔐 Sesión iniciada como: {sesion_activa.username}\n")
    else:
        print("🔓 Ningún usuario ha iniciado sesión.\n")

    print("1️⃣ Registrar usuario")
    print("2️⃣ Mostrar usuarios")

    if not sesion_activa:
        print("3️⃣ Iniciar sesión")
    else:
        print("3️⃣ Cerrar sesión")

    print("4️⃣ Salir")