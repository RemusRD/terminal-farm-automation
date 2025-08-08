"""
Terminal Farm Automation - Juego Principal
==========================================
Este archivo contiene errores intencionales que deberás arreglar
siguiendo los issues en GitHub.
"""

# Issue #1: Los print están mal escritos
print Bienvenido a Terminal Farm Automation!
print Tu granja tiene, cultivos, "cultivos"

# Issue #5: Falta input para el nombre de la granja
farm_name = "Granja Sin Nombre"
print("Nombre de tu granja:", farm_name)

# Issue #17: Falta el game loop principal
# TODO: Aquí debería haber un bucle while para el juego

def main():
    """Función principal del juego"""
    
    # Issue #1: Más prints rotos
    print === TERMINAL FARM AUTOMATION ===
    
    # Variables del juego (algunas tienen errores de tipo)
    # Issue #2: Tipos de datos incorrectos
    nivel_agua = "10"  # Debería ser int
    energia = 100.0    # Correcto
    dia = "1"          # Debería ser int
    jugando = "si"     # Debería ser bool
    
    # Issue #4: Faltan variables de la granja
    # TODO: Añadir variables para tamaño_granja, cultivos_plantados, dinero
    
    # Mostrar estado inicial
    print(f"Día: {dia}")
    print(f"Agua: {nivel_agua}")
    print(f"Energía: {energia}")
    
    # Issue #17: Aquí debería estar el bucle principal del juego
    # while jugando:
    #     mostrar_menu()
    #     procesar_opcion()
    
    print("Gracias por jugar!")

def mostrar_menu():
    """Muestra el menú principal"""
    # Issue #1: Print sin paréntesis
    print "=== MENÚ PRINCIPAL ==="
    print("1. Plantar cultivo")
    print("2. Regar cultivos")
    print("3. Cosechar")
    print("4. Ver inventario")
    print("5. Ir al mercado")
    print("0. Salir")

def procesar_opcion():
    """Procesa la opción del usuario"""
    # Issue #5: Falta input del usuario
    opcion = "1"  # Hardcodeado, debería usar input()
    
    # Issue #9: Falta lógica de condicionales
    # TODO: Implementar if/elif/else para procesar opciones
    
    print(f"Opción seleccionada: {opcion}")

# Issue #3: Conversión de tipos
def calcular_ganancia(precio_texto, cantidad_texto):
    """Calcula la ganancia total"""
    # TODO: Convertir strings a números antes de multiplicar
    total = precio_texto * cantidad_texto  # Esto dará error
    return total

# Código que se ejecuta al iniciar
if __name__ == "__main__":
    # Issue #1: Print mal formateado
    print("Iniciando juego...")
    main()