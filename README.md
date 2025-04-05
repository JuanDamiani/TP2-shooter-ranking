# TP2 - Simulación de partidas y ranking en shooter online  -------------------- JUAN DE LA CRUZ DAMIANI 

Este proyecto simula partidas de un juego de disparos tipo shooter, calcula puntajes por jugador según sus kills, asistencias y muertes, y genera un ranking actualizado ronda por ronda.

El trabajo corresponde al **Ejercicio 10** del TP2 de Seminario de Lenguajes - Python (2025), y está estructurado como un proyecto Python real, con código modular, notebook de análisis y entorno virtual.

## Estructura del proyecto

TP2/
│
├── notebooks/              # Notebooks con el análisis
│   └── Ej10.ipynb          # Simulación y ranking ronda por ronda
│
├── src/                    # Código fuente
│   ├── __init__.py         # Hace que src sea un paquete
│   └── funciones.py        # Funciones para simular rondas y rankings
│
├── requirements.txt        # Dependencias del entorno virtual
├── README.md               # Este archivo :)
└── .gitignore              # Archivos que no se suben al repo

## Cómo correr el proyecto

1. Clonar el repositorio (si está en GitHub):
   git clone https://github.com/tu-usuario/TP2-shooter-ranking.git
   cd TP2-shooter-ranking

2. Crear entorno virtual (si no lo hiciste ya):
   python -m venv venv

3. Activar entorno virtual:

   - En Git Bash:
     source venv/Scripts/activate

   - En CMD:
     venv\Scripts\activate.bat

4. Instalar dependencias:
   pip install -r requirements.txt

5. Correr el notebook:
   jupyter notebook

   Luego abrí el archivo Ej10.ipynb desde el navegador y ejecutá las celdas.

## Qué hace el proyecto

- Simula una serie de rondas con jugadores y sus estadísticas (kills, assists, deaths).
- Calcula los puntajes según las reglas:
  - Kill: +3 pts
  - Asistencia: +1 pt
  - Muerte: -1 pt
- Muestra un ranking
