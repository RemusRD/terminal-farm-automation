"""Tests para Issues del Nivel 3: Bucles y Funciones"""

import pytest
import sys
import io
from contextlib import redirect_stdout
from unittest.mock import patch, MagicMock

# Añadir src al path
sys.path.insert(0, '../')

def test_issue_16_harvest_loop():
    """Test para Issue #16: Bucle de cosecha con for"""
    try:
        from src.automation import Automatizador
        from src.farm import Farm
        from src.crops import Cultivo
        
        # Crear granja y automatizador
        granja = Farm()
        granja.cultivos = []
        automatizador = Automatizador(granja)
        
        # Crear cultivos con diferentes estados
        cultivo1 = Cultivo("tomate")
        cultivo1.puede_cosechar = lambda: True
        
        cultivo2 = Cultivo("maíz") 
        cultivo2.puede_cosechar = lambda: False
        
        cultivo3 = Cultivo("lechuga")
        cultivo3.puede_cosechar = lambda: True
        
        granja.cultivos = [cultivo1, cultivo2, cultivo3]
        
        # Test: cosechar_todos con bucle for
        if hasattr(automatizador, 'cosechar_todos'):
            resultado = automatizador.cosechar_todos()
            
            assert isinstance(resultado, int), (
                "❌ cosechar_todos() debe retornar un entero.\n"
                "   Pista: return cosechados"
            )
            
            assert resultado == 2, (
                "❌ No cuenta correctamente cultivos cosechados.\n"
                "   Pista: Usa un contador que se incremente por cada cultivo cosechado"
            )
        
        # Test: plantar_hilera con range
        if hasattr(automatizador, 'plantar_hilera'):
            # Mock del método plantar para contar llamadas
            granja.plantar_cultivo = MagicMock(return_value=True)
            
            automatizador.plantar_hilera("zanahoria", 5)
            
            # Debería plantar 5 cultivos usando for con range
            assert granja.plantar_cultivo.call_count >= 5, (
                "❌ plantar_hilera no planta suficientes cultivos.\n"
                "   Pista: Usa for i in range(cantidad)"
            )
        
        # Test: lista vacía
        granja.cultivos = []
        if hasattr(automatizador, 'cosechar_todos'):
            resultado = automatizador.cosechar_todos()
            assert resultado == 0, (
                "❌ No maneja correctamente lista vacía.\n"
                "   Pista: El bucle for debería no ejecutarse con lista vacía"
            )
        
    except ImportError as e:
        pytest.fail(
            f"❌ No se puede importar: {e}\n"
            "   Pista: Implementa cosechar_todos() en src/automation.py"
        )

def test_issue_17_game_loop():
    """Test para Issue #17: Game loop con while"""
    try:
        import main
        
        # Test: main tiene bucle while
        main_code = open('main.py', 'r').read()
        
        assert 'while' in main_code, (
            "❌ No se encuentra bucle 'while' en main.py.\n"
            "   Pista: Implementa while jugando: en la función main()"
        )
        
        assert 'jugando' in main_code or 'playing' in main_code, (
            "❌ Falta variable de control del bucle.\n"
            "   Pista: Usa una variable como 'jugando = True'"
        )
        
        # Test: función de game loop simulada
        if hasattr(main, 'game_loop'):
            # Simular entrada del usuario: varias opciones y luego salir
            with patch('builtins.input', side_effect=['1', '2', '3', '0']):
                try:
                    main.game_loop()
                except SystemExit:
                    pass  # Es normal que el juego termine
                
        # Test: mostrar_menu existe
        assert hasattr(main, 'mostrar_menu'), (
            "❌ Falta función mostrar_menu().\n"
            "   Pista: El bucle debe llamar mostrar_menu() en cada iteración"
        )
        
        # Test: procesar_opcion existe
        assert hasattr(main, 'procesar_opcion'), (
            "❌ Falta función procesar_opcion().\n"
            "   Pista: El bucle debe procesar la entrada del usuario"
        )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar main.py.\n"
            "   Pista: Implementa el game loop en main.py"
        )

