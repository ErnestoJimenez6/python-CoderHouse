# TuModeloDeClientes_Jimenez

Sistema de modelado de clientes para una página de compras, desarrollado en **Python** utilizando Programación Orientada a Objetos (POO).  

Este proyecto fue creado como trabajo práctico para **Coderhouse**.

---

## 🚀 Características

- Registro de usuarios con nombre, email, usuario y contraseña.
- Persistencia de datos en archivo `datos.txt` (JSON).
- Inicio y cierre de sesión.
- Menú interactivo desde consola.
- Implementado como **paquete redistribuible** con `setup.py`.

---

## 📦 Instalación

Cloná el repositorio y movete a la carpeta:

```bash
git clone https://github.com/tuusuario/TuModeloDeClientes_Jimenez.git
cd TuModeloDeClientes_Jimenez
```

Instalá el paquete en tu entorno local:

```bash
python setup.py install
```

o

```bash
pip install .
```

---

## ▶️ Uso

Ejecutá el programa desde la raíz del proyecto:

```bash
python main.py
```

Ejemplo de menú principal:

```bash
====== 📋 MENÚ PRINCIPAL ======
🔓 Ningún usuario ha iniciado sesión.

1️⃣ Registrar usuario
2️⃣ Mostrar usuarios
3️⃣ Iniciar sesión
4️⃣ Salir
```

---

## 🛠️ Estructura del proyecto

```bash
TuModeloDeClientes_Jimenez/
├── clase_cliente/
│   ├── __init__.py
│   ├── cliente.py
│   └── sistema.py
├── func_aux/
│   ├── __init__.py
│   └── auxiliar.py
├── datos.txt
├── main.py
├── setup.py
└── README.md
```

---

## 👨‍💻 Autor

Ernesto Jimenez
