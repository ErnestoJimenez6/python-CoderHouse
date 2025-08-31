class Cliente:
    def __init__(self,username,password,nombre,email):
        self.username=username
        self.password=password
        self.nombre=nombre
        self.email=email
        self.logged_in=False

    def __str__(self):
        return f"👤 Cliente: {self.username} | Nombre: {self.nombre} | Email: {self.email}"

    def mostrar_informacion(self):
        return f"📌 Usuario: {self.username}\nNombre: {self.nombre}\nEmail: {self.email}"

    def login(self,password):
        if self.password==password:
            self.logged_in=True
            return True
        return False

    def logout(self):
        self.logged_in=False