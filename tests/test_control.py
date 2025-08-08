"""Tests para Issues del Nivel 2: Control de Flujo"""

import pytest
import sys
import io
from contextlib import redirect_stdout
from unittest.mock import patch, MagicMock

# Añadir src al path
sys.path.insert(0, '../')

def test_issue_9_irrigation_system():
    """Test para Issue #9: Sistema de riego con condicionales"""
    try:
        from src.automation import regar_cultivos
        from src.farm import Farm
        from src.crops import Cultivo
        
        # Crear granja con agua
        granja = Farm()
        granja.nivel_agua = 50
        granja.cultivos = []
        
        # Crear cultivos con diferentes necesidades de agua
        cultivo_necesita_agua = Cultivo("tomate")
        cultivo_necesita_agua.necesita_agua = True
        
        cultivo_no_necesita_agua = Cultivo("cactus") 
        cultivo_no_necesita_agua.necesita_agua = False
        
        granja.cultivos = [cultivo_necesita_agua, cultivo_no_necesita_agua]
        
        # Test: Regar con agua disponible
        resultado = regar_cultivos(granja)
        
        assert granja.nivel_agua < 50, (
            "❌ El nivel de agua no se redujo después del riego.\n"
            "   Pista: Reduce self.nivel_agua -= 1 por cada cultivo regado."
        )
        
        # Test: Sin agua
        granja.nivel_agua = 0
        agua_inicial = granja.nivel_agua
        regar_cultivos(granja)
        
        assert granja.nivel_agua == agua_inicial, (
            "❌ Se intentó regar sin agua disponible.\n"
            "   Pista: Verifica if self.nivel_agua > 0 antes de regar."
        )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar la función regar_cultivos.\n"
            "   Pista: Asegúrate de que existe en src/automation.py"
        )

def test_issue_10_crop_list():
    """Test para Issue #10: Lista de cultivos"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        
        # Test: Inicialización como lista
        assert isinstance(granja.cultivos, list), (
            "❌ self.cultivos debe ser una lista, no None u otro tipo.\n"
            "   Pista: Cambia self.cultivos = None por self.cultivos = []"
        )
        
        assert granja.cultivos == [], (
            "❌ La lista de cultivos debe inicializarse vacía.\n"
            "   Pista: self.cultivos = [] en __init__"
        )
        
        # Test: Añadir cultivos
        cultivo1 = Cultivo("tomate")
        cultivo2 = Cultivo("maíz")
        
        granja.cultivos.append(cultivo1)
        granja.cultivos.append(cultivo2)
        
        assert len(granja.cultivos) == 2, (
            "❌ No se pueden añadir cultivos a la lista.\n"
            "   Pista: Usa self.cultivos.append(cultivo)"
        )
        
        assert cultivo1 in granja.cultivos, (
            "❌ El cultivo añadido no está en la lista.\n"
            "   Pista: Verifica que append() funcione correctamente"
        )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm o Cultivo.\n"
            "   Pista: Verifica que existan en src/farm.py y src/crops.py"
        )

def test_issue_11_list_methods():
    """Test para Issue #11: Métodos de lista"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        
        # Crear cultivos con diferentes precios
        tomate = Cultivo("tomate")
        tomate.precio = 15.0
        
        maiz = Cultivo("maíz")
        maiz.precio = 10.0
        
        lechuga = Cultivo("lechuga")
        lechuga.precio = 20.0
        
        # Test: plantar_cultivo usando append
        if hasattr(granja, 'plantar_cultivo'):
            granja.plantar_cultivo(tomate)
            granja.plantar_cultivo(maiz)
            granja.plantar_cultivo(lechuga)
        else:
            granja.cultivos = [tomate, maiz, lechuga]
        
        assert len(granja.cultivos) == 3, (
            "❌ No se plantaron todos los cultivos.\n"
            "   Pista: Usa self.cultivos.append(cultivo) en plantar_cultivo()"
        )
        
        # Test: quitar_cultivo usando remove
        if hasattr(granja, 'quitar_cultivo'):
            granja.quitar_cultivo(maiz)
            assert len(granja.cultivos) == 2, (
                "❌ No se removió el cultivo correctamente.\n"
                "   Pista: Usa self.cultivos.remove(cultivo) en quitar_cultivo()"
            )
            assert maiz not in granja.cultivos, (
                "❌ El cultivo removido sigue en la lista.\n"
                "   Pista: Verifica que remove() funcione"
            )
        
        # Test: ordenar_cultivos_por_precio
        if hasattr(granja, 'ordenar_cultivos_por_precio'):
            granja.ordenar_cultivos_por_precio()
            precios = [c.precio for c in granja.cultivos]
            assert precios == sorted(precios), (
                "❌ Los cultivos no están ordenados por precio.\n"
                "   Pista: Usa self.cultivos.sort(key=lambda x: x.precio)"
            )
        
        # Test: contar_cultivos usando len
        if hasattr(granja, 'contar_cultivos'):
            assert granja.contar_cultivos() == len(granja.cultivos), (
                "❌ contar_cultivos() no devuelve el número correcto.\n"
                "   Pista: return len(self.cultivos)"
            )
        
        # Test: tiene_cultivo usando operador in
        if hasattr(granja, 'tiene_cultivo'):
            assert granja.tiene_cultivo(tomate) == True, (
                "❌ tiene_cultivo() no funciona correctamente.\n"
                "   Pista: return cultivo in self.cultivos"
            )
            
            cultivo_inexistente = Cultivo("pepino")
            assert granja.tiene_cultivo(cultivo_inexistente) == False, (
                "❌ tiene_cultivo() devuelve True para cultivo inexistente.\n"
                "   Pista: Verifica la lógica del operador 'in'"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm o Cultivo.\n"
            "   Pista: Verifica que existan en src/farm.py y src/crops.py"
        )