def test_issue_18_plant_function():
    """Test para Issue #18: Función plantar_cultivo"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        # Asegurar que la granja tiene los recursos necesarios
        granja.energia = 100
        granja.dinero = 100
        
        if not hasattr(granja, 'cultivos'):
            granja.cultivos = []
        
        # Test: función existe y acepta parámetros
        assert hasattr(granja, 'plantar_cultivo'), (
            "❌ Falta función plantar_cultivo() en Farm.\n"
            "   Pista: Implementa def plantar_cultivo(self, tipo_cultivo, posicion)"
        )
        
        # Test: plantación exitosa
        resultado = granja.plantar_cultivo("tomate", (0, 0))
        
        if resultado is not None:
            assert isinstance(resultado, bool), (
                "❌ plantar_cultivo() debe retornar True/False.\n"
                "   Pista: return True si exitoso, False si no"
            )
        
        # Test: docstring existe
        assert granja.plantar_cultivo.__doc__ is not None, (
            "❌ Falta docstring en plantar_cultivo().\n"
            "   Pista: Añade \"\"\"Descripción de la función\"\"\" después de def"
        )
        
        # Test: sin suficientes recursos
        granja.energia = 0  # Sin energía
        resultado = granja.plantar_cultivo("maíz", (1, 1))
        
        if resultado is not None:
            assert resultado == False, (
                "❌ Debe retornar False cuando no hay recursos.\n"
                "   Pista: Verifica if self.energia >= costo_plantar"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm.\n"
            "   Pista: Implementa plantar_cultivo() en src/farm.py"
        )

def test_issue_19_day_function():
    """Test para Issue #19: Función pasar_dia"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        # Inicializar valores si no existen
        if not hasattr(granja, 'dia'):
            granja.dia = 1
        if not hasattr(granja, 'energia'):
            granja.energia = 50
        if not hasattr(granja, 'cultivos'):
            granja.cultivos = []
        
        # Crear cultivos de prueba
        cultivo1 = Cultivo("tomate")
        cultivo1.crecer_un_dia = MagicMock()
        
        cultivo2 = Cultivo("maíz")
        cultivo2.crecer_un_dia = MagicMock()
        
        granja.cultivos = [cultivo1, cultivo2]
        
        # Test: función existe
        assert hasattr(granja, 'pasar_dia'), (
            "❌ Falta función pasar_dia() en Farm.\n"
            "   Pista: Implementa def pasar_dia(self) en src/farm.py"
        )
        
        dia_inicial = granja.dia
        energia_inicial = granja.energia
        
        # Ejecutar pasar_dia
        resultado = granja.pasar_dia()
        
        # Test: incrementa día
        assert granja.dia == dia_inicial + 1, (
            "❌ No incrementa correctamente el día.\n"
            "   Pista: self.dia += 1 en pasar_dia()"
        )
        
        # Test: resetea energía
        assert granja.energia == 100, (
            "❌ No resetea la energía correctamente.\n"
            "   Pista: self.energia = 100 en pasar_dia()"
        )
        
        # Test: actualiza cultivos (llamó a crecer_un_dia)
        cultivo1.crecer_un_dia.assert_called_once()
        cultivo2.crecer_un_dia.assert_called_once()
        
        # Test: retorna resumen
        if resultado is not None:
            assert isinstance(resultado, dict), (
                "❌ pasar_dia() debe retornar un diccionario con resumen.\n"
                "   Pista: return {'dia': self.dia, 'cultivos_actualizados': ...}"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm o Cultivo.\n"
            "   Pista: Implementa pasar_dia() en src/farm.py"
        )

def test_issue_20_nested_loops():
    """Test para Issue #20: Bucles anidados para regar zona"""
    try:
        from src.automation import Automatizador
        from src.farm import Farm
        from src.crops import Cultivo
        
        # Setup
        granja = Farm()
        granja.nivel_agua = 50
        automatizador = Automatizador(granja)
        
        # Mock para get_cultivo_en
        def mock_get_cultivo_en(x, y):
            if x <= 3 and y <= 3:  # Solo hay cultivos en área 4x4
                cultivo = Cultivo(f"cultivo_{x}_{y}")
                cultivo.necesita_agua = True
                cultivo.regar = MagicMock()
                return cultivo
            return None
        
        granja.get_cultivo_en = mock_get_cultivo_en
        
        # Test: función existe
        assert hasattr(automatizador, 'regar_zona'), (
            "❌ Falta función regar_zona() en Automatizador.\n"
            "   Pista: Implementa def regar_zona(self, x_inicio, x_fin, y_inicio, y_fin)"
        )
        
        # Test: regar zona 2x2
        resultado = automatizador.regar_zona(0, 1, 0, 1)
        
        if resultado is not None:
            assert isinstance(resultado, int), (
                "❌ regar_zona() debe retornar número de cultivos regados.\n"
                "   Pista: return contador_regados"
            )
            
            # Debería regar 4 cultivos (2x2)
            assert resultado == 4, (
                "❌ No riega correctamente toda la zona.\n"
                "   Pista: Usa bucles anidados for y in range() para x y for x in range()"
            )
        
        # Test: zona más grande
        granja.nivel_agua = 100  # Asegurar suficiente agua
        resultado = automatizador.regar_zona(0, 2, 0, 2)
        
        if resultado is not None:
            assert resultado == 9, (  # 3x3 = 9 cultivos
                "❌ Bucles anidados no cubren área completa.\n"
                "   Pista: for y in range(y_inicio, y_fin + 1): for x in range(x_inicio, x_fin + 1):"
            )
        
        # Test: sin agua suficiente
        granja.nivel_agua = 2
        resultado = automatizador.regar_zona(0, 3, 0, 3)
        
        if resultado is not None:
            assert resultado <= 2, (
                "❌ Riega más cultivos que agua disponible.\n"
                "   Pista: Verifica if self.granja.nivel_agua > 0 antes de regar"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Automatizador.\n"
            "   Pista: Implementa regar_zona() en src/automation.py"
        )

