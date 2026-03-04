# 🧮 Calculadora Sencilla en Python

Una calculadora de consola interactiva con historial de operaciones y salida en color, desarrollada en Python.

---

## 📋 Características

- **4 operaciones básicas**: suma, resta, multiplicación y división
- **Historial de operaciones**: guarda y muestra todas las operaciones realizadas en la sesión
- **Salida en color** gracias a `colorama`:
  - 🟢 Verde → Suma
  - 🔴 Rojo → Resta
  - 🔵 Azul → Multiplicación
  - 🟡 Amarillo → División
- **Validación de división por cero**
- **Interfaz limpia**: limpia la terminal entre operaciones

---

## 🚀 Instalación y uso

### 1. Clona o descarga el proyecto

```bash
git clone https://github.com/tu-usuario/calculadora-sencilla.git
cd calculadora-sencilla
```

### 2. Instala las dependencias

```bash
pip install colorama
```

### 3. Ejecuta la calculadora

```bash
python calculadora.py
```

---

## 🗂️ Menú de opciones

```
Seleccione una funcion:
1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir
6. Historial
```

---

## 🛠️ Requisitos

| Requisito | Versión |
|-----------|---------|
| Python    | 3.x     |
| colorama  | ≥ 0.4.x |

---

## 📁 Estructura del proyecto

```
calculadora-sencilla/
│
└── calculadora.py   # Script principal
```

---

## ⚠️ Notas

- La calculadora opera con **números enteros**. Para decimales, se puede modificar `int(input(...))` por `float(input(...))`.
- El historial de operaciones **se reinicia** al cerrar el programa.
- En Windows, `os.system('clear')` puede requerir cambiarse a `os.system('cls')`.

---

## 📄 Licencia

Este proyecto es de uso libre para fines educativos.