def test_issue_12_input_validation():
    """Test para Issue #12: Validación de entrada con if/else"""
    try:
        import main
        
        # Test: validar_cantidad
        if hasattr(main, 'validar_cantidad'):
            # Cantidad válida
            with patch('builtins.input', return_value='5'):
                resultado = main.validar_cantidad()
                assert isinstance(resultado, int) and resultado > 0, (
                    "❌ validar_cantidad() no devuelve entero positivo válido.\n"
                    "   Pista: Convierte a int() y verifica que sea > 0"
                )
            
            # Cantidad negativa - debería pedir nueva entrada
            with patch('builtins.input', side_effect=['-5', '3']):
                resultado = main.validar_cantidad()
                assert resultado == 3, (
                    "❌ No se maneja correctamente cantidad negativa.\n"
                    "   Pista: if cantidad <= 0: pedir nueva entrada"
                )
        
        # Test: validar_opcion_menu
        if hasattr(main, 'validar_opcion_menu'):
            opciones_validas = [1, 2, 3, 4, 0]
            
            # Opción válida
            with patch('builtins.input', return_value='2'):
                resultado = main.validar_opcion_menu(opciones_validas)
                assert resultado in opciones_validas, (
                    "❌ No acepta opción válida correctamente.\n"
                    "   Pista: if opcion in opciones_validas:"
                )
            
            # Opción inválida - debería pedir nueva entrada
            with patch('builtins.input', side_effect=['99', '1']):
                resultado = main.validar_opcion_menu(opciones_validas)
                assert resultado == 1, (
                    "❌ No maneja opción inválida correctamente.\n"
                    "   Pista: Mostrar error y pedir nueva entrada"
                )
        
        # Test: manejo de entrada no numérica
        if hasattr(main, 'validar_numero'):
            with patch('builtins.input', side_effect=['abc', '42']):
                resultado = main.validar_numero()
                assert resultado == 42, (
                    "❌ No maneja entrada no numérica correctamente.\n"
                    "   Pista: Usa try/except ValueError"
                )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar main.py.\n"
            "   Pista: Asegúrate de que las funciones de validación existan"
        )

