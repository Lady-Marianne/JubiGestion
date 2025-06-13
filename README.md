# JubiGestion

**Sistema de gestión de Centros de Jubilados vinculados a PAMI.**  
**Management system for Senior Community Centers affiliated with PAMI.**

---

## 🧩 Descripción

JubiGestion es una aplicación web liviana, diseñada para facilitar la gestión de actividades, socios, profesionales y turnos médicos en centros de jubilados que trabajan en conjunto con PAMI.

Está pensada para funcionar de manera local, sin necesidad de conexión a internet, con una interfaz accesible y amigable para usuarios adultos mayores.

---

## ⚙️ Tecnologías utilizadas

- Python 3.x
- Flask
- HTML + CSS (accesible, sin frameworks pesados)
- SQLite

---

## 🗂️ Estructura del proyecto:

- data: jubigestion_db_esquema.md
- models: member.py, teacher.py
- static: styles.css
- templates: index.html, layout.html
-app.puy
- database_setup.py
- extensions.py
- README.md
- requirements.txt
- run.bat


JubiGestion - Base de datos:

┌────────────────────┐
│     Members        │
└────────────────────┘
dni (PK) (not autoincrement, not null)
full_name
pami_number
birth_date
phone
email
address
status (activo/inactivo)
join_date

┌────────────────────┐
│     Teachers       │
└────────────────────┘
dni (PK) (not autoincrement, not null)
activity_id (FK -> Activities)
full_name
birth_date
phone
email
address
status (activo/inactivo)
join_date

┌────────────────────┐
│      Payments      │
└────────────────────┘
id (PK) (autoincrement, not null)
member_dni (FK → Members) (not null, not autoincrement)
payment_date
amount
month
year

┌────────────────────┐
│     Activities     │
└────────────────────┘
id (PK) (not null, autoincrement)
teacher_id (FK -> Teachers)
name
description
schedule
capacity

┌───────────────────---─┐
│   ActivityEnrollments │
└──────────────────---──┘
id (PK)
member_id (FK → Members)
activity_id (FK → Activities)

┌───────────────────-─┐
│    Professionals    │
└─────────────────-───┘
dni (PK) (not null, not autoincrement)
full_name
license
specialty (clínico, psicólogo, podólogo, enfermero, masajista)
phone
email

┌────────────-────────┐
│      Appointments   │
└────────────-────────┘
id (PK)
member_id (FK → Members)
professional_dni (FK → Professionals)
appointment_date
notes


Pantallas (Vista Web):

- Página de inicio (dashboard)
- Formulario para cargar socios
- Tabla con listado de socios + búsqueda
- Formulario de pago
- Gestión de actividades
- Agendador de turnos

Organización de carpetas sugerida (Estructura básica del proyecto):

JubiGestion/
├── app.py                ← Lógica principal con Flask
├── database.db           ← Base SQLite
├── static/               ← Archivos CSS e imágenes
│   └── styles.css
├── templates/            ← Archivos HTML (uno por pantalla)
│   ├── layout.html       ← Plantilla base
│   ├── index.html        ← Menú principal
│   ├── add_member.html   ← Formulario alta de socios
│   └── ...
└── models.py             ← Definición de tablas (opcional)


🧩 Requisitos clave de la interfaz web (inclusiva + liviana). Recordar que los administrativos
    del Centro de Jubilados son voluntarios jubilados. Al principio, sólo se va a correr localmente:

🟢 Liviana:

HTML puro + CSS simple.
Nada de React, Bootstrap ni frameworks pesados.
Evitamos animaciones o efectos innecesarios.
Cargamos todo localmente (sin conexión).

🟢 Accesible para adultos mayores:

Tamaño de letra grande (mínimo 18px).
Contraste alto: fondo claro + texto oscuro (o viceversa).
Botones grandes y bien espaciados.
Íconos sencillos (si usamos alguno).
Formularios simples (una cosa por vez).
Posibilidad de usar el teclado (tab, enter).

Recordatorio de instalación de Python:

🐍 1. INSTALAR PYTHON EN WINDOWS:

Actualmente, lo más común es instalar Python desde su instalador oficial:

🔹 Paso a paso:
Descargar el instalador desde la web oficial:
👉 https://www.python.org/downloads/

Ejecutar el instalador y marcar la opción ✅ "Add Python to PATH".

Luego elegir "Install Now" (instalación recomendada) o una personalizada.

⚠️ Esa opción del PATH es clave para poder usar python y pip desde la consola sin dolores de cabeza.

🛠️ 2. INSTALAR pip (si por alguna razón no vino incluido)
Desde hace varios años, pip ya viene con Python. Pero si no estuviera, podés instalarlo así:

python -m ensurepip --upgrade

Ver versiones instaladas:

python --version
pip --version

O para chequear con el intérprete de Python activo en la consola:
python -m pip --version

⬆️ 4. ACTUALIZAR PYTHON
Python no se actualiza solo (como pip), tenés que descargar la nueva versión desde la web e instalarla como la primera vez.
Tené cuidado de no desinstalar versiones que puedan estar siendo usadas por proyectos antiguos.

⬆️ 5. ACTUALIZAR pip
Esto sí se hace por consola. Escribí:

🧪 EXTRA: Ver todas las versiones de Python instaladas en el sistema
where python
where pip
Esto te muestra todos los ejecutables python.exe y pip.exe encontrados en el PATH.

python -m pip install --upgrade pip

Pasos para instalar Flask:
1 - Crear entorno virtual:

mkdir JubiGestion
cd JubiGestion
python -m venv jubi_gestion --upgrade-deps

2 - Activar el entorno virtual:
.\jubi_gestion\Scripts\activate

3 - Verificar qué Python se está usando:
python -c "import sys; print(sys.executable)"

4 - Instalar flask:
pip install flask

O mejor:
jubi_gestion\Scripts\python.exe -m pip install flask

Luego abrir la consola de Python:
jubi_gestion\Scripts\python.exe

Y dentro de la consola de Python:
import flask
print(flask.__version__)

O mejor (versión más nueva):
import importlib.metadata
print(importlib.metadata.version("flask"))

📝 Próximo paso: para no olvidarlo.
Te recomiendo guardar este comando para correr siempre tu aplicación desde el entorno correcto:

jubi_gestion\Scripts\python.exe app.py
(Evitando el python global, que te lleva por mal camino.)

🛠 Si querés mejorar el flujo...
Como dijimos antes, podés crear un archivo run.bat dentro de tu carpeta JubiGestion con esto:

@echo off
jubi_gestion\Scripts\python.exe app.py

Así cada vez que querés ejecutar tu app, simplemente hacés doble clic en ese archivo o lo corrés desde consola con:

run.bat