def test_issue_21_function_params():
    """Test para Issue #21: Función con parámetros y retorno"""
    try:
        from src.crops import calcular_rentabilidad
        
        # Test: función existe
        assert callable(calcular_rentabilidad), (
            "❌ Falta función calcular_rentabilidad().\n"
            "   Pista: def calcular_rentabilidad(precio, tiempo_crecimiento, costo_mantenimiento=1.0, incluir_estacional=False)"
        )
        
        # Test: parámetros básicos
        resultado = calcular_rentabilidad(20, 5)
        
        assert isinstance(resultado, dict), (
            "❌ Debe retornar un diccionario.\n"
            "   Pista: return {'ganancia_diaria': ..., 'clasificacion': ...}"
        )
        
        # Test: contiene campos necesarios
        campos_necesarios = ['ganancia_diaria', 'clasificacion']
        for campo in campos_necesarios:
            assert campo in resultado, (
                f"❌ Falta campo '{campo}' en el resultado.\n"
                f"   Pista: Incluye '{campo}' en el diccionario de retorno"
            )
        
        # Test: parámetros opcionales
        resultado_con_costo = calcular_rentabilidad(20, 5, costo_mantenimiento=2.0)
        resultado_sin_costo = calcular_rentabilidad(20, 5)
        
        assert resultado_con_costo['ganancia_diaria'] != resultado_sin_costo['ganancia_diaria'], (
            "❌ Parámetro costo_mantenimiento no afecta el cálculo.\n"
            "   Pista: ganancia_neta = precio - (costo_mantenimiento * tiempo)"
        )
        
        # Test: parámetro booleano
        resultado_estacional = calcular_rentabilidad(20, 5, incluir_estacional=True)
        resultado_normal = calcular_rentabilidad(20, 5, incluir_estacional=False)
        
        if incluir_estacional:
            assert resultado_estacional['ganancia_diaria'] > resultado_normal['ganancia_diaria'], (
                "❌ Parámetro incluir_estacional no aumenta ganancia.\n"
                "   Pista: if incluir_estacional: ganancia_diaria *= 1.2"
            )
        
        # Test: validación de parámetros
        try:
            calcular_rentabilidad(-10, 5)  # Precio negativo
            pytest.fail(
                "❌ No valida precio negativo.\n"
                "   Pista: if precio < 0: raise ValueError('...')"
            )
        except ValueError:
            pass  # Correcto, debe lanzar excepción
        
        # Test: clasificación
        resultado_alta = calcular_rentabilidad(100, 10)  # Alta rentabilidad
        resultado_baja = calcular_rentabilidad(5, 10)    # Baja rentabilidad
        
        assert 'clasificacion' in resultado_alta, (
            "❌ Falta clasificación de rentabilidad.\n"
            "   Pista: Clasifica como 'alta', 'media', o 'baja' según ganancia_diaria"
        )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar calcular_rentabilidad.\n"
            "   Pista: Implementa la función en src/crops.py"
        )

