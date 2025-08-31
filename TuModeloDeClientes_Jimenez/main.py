from clase_cliente.sistema import Sistema
from func_aux.auxiliar import mostrar_menu

def main():
    sistema=Sistema()

    while True:
        mostrar_menu(sistema.usuario_actual)
        opcion=input("👉 Selecciona una opción: ").strip()

        if opcion=="1":
            username=input("📝 Usuario: ").strip()
            password=input("🔒 Contraseña: ").strip()
            nombre=input("📛 Nombre: ").strip()
            email=input("📧 Email: ").strip()
            sistema.registrar_usuario(username,password,nombre,email)

        elif opcion=="2":
            sistema.mostrar_usuarios()

        elif opcion=="3":
            if sistema.usuario_actual:
                sistema.logout()
            else:
                username=input("👤 Usuario: ").strip()
                password=input("🔑 Contraseña: ").strip()
                sistema.login(username,password)

        elif opcion=="4":
            print("👋 Programa finalizado. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción inválida. Intenta de nuevo.\n")

if __name__=="__main__":
    main()