def test_issue_13_seasons_system():
    """Test para Issue #13: Sistema de temporadas"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        
        # Test: Inicialización con temporada
        assert hasattr(granja, 'temporada'), (
            "❌ Falta la variable self.temporada en Farm.\n"
            "   Pista: Añade self.temporada = 'primavera' en __init__"
        )
        
        # Test: cambiar_temporada
        if hasattr(granja, 'cambiar_temporada'):
            granja.cambiar_temporada('verano')
            assert granja.temporada == 'verano', (
                "❌ cambiar_temporada() no actualiza la temporada.\n"
                "   Pista: self.temporada = nueva_temporada"
            )
            
            # Temporada inválida
            resultado = granja.cambiar_temporada('temporada_inexistente')
            if resultado is False:
                assert granja.temporada == 'verano', (
                    "❌ Se cambió a temporada inválida.\n"
                    "   Pista: Valida temporadas permitidas"
                )
        
        # Crear cultivos con temporadas específicas
        tomate = Cultivo("tomate")
        if hasattr(tomate, 'temporadas'):
            tomate.temporadas = ['primavera', 'verano']
        
        calabaza = Cultivo("calabaza")  
        if hasattr(calabaza, 'temporadas'):
            calabaza.temporadas = ['otoño']
            
        apio = Cultivo("apio")
        if hasattr(apio, 'temporadas'):
            apio.temporadas = 'todo-temporada'
        
        # Test: puede_plantar_cultivo con verificación de temporada
        if hasattr(granja, 'puede_plantar_cultivo'):
            granja.temporada = 'verano'
            
            # Cultivo de verano - debería permitirse
            puede_plantar_tomate = granja.puede_plantar_cultivo(tomate)
            assert puede_plantar_tomate == True, (
                "❌ No permite plantar cultivo de temporada correcta.\n"
                "   Pista: if self.temporada in cultivo.temporadas:"
            )
            
            # Cultivo de otoño en verano - no debería permitirse
            puede_plantar_calabaza = granja.puede_plantar_cultivo(calabaza)
            assert puede_plantar_calabaza == False, (
                "❌ Permite plantar cultivo fuera de temporada.\n"
                "   Pista: Verifica que la temporada actual esté en cultivo.temporadas"
            )
            
            # Cultivo todo-temporada - siempre debería permitirse
            puede_plantar_apio = granja.puede_plantar_cultivo(apio)
            assert puede_plantar_apio == True, (
                "❌ No permite cultivo todo-temporada.\n"
                "   Pista: if cultivo.temporadas == 'todo-temporada': return True"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm o Cultivo.\n"
            "   Pista: Asegúrate de implementar el sistema de temporadas"
        )

def test_issue_14_crop_comparison():
    """Test para Issue #14: Comparación de cultivos"""
    try:
        from src.crops import Cultivo
        
        # Crear cultivos con diferentes características
        tomate = Cultivo("tomate")
        tomate.precio = 15.0
        tomate.tiempo_crecimiento = 5
        
        maiz = Cultivo("maíz")
        maiz.precio = 10.0
        maiz.tiempo_crecimiento = 3
        
        lechuga = Cultivo("lechuga")
        lechuga.precio = 8.0
        lechuga.tiempo_crecimiento = 2
        
        # Test: comparar_por_precio
        if hasattr(Cultivo, 'comparar_por_precio') or 'comparar_por_precio' in globals():
            try:
                from src.crops import comparar_por_precio
                resultado = comparar_por_precio(tomate, maiz)
                assert resultado == tomate, (
                    "❌ No identifica correctamente el cultivo más caro.\n"
                    "   Pista: return cultivo1 if cultivo1.precio > cultivo2.precio else cultivo2"
                )
            except ImportError:
                pass
        
        # Test: comparar_por_tiempo
        if 'comparar_por_tiempo' in dir():
            resultado = comparar_por_tiempo(lechuga, tomate)
            assert resultado == lechuga, (
                "❌ No identifica el cultivo que crece más rápido.\n"
                "   Pista: Menor tiempo_crecimiento = más rápido"
            )
        
        # Test: es_mas_rentable (precio/tiempo)
        if 'es_mas_rentable' in dir():
            # Rentabilidad tomate: 15/5 = 3.0
            # Rentabilidad maíz: 10/3 = 3.33
            resultado = es_mas_rentable(maiz, tomate)
            assert resultado == True, (
                "❌ Cálculo de rentabilidad incorrecto.\n"
                "   Pista: rentabilidad = precio / tiempo_crecimiento"
            )
        
        # Test: recomendar_mejor_cultivo
        cultivos = [tomate, maiz, lechuga]
        
        if 'recomendar_mejor_cultivo' in dir():
            mejor_precio = recomendar_mejor_cultivo(cultivos, 'precio')
            assert mejor_precio == tomate, (
                "❌ No recomienda correctamente por precio.\n"
                "   Pista: Encuentra max por criterio dado"
            )
            
            mejor_velocidad = recomendar_mejor_cultivo(cultivos, 'velocidad')
            assert mejor_velocidad == lechuga, (
                "❌ No recomienda correctamente por velocidad.\n"
                "   Pista: Menor tiempo = más rápido"
            )
            
            mejor_rentabilidad = recomendar_mejor_cultivo(cultivos, 'rentabilidad')
            # Rentabilidades: tomate=3.0, maíz=3.33, lechuga=4.0
            assert mejor_rentabilidad == lechuga, (
                "❌ No recomienda correctamente por rentabilidad.\n"
                "   Pista: Mayor precio/tiempo = más rentable"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar las funciones de comparación.\n"
            "   Pista: Implementa las funciones en src/crops.py"
        )