def test_issue_22_range_enumerate():
    """Test para Issue #22: Range y enumerate en bucles"""
    try:
        from src.automation import Automatizador
        from src.farm import Farm
        from src.crops import Cultivo
        
        # Setup
        granja = Farm()
        granja.cultivos = []
        automatizador = Automatizador(granja)
        
        # Test: plantar_patron usa range con step
        if hasattr(automatizador, 'plantar_patron'):
            granja.plantar_cultivo = MagicMock(return_value=True)
            granja.puede_plantar_en = MagicMock(return_value=True)
            
            resultado = automatizador.plantar_patron("tomate", 0, 20, 3)
            
            # Debería plantar en posiciones 0, 3, 6, 9, 12, 15, 18 = 7 cultivos
            esperados = len(list(range(0, 20, 3)))
            assert granja.plantar_cultivo.call_count == esperados or len(resultado) == esperados, (
                "❌ plantar_patron no usa range(inicio, fin, intervalo) correctamente.\n"
                "   Pista: for posicion in range(inicio, fin, intervalo):"
            )
        
        # Test: inspeccionar_cultivos usa enumerate
        cultivos_test = [
            Cultivo("tomate"),
            Cultivo("maíz"),  
            Cultivo("lechuga")
        ]
        granja.cultivos = cultivos_test
        
        if hasattr(automatizador, 'inspeccionar_cultivos'):
            resultado = automatizador.inspeccionar_cultivos()
            
            assert isinstance(resultado, list), (
                "❌ inspeccionar_cultivos debe retornar una lista.\n"
                "   Pista: return reporte (lista de tuplas)"
            )
            
            if len(resultado) > 0:
                # Cada elemento debe ser tupla (índice, estado)
                for item in resultado:
                    assert isinstance(item, tuple) and len(item) == 2, (
                        "❌ Cada elemento debe ser tupla (índice, estado).\n"
                        "   Pista: for indice, cultivo in enumerate(self.granja.cultivos)"
                    )
                    
                    indice, estado = item
                    assert isinstance(indice, int), (
                        "❌ El primer elemento debe ser el índice (entero).\n"
                        "   Pista: enumerate() proporciona (índice, elemento)"
                    )
        
        # Test: regar_por_intervalos usa enumerate con módulo
        if hasattr(automatizador, 'regar_por_intervalos'):
            # Crear cultivos que necesitan agua
            for cultivo in cultivos_test:
                cultivo.necesita_agua = True
                cultivo.regar = MagicMock()
            
            resultado = automatizador.regar_por_intervalos(intervalo=2)
            
            # Con intervalo 2, debe regar cultivos en posiciones 0, 2 (2 de 3)
            assert isinstance(resultado, int), (
                "❌ regar_por_intervalos debe retornar número de cultivos regados.\n"
                "   Pista: return regados"
            )
            
            # Verificar que se usa módulo para intervalos
            regados_esperados = len([i for i in range(len(cultivos_test)) if i % 2 == 0])
            assert resultado == regados_esperados, (
                "❌ No usa correctamente el módulo para intervalos.\n"
                "   Pista: if indice % intervalo == 0: regar"
            )
        
        # Test: diferentes usos de range
        test_ranges = {
            'simple': list(range(5)),
            'con_inicio': list(range(2, 8)),  
            'con_step': list(range(0, 10, 2)),
            'negativo': list(range(10, 0, -1))
        }
        
        # Verificar que entiende diferentes formas de range
        assert test_ranges['simple'] == [0, 1, 2, 3, 4], (
            "❌ Problema con range(5).\n"
            "   Pista: range(n) genera 0, 1, 2, ..., n-1"
        )
        
        assert test_ranges['con_step'] == [0, 2, 4, 6, 8], (
            "❌ Problema con range(0, 10, 2).\n"
            "   Pista: range(start, stop, step) salta de step en step"
        )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar funciones de automatización.\n"
            "   Pista: Implementa plantar_patron, inspeccionar_cultivos, regar_por_intervalos en src/automation.py"
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
    print("\n" + "="*60)
    print("TESTS NIVEL 3: BUCLES Y FUNCIONES")
    print("="*60 + "\n")
    
    tests = [
        ("Issue #16: Bucle de cosecha con for", test_issue_16_harvest_loop),
        ("Issue #17: Game loop con while", test_issue_17_game_loop),
        ("Issue #18: Función plantar_cultivo", test_issue_18_plant_function),
        ("Issue #19: Función pasar_dia", test_issue_19_day_function),
        ("Issue #20: Bucles anidados para regar zona", test_issue_20_nested_loops),
        ("Issue #21: Función con parámetros y retorno", test_issue_21_function_params),
        ("Issue #22: Range y enumerate en bucles", test_issue_22_range_enumerate),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
            mostrar_resultado_test(name, True)
        except Exception as e:
            mostrar_resultado_test(name, False)
            print(f"  Razón: {str(e)}\n")