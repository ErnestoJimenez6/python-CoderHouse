import json
from clase_cliente.cliente import Cliente

class Sistema:
    def __init__(self,archivo_datos="datos.txt"):
        self.usuarios={}
        self.usuario_actual=None
        self.archivo_datos=archivo_datos
        self.cargar_usuarios()

    def guardar_usuarios(self):
        """Guarda los usuarios en el archivo de datos."""
        with open(self.archivo_datos,"w",encoding="utf-8") as f:
            datos={
                u:vars(c) for u,c in self.usuarios.items()
            }
            json.dump(datos,f,ensure_ascii=False,indent=4)

    def cargar_usuarios(self):
        """Carga los usuarios desde el archivo de datos."""
        try:
            with open(self.archivo_datos,"r",encoding="utf-8") as f:
                datos=json.load(f)
                self.usuarios={
                    u:Cliente(
                        c["username"],
                        c["password"],
                        c["nombre"],
                        c["email"]
                    )
                    for u,c in datos.items()
                }
        except (FileNotFoundError,json.JSONDecodeError):
            self.usuarios={}

    def registrar_usuario(self,username,password,nombre,email):
        if username in self.usuarios:
            print("⚠️ El usuario ya existe.\n")
            return
        self.usuarios[username]=Cliente(username,password,nombre,email)
        self.guardar_usuarios()
        print(f"✅ Usuario '{username}' registrado con éxito.\n")

    def mostrar_usuarios(self):
        if not self.usuarios:
            print("📭 No hay usuarios registrados.\n")
            return
        print("👥 Usuarios registrados:")
        for cliente in self.usuarios.values():
            print(f"   • {cliente}")
        print()

    def login(self,username,password):
        if self.usuario_actual:
            print(f"⚠️ Ya hay una sesión iniciada con '{self.usuario_actual.username}'.\n")
            return
        if username not in self.usuarios:
            print("🚫 El usuario no existe.\n")
            return
        cliente=self.usuarios[username]
        if cliente.login(password):
            self.usuario_actual = cliente
            self.guardar_usuarios()
            print(f"🎉 ¡Bienvenido, {username}! Sesión iniciada con éxito.\n")
        else:
            print("❌ Contraseña incorrecta.\n")

    def logout(self):
        if self.usuario_actual:
            print(f"👋 Sesión de '{self.usuario_actual.username}' cerrada.\n")
            self.usuario_actual.logout()
            self.usuario_actual=None
            self.guardar_usuarios()
        else:
            print("⚠️ No hay ninguna sesión activa.\n")