def test_issue_15_game_state_booleans():
    """Test para Issue #15: Estado del juego con booleanos"""
    try:
        from src.farm import Farm
        from src.crops import Cultivo
        
        granja = Farm()
        
        # Test: Variables de estado iniciales
        required_states = ['es_dia', 'hay_tormenta', 'granja_operativa']
        for state in required_states:
            assert hasattr(granja, state), (
                f"❌ Falta la variable de estado '{state}' en Farm.\n"
                f"   Pista: Añade self.{state} = True/False en __init__"
            )
        
        # Verificar valores iniciales lógicos
        assert isinstance(granja.es_dia, bool), (
            "❌ es_dia debe ser booleano (True/False).\n"
            "   Pista: self.es_dia = True"
        )
        
        assert isinstance(granja.hay_tormenta, bool), (
            "❌ hay_tormenta debe ser booleano (True/False).\n"
            "   Pista: self.hay_tormenta = False"
        )
        
        assert isinstance(granja.granja_operativa, bool), (
            "❌ granja_operativa debe ser booleano (True/False).\n"
            "   Pista: self.granja_operativa = True"
        )
        
        # Test: Transiciones de estado
        if hasattr(granja, 'cambiar_a_noche'):
            granja.cambiar_a_noche()
            assert granja.es_dia == False, (
                "❌ cambiar_a_noche() no actualiza es_dia.\n"
                "   Pista: self.es_dia = False"
            )
        
        if hasattr(granja, 'cambiar_a_dia'):
            granja.cambiar_a_dia()
            assert granja.es_dia == True, (
                "❌ cambiar_a_dia() no actualiza es_dia.\n"
                "   Pista: self.es_dia = True"
            )
        
        if hasattr(granja, 'iniciar_tormenta'):
            granja.iniciar_tormenta()
            assert granja.hay_tormenta == True, (
                "❌ iniciar_tormenta() no actualiza hay_tormenta.\n"
                "   Pista: self.hay_tormenta = True"
            )
        
        if hasattr(granja, 'terminar_tormenta'):
            granja.terminar_tormenta()
            assert granja.hay_tormenta == False, (
                "❌ terminar_tormenta() no actualiza hay_tormenta.\n"
                "   Pista: self.hay_tormenta = False"
            )
        
        # Test: Restricciones basadas en estado
        cultivo = Cultivo("tomate")
        
        # Test plantar de noche
        if hasattr(granja, 'puede_plantar'):
            granja.es_dia = False
            resultado, mensaje = granja.puede_plantar()
            assert resultado == False, (
                "❌ Permite plantar de noche.\n"
                "   Pista: if not self.es_dia: return False"
            )
            assert "día" in mensaje.lower(), (
                "❌ El mensaje no explica que solo se puede plantar de día.\n"
                "   Pista: Retorna mensaje explicativo"
            )
        
        # Test regar durante tormenta
        if hasattr(granja, 'puede_regar'):
            granja.es_dia = True
            granja.hay_tormenta = True
            resultado, mensaje = granja.puede_regar()
            assert resultado == False, (
                "❌ Permite regar durante tormenta.\n"
                "   Pista: if self.hay_tormenta: return False"
            )
            assert "tormenta" in mensaje.lower(), (
                "❌ El mensaje no explica sobre la tormenta.\n"
                "   Pista: Mensaje debe mencionar la tormenta"
            )
        
        # Test cosechar con granja no operativa
        if hasattr(granja, 'puede_cosechar'):
            granja.granja_operativa = False
            resultado, mensaje = granja.puede_cosechar()
            assert resultado == False, (
                "❌ Permite cosechar con granja no operativa.\n"
                "   Pista: if not self.granja_operativa: return False"
            )
            assert "operativa" in mensaje.lower() or "reparar" in mensaje.lower(), (
                "❌ El mensaje no explica sobre granja no operativa.\n"
                "   Pista: Mensaje debe explicar que hay que reparar"
            )
        
        # Test condiciones óptimas
        granja.es_dia = True
        granja.hay_tormenta = False  
        granja.granja_operativa = True
        
        if hasattr(granja, 'puede_plantar'):
            resultado, mensaje = granja.puede_plantar()
            assert resultado == True, (
                "❌ No permite acciones en condiciones óptimas.\n"
                "   Pista: Con todas las condiciones True, debería permitir"
            )
        
    except ImportError:
        pytest.fail(
            "❌ No se puede importar Farm.\n"
            "   Pista: Implementa las variables y métodos de estado en src/farm.py"
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
    print("TESTS NIVEL 2: CONTROL DE FLUJO")
    print("="*50 + "\n")
    
    tests = [
        ("Issue #9: Sistema de riego con condicionales", test_issue_9_irrigation_system),
        ("Issue #10: Lista de cultivos", test_issue_10_crop_list),
        ("Issue #11: Métodos de lista", test_issue_11_list_methods),
        ("Issue #12: Validación de entrada con if/else", test_issue_12_input_validation),
        ("Issue #13: Sistema de temporadas", test_issue_13_seasons_system),
        ("Issue #14: Comparación de cultivos", test_issue_14_crop_comparison),
        ("Issue #15: Estado del juego con booleanos", test_issue_15_game_state_booleans),
    ]
    
    for name, test_func in tests:
        try:
            test_func()
            mostrar_resultado_test(name, True)
        except Exception as e:
            mostrar_resultado_test(name, False)
            print(f"  Razón: {str(e)}\n")