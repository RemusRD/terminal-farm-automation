# 🌾 Terminal Farm Automation

> Aprende Python automatizando una granja virtual en tu terminal

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Issues](https://img.shields.io/badge/Issues-35-orange.svg)
![Dificultad](https://img.shields.io/badge/Dificultad-Principiante-green.svg)

## 📖 Sobre este Proyecto

Este es un proyecto educativo diseñado para aprender Python de manera práctica. Simularás una granja que necesita ser automatizada, resolviendo issues progresivos que te enseñarán desde conceptos básicos hasta avanzados de Python.

## 🎯 Objetivos de Aprendizaje

- **Fundamentos de Python**: Variables, tipos de datos, entrada/salida
- **Control de Flujo**: Condicionales, bucles, funciones
- **Estructuras de Datos**: Listas, diccionarios, conjuntos
- **Programación Orientada a Objetos**: Clases, herencia, métodos
- **Manejo de Archivos**: Leer/escribir archivos, CSV, JSON
- **Testing**: Escribir y ejecutar tests unitarios

## 📊 Tu Progreso

### Niveles de Aprendizaje
- 🟢 **Nivel 1: Básico** (0/8) - Variables, tipos, input/output
- 🟡 **Nivel 2: Control** (0/7) - Condicionales, listas
- 🔵 **Nivel 3: Bucles** (0/7) - While, for, funciones
- 🟣 **Nivel 4: Lógica** (0/8) - Diccionarios, algoritmos
- 🔴 **Nivel 5: Avanzado** (0/5) - Clases, archivos, regex

**Progreso Total: 0/35 issues resueltos**

## 🚀 Cómo Empezar

### 1. Prerrequisitos

- Python 3.8 o superior instalado
- Git para control de versiones
- Un editor de texto (recomendamos VS Code)

### 2. Instalación

```bash
# Clona este repositorio
git clone https://github.com/remusrd/terminal-farm-automation.git
cd terminal-farm-automation

# Instala las dependencias
pip install -r requirements.txt

# Verifica que todo funcione
python main.py
```

### 3. Tu Primera Tarea

1. Ve a la [pestaña Issues](https://github.com/remusrd/terminal-farm-automation/issues)
2. Busca el **Issue #1: Arregla los print** 🟢
3. Lee las instrucciones cuidadosamente
4. Arregla el código en `main.py`
5. Ejecuta los tests: `pytest tests/test_basics.py::test_issue_1`
6. ¡Cuando pasen los tests, habrás completado tu primer issue!

## 🎮 Cómo Jugar

### El Ciclo de Aprendizaje

1. **📋 Lee el Issue**: Cada issue explica qué está roto y qué conceptos aprenderás
2. **💭 Usa los Hints**: Hay 3 niveles de hints si te atascas
3. **🔧 Arregla el Código**: Implementa la solución
4. **🧪 Ejecuta los Tests**: Verifica que tu solución funciona
5. **✅ Cierra el Issue**: Marca como completado y pasa al siguiente

### Sistema de Hints

Cada issue tiene 3 hints progresivos:
- **Hint 1** (0 min): Pregunta guía para orientar tu pensamiento
- **Hint 2** (10 min): Pista más específica sobre el approach
- **Hint 3** (20 min): Estructura del código (sin dar la solución)

### Comandos Útiles

```bash
# Ejecutar el juego
python main.py

# Ejecutar todos los tests
pytest

# Ejecutar tests de un nivel específico
pytest tests/test_basics.py    # Nivel 1
pytest tests/test_control.py   # Nivel 2
pytest tests/test_loops.py     # Nivel 3
pytest tests/test_logic.py     # Nivel 4
pytest tests/test_advanced.py  # Nivel 5

# Ver tu progreso
python check_progress.py

# Obtener un hint
python hints/get_hint.py [numero_issue]
```

## 📚 Estructura del Proyecto

```
terminal-farm-automation/
├── src/                    # Código principal del juego
│   ├── farm.py            # Sistema de granja
│   ├── crops.py           # Definición de cultivos
│   ├── inventory.py       # Sistema de inventario
│   ├── automation.py      # Scripts de automatización
│   └── market.py          # Sistema de comercio
├── data/                   # Archivos de datos
│   ├── crops.json         # Información de cultivos
│   └── prices.csv         # Precios del mercado
├── tests/                  # Tests para cada issue
├── hints/                  # Sistema de hints
└── docs/                   # Documentación adicional
```

## 🎓 Conceptos por Nivel

### 🟢 Nivel 1: Básico
- `print()` - Mostrar información
- Variables y tipos de datos
- `input()` - Recibir datos del usuario
- Conversión de tipos (casting)

### 🟡 Nivel 2: Control de Flujo
- Condicionales (`if`, `elif`, `else`)
- Operadores lógicos (`and`, `or`, `not`)
- Listas y sus métodos
- Operadores de comparación

### 🔵 Nivel 3: Bucles y Funciones
- Bucle `while`
- Bucle `for`
- Definición de funciones
- Parámetros y valores de retorno

### 🟣 Nivel 4: Estructuras de Datos
- Diccionarios
- Algoritmos de búsqueda
- Optimización básica
- Comprensión de listas

### 🔴 Nivel 5: Avanzado
- Clases y objetos
- Manejo de archivos
- Expresiones regulares
- Manejo de excepciones

## 💡 Tips para el Éxito

1. **No tengas miedo de experimentar**: Python es muy indulgente
2. **Lee los mensajes de error**: Son muy informativos
3. **Usa `print()` para debug**: Ver valores intermedios ayuda mucho
4. **Googlea**: Buscar errores es parte del aprendizaje
5. **Tómate tu tiempo**: No hay prisa, el objetivo es aprender

## 🏆 Sistema de Logros

- 🌱 **Primera Semilla**: Completa tu primer issue
- 🌿 **Jardinero Novato**: Completa el Nivel 1
- 🌾 **Agricultor**: Completa el Nivel 2
- 🚜 **Granjero Experto**: Completa el Nivel 3
- 🤖 **Automatizador**: Completa el Nivel 4
- 👨‍🌾 **Maestro Granjero**: Completa todos los issues

## 🤝 Contribuciones

¿Encontraste un bug? ¿Tienes una sugerencia? ¡Abre un issue o pull request!

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 🙏 Agradecimientos

- Inspirado en "The Farmer Was Replaced" y Factorio
- Basado en el [Curso Python de midudev](https://github.com/midudev/curso-python)
- Creado con ❤️ para ayudar a Daniel a aprender Python

---

**¿Listo para empezar?** 👉 [Ve al Issue #1](https://github.com/remusrd/terminal-farm-automation/issues/1)