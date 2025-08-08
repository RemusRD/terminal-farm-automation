"""Tests para Issues del Nivel 1: Básico"""

import pytest
import sys
import io
from contextlib import redirect_stdout

# Añadir src al path
sys.path.insert(0, '../')

def test_issue_1_print_statements():
    """Test para Issue #1: Arregla los print"""
    # Este test verifica que los prints estén correctamente formateados
    
    try:
        # Intentar importar main
        import main
        
        # Capturar output
        f = io.StringIO()
        with redirect_stdout(f):
            # Los prints del nivel superior deberían ejecutarse
            pass
            
        output = f.getvalue()
        
        # Verificaciones
        assert "Bienvenido" in output or "Terminal Farm" in output, (
            "❌ Los prints no están funcionando correctamente.\n"
            "   Pista: Asegúrate de usar print() con paréntesis.\n"
            "   Ejemplo: print('Hola mundo')"
        )
        
    except SyntaxError as e:
        pytest.fail(
            f"❌ Hay errores de sintaxis en los print statements.\n"
            f"   Error: {str(e)}\n"
            f"   Pista: Los print necesitan paréntesis: print('texto')\n"
            f"   Revisa todos los print en main.py"
        )

def test_issue_2_variable_types():
    """Test para Issue #2: Tipos de variables correctos"""
    from src.crops import Cultivo
    
    cultivo = Cultivo("tomate")
    
    # Verificar tipos
    assert isinstance(cultivo.tiempo_crecimiento, int), (
        "❌ tiempo_crecimiento debe ser un entero (int), no string.\n"
        "   Pista: Usa 3 en lugar de '3'"
    )
    
    assert isinstance(cultivo.precio, float), (
        "❌ precio debe ser un número decimal (float), no string.\n"
        "   Pista: Usa 15.50 en lugar de '15.50'"
    )
    
    assert isinstance(cultivo.necesita_agua, bool), (
        "❌ necesita_agua debe ser booleano (bool), no string.\n"
        "   Pista: Usa True o False en lugar de 'si' o 'no'"
    )
    
    assert isinstance(cultivo.dias_plantado, int), (
        "❌ dias_plantado debe ser un entero (int), no string.\n"
        "   Pista: Usa 0 en lugar de '0'"
    )

def test_issue_3_type_conversion():
    """Test para Issue #3: Conversión de tipos"""
    import main
    
    # Test de conversión en calcular_ganancia
    resultado = main.calcular_ganancia("10.5", "3")
    
    assert isinstance(resultado, (int, float)), (
        "❌ El resultado debe ser un número, no un string.\n"
        "   Pista: Convierte los strings a números antes de multiplicar.\n"
        "   Usa float(precio_texto) y int(cantidad_texto)"
    )
    
    assert resultado == 31.5, (
        f"❌ El cálculo es incorrecto. Esperado: 31.5, Obtenido: {resultado}\n"
        "   Pista: float('10.5') * int('3') = 31.5"
    )

def test_issue_4_farm_variables():
    """Test para Issue #4: Variables de la granja"""
    from src.farm import Farm
    
    granja = Farm()
    
    # Verificar que existan las variables necesarias
    assert hasattr(granja, 'tamaño'), (
        "❌ Falta la variable 'tamaño' en la clase Farm.\n"
        "   Pista: Añade self.tamaño = 10 en __init__"
    )
    
    assert hasattr(granja, 'nivel_agua'), (
        "❌ Falta la variable 'nivel_agua' en la clase Farm.\n"
        "   Pista: Añade self.nivel_agua = 100 en __init__"
    )
    
    assert hasattr(granja, 'energia'), (
        "❌ Falta la variable 'energia' en la clase Farm.\n"
        "   Pista: Añade self.energia = 100 en __init__"
    )
    
    assert hasattr(granja, 'dia'), (
        "❌ Falta la variable 'dia' en la clase Farm.\n"
        "   Pista: Añade self.dia = 1 en __init__"
    )

def test_issue_5_user_input():
    """Test para Issue #5: Input del usuario"""
    # Este test es más complejo, verificaría que se usa input()
    # Por ahora solo verificamos que la función existe
    import main
    
    # Verificar que main.py use input en algún lugar
    with open('main.py', 'r') as f:
        content = f.read()
        
    assert 'input(' in content, (
        "❌ No se está usando input() para recibir datos del usuario.\n"
        "   Pista: Usa input('Mensaje: ') para pedir datos al usuario.\n"
        "   Ejemplo: farm_name = input('Nombre de tu granja: ')"
    )

# Función helper para mostrar progreso
def mostrar_resultado_test(test_name, passed):
    """Muestra el resultado de un test de forma bonita"""
    if passed:
        print(f"✅ {test_name} - PASADO")
    else:
        print(f"❌ {test_name} - FALLADO")

if __name__ == "__main__":
    # Ejecutar tests individualmente para mejor feedback
    print("\n" + "="*50)
    print("TESTS NIVEL 1: BÁSICO")
    print("="*50 + "\n")
    
    tests = [
        ("Issue #1: Print statements", test_issue_1_print_statements),
        ("Issue #2: Tipos de variables", test_issue_2_variable_types),
        ("Issue #3: Conversión de tipos", test_issue_3_type_conversion),
        ("Issue #4: Variables de granja", test_issue_4_farm_variables),
        ("Issue #5: Input del usuario", test_issue_5_user_input),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
            mostrar_resultado_test(name, True)
        except Exception as e:
            mostrar_resultado_test(name, False)
            print(f"  Razón: {str(e)}\n")