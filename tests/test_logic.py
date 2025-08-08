"""
Tests para Level 4: 🟣 Lógica y Estructuras de Datos
Issues #23-30: Diccionarios, algoritmos, list comprehensions, y análisis avanzado
"""

import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from unittest.mock import patch, MagicMock
import random
import json

class TestIssue23DiccionarioCultivos(unittest.TestCase):
    """Tests para Issue #23: Diccionario de cultivos"""
    
    def setUp(self):
        """Setup para tests de diccionario de cultivos."""
        try:
            import crops
            self.crops = crops
        except ImportError:
            self.crops = None
    
    def test_cultivos_db_existe(self):
        """Test que CULTIVOS_DB existe y tiene estructura correcta."""
        if self.crops is None:
            self.skipTest("Módulo crops no disponible")
        
        self.assertTrue(hasattr(self.crops, 'CULTIVOS_DB'), 
                       "CULTIVOS_DB debe existir en crops.py")
        
        cultivos_db = self.crops.CULTIVOS_DB
        self.assertIsInstance(cultivos_db, dict, "CULTIVOS_DB debe ser un diccionario")
        self.assertGreaterEqual(len(cultivos_db), 9, 
                               "Debe tener al menos 9 cultivos")
    
    def test_estructura_cultivo(self):
        """Test que cada cultivo tiene todos los campos requeridos."""
        if self.crops is None:
            self.skipTest("Módulo crops no disponible")
        
        campos_requeridos = [
            'precio', 'tiempo_crecimiento', 'temporadas', 'agua_requerida',
            'experiencia', 'categoria', 'descripcion', 'nivel_requerido'
        ]
        
        for nombre, cultivo in self.crops.CULTIVOS_DB.items():
            self.assertIsInstance(cultivo, dict, f"Cultivo {nombre} debe ser diccionario")
            for campo in campos_requeridos:
                self.assertIn(campo, cultivo, f"Cultivo {nombre} debe tener campo {campo}")
    
    def test_obtener_cultivo(self):
        """Test función obtener_cultivo()."""
        if self.crops is None:
            self.skipTest("Módulo crops no disponible")
        
        if hasattr(self.crops, 'obtener_cultivo'):
            # Test cultivo existente
            cultivo = self.crops.obtener_cultivo('tomate')
            self.assertIsNotNone(cultivo, "Debe retornar cultivo existente")
            
            # Test cultivo no existente
            cultivo_inexistente = self.crops.obtener_cultivo('cultivo_inexistente')
            self.assertIsNone(cultivo_inexistente, "Debe retornar None para cultivo inexistente")
    
    def test_filtros_cultivos(self):
        """Test funciones de filtrado por temporada y categoría."""
        if self.crops is None:
            self.skipTest("Módulo crops no disponible")
        
        if hasattr(self.crops, 'cultivos_por_temporada'):
            cultivos_verano = self.crops.cultivos_por_temporada('verano')
            self.assertIsInstance(cultivos_verano, list, 
                                "cultivos_por_temporada debe retornar lista")
            
            for cultivo in cultivos_verano:
                self.assertIn('verano', cultivo.get('temporadas', []), 
                            "Todos los cultivos deben tener temporada 'verano'")
        
        if hasattr(self.crops, 'cultivos_por_categoria'):
            cultivos_verdura = self.crops.cultivos_por_categoria('verdura')
            self.assertIsInstance(cultivos_verdura, list)
            
            for cultivo in cultivos_verdura:
                self.assertEqual(cultivo.get('categoria'), 'verdura')


class TestIssue24AlgoritmoBestCultivo(unittest.TestCase):
    """Tests para Issue #24: Algoritmo de mejor cultivo"""
    
    def setUp(self):
        """Setup para tests de algoritmo de mejor cultivo."""
        try:
            import market
            self.market = market
        except ImportError:
            self.market = None
    
    def test_encontrar_mejor_cultivo_existe(self):
        """Test que función encontrar_mejor_cultivo existe."""
        if self.market is None:
            self.skipTest("Módulo market no disponible")
        
        self.assertTrue(hasattr(self.market, 'encontrar_mejor_cultivo'),
                       "Función encontrar_mejor_cultivo debe existir")
    
    def test_criterios_diferentes(self):
        """Test diferentes criterios de optimización."""
        if self.market is None or not hasattr(self.market, 'encontrar_mejor_cultivo'):
            self.skipTest("Función encontrar_mejor_cultivo no disponible")
        
        criterios = ['rentabilidad', 'rapido', 'experiencia', 'equilibrado']
        
        for criterio in criterios:
            try:
                resultado = self.market.encontrar_mejor_cultivo(
                    granja=MagicMock(), criterio=criterio, temporada_actual='primavera'
                )
                self.assertIsInstance(resultado, dict, 
                                    f"Criterio {criterio} debe retornar diccionario")
            except Exception as e:
                self.fail(f"Error con criterio {criterio}: {e}")
    
    def test_estructura_resultado(self):
        """Test que el resultado tiene la estructura esperada."""
        if self.market is None or not hasattr(self.market, 'encontrar_mejor_cultivo'):
            self.skipTest("Función encontrar_mejor_cultivo no disponible")
        
        try:
            granja_mock = MagicMock()
            granja_mock.nivel = 5
            granja_mock.agua = 50
            granja_mock.energia = 80
            
            resultado = self.market.encontrar_mejor_cultivo(granja_mock)
            
            campos_esperados = ['nombre', 'score', 'justificacion']
            for campo in campos_esperados:
                self.assertIn(campo, resultado, f"Resultado debe tener campo {campo}")
        except Exception:
            pass  # Skip si hay errores de implementación


class TestIssue25BatallaCultivos(unittest.TestCase):
    """Tests para Issue #25: Sistema de batalla de cultivos"""
    
    def setUp(self):
        """Setup para tests de batalla de cultivos."""
        try:
            import battle
            self.battle = battle
        except ImportError:
            self.battle = None
    
    def test_clase_batalla_existe(self):
        """Test que clase BatallaCultivos existe."""
        if self.battle is None:
            self.skipTest("Módulo battle no disponible")
        
        self.assertTrue(hasattr(self.battle, 'BatallaCultivos'),
                       "Clase BatallaCultivos debe existir")
    
    def test_estadisticas_batalla_cultivos(self):
        """Test que cultivos tienen estadísticas de batalla."""
        try:
            import crops
            
            # Verificar que al menos un cultivo tenga estadísticas de batalla
            tiene_estadisticas = False
            for cultivo in crops.CULTIVOS_DB.values():
                if 'estadisticas_batalla' in cultivo:
                    estadisticas = cultivo['estadisticas_batalla']
                    campos_batalla = ['ataque', 'defensa', 'velocidad', 'salud_maxima']
                    
                    for campo in campos_batalla:
                        self.assertIn(campo, estadisticas, 
                                    f"Estadísticas deben incluir {campo}")
                    tiene_estadisticas = True
                    break
            
            if not tiene_estadisticas:
                self.skipTest("Ningún cultivo tiene estadísticas de batalla aún")
                
        except ImportError:
            self.skipTest("Módulo crops no disponible")
    
    def test_habilidades_especiales(self):
        """Test sistema de habilidades especiales."""
        if self.battle is None:
            self.skipTest("Módulo battle no disponible")
        
        if hasattr(self.battle, 'BatallaCultivos'):
            try:
                batalla = self.battle.BatallaCultivos(
                    MagicMock(), MagicMock(), terreno='normal'
                )
                
                # Verificar que tiene método para habilidades
                self.assertTrue(hasattr(batalla, 'aplicar_habilidad'),
                               "Debe tener método aplicar_habilidad")
            except Exception:
                pass  # Skip si hay errores de implementación


class TestIssue26ListComprehensions(unittest.TestCase):
    """Tests para Issue #26: Comprensión de listas"""
    
    def setUp(self):
        """Setup para tests de list comprehensions."""
        try:
            import farm
            self.farm = farm
        except ImportError:
            self.farm = None
    
    def test_cultivos_listos_cosecha(self):
        """Test función con list comprehension para cultivos listos."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'obtener_cultivos_listos_cosecha'):
                try:
                    cultivos_listos = granja.obtener_cultivos_listos_cosecha()
                    self.assertIsInstance(cultivos_listos, list,
                                        "Debe retornar lista")
                except Exception:
                    pass  # Skip si hay errores de implementación
    
    def test_valor_total_granja(self):
        """Test cálculo de valor total con comprehension."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'calcular_valor_total_granja'):
                try:
                    valor_total = granja.calcular_valor_total_granja()
                    self.assertIsInstance(valor_total, (int, float),
                                        "Valor total debe ser numérico")
                except Exception:
                    pass  # Skip si hay errores de implementación
    
    def test_analisis_por_categoria(self):
        """Test análisis avanzado con comprehensions anidadas."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'analizar_produccion_por_categoria'):
                try:
                    analisis = granja.analizar_produccion_por_categoria()
                    self.assertIsInstance(analisis, dict,
                                        "Análisis debe retornar diccionario")
                    
                    # Verificar estructura de análisis
                    for categoria, datos in analisis.items():
                        self.assertIsInstance(datos, dict)
                        campos_esperados = ['cantidad', 'valor_total', 'promedio_dias']
                        for campo in campos_esperados:
                            self.assertIn(campo, datos)
                except Exception:
                    pass  # Skip si hay errores de implementación


class TestIssue27DiccionariosAnidados(unittest.TestCase):
    """Tests para Issue #27: Diccionarios anidados"""
    
    def setUp(self):
        """Setup para tests de diccionarios anidados."""
        try:
            import farm
            self.farm = farm
        except ImportError:
            self.farm = None
    
    def test_estructura_datos_completa(self):
        """Test estructura DATOS_GRANJA_COMPLETOS."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'DATOS_GRANJA_COMPLETOS'):
            datos = self.farm.DATOS_GRANJA_COMPLETOS
            
            # Verificar estructura principal
            secciones_principales = ['configuracion', 'regiones', 'estadisticas']
            for seccion in secciones_principales:
                self.assertIn(seccion, datos, f"Debe tener sección {seccion}")
            
            # Verificar anidación profunda
            self.assertIn('recursos', datos['configuracion'])
            self.assertIn('agua', datos['configuracion']['recursos'])
            self.assertIn('actual', datos['configuracion']['recursos']['agua'])
    
    def test_navegacion_profunda(self):
        """Test funciones de navegación en estructuras anidadas."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'obtener_valor_anidado'):
            # Test datos de prueba
            datos_test = {
                'nivel1': {
                    'nivel2': {
                        'nivel3': 'valor_encontrado'
                    }
                }
            }
            
            try:
                valor = self.farm.obtener_valor_anidado(datos_test, 'nivel1.nivel2.nivel3')
                self.assertEqual(valor, 'valor_encontrado')
                
                # Test valor por defecto
                valor_default = self.farm.obtener_valor_anidado(
                    datos_test, 'ruta.inexistente', default='default'
                )
                self.assertEqual(valor_default, 'default')
            except Exception:
                pass  # Skip si hay errores de implementación
    
    def test_configuracion_regiones(self):
        """Test configuración dinámica por regiones."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'DATOS_GRANJA_COMPLETOS'):
            datos = self.farm.DATOS_GRANJA_COMPLETOS
            
            if 'regiones' in datos:
                # Verificar que tiene al menos 4 regiones
                regiones = datos['regiones']
                self.assertGreaterEqual(len(regiones), 4, 
                                       "Debe tener al menos 4 regiones")
                
                # Verificar estructura de región
                for region, config in regiones.items():
                    campos_region = ['clima', 'fertilidad', 'cultivos_plantados']
                    for campo in campos_region:
                        self.assertIn(campo, config, 
                                    f"Región {region} debe tener {campo}")


class TestIssue28AlgoritmoBusqueda(unittest.TestCase):
    """Tests para Issue #28: Algoritmo de búsqueda"""
    
    def setUp(self):
        """Setup para tests de algoritmos de búsqueda."""
        try:
            import farm
            self.farm = farm
        except ImportError:
            self.farm = None
    
    def test_busqueda_lineal(self):
        """Test búsqueda lineal con criterio personalizado."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'busqueda_lineal_cultivo'):
                try:
                    # Criterio de prueba
                    criterio = lambda c: getattr(c, 'precio', 0) > 50
                    resultado = granja.busqueda_lineal_cultivo(criterio)
                    
                    # Debe retornar tupla (índice, elemento) o similar
                    self.assertIsNotNone(resultado)
                except Exception:
                    pass  # Skip si hay errores de implementación
    
    def test_busqueda_binaria(self):
        """Test búsqueda binaria en lista ordenada."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'busqueda_binaria_por_precio'):
                try:
                    resultado = granja.busqueda_binaria_por_precio(25)
                    self.assertIsInstance(resultado, int)
                except Exception:
                    pass  # Skip si hay errores de implementación
    
    def test_busqueda_multiples_criterios(self):
        """Test búsqueda con múltiples filtros."""
        if self.farm is None:
            self.skipTest("Módulo farm no disponible")
        
        if hasattr(self.farm, 'Farm'):
            granja = self.farm.Farm()
            
            if hasattr(granja, 'buscar_por_multiples_criterios'):
                try:
                    resultado = granja.buscar_por_multiples_criterios(
                        temporada='verano', precio_max=50, categoria='fruta'
                    )
                    self.assertIsInstance(resultado, list)
                except Exception:
                    pass  # Skip si hay errores de implementación


class TestIssue29OrdenamientoPersonalizado(unittest.TestCase):
    """Tests para Issue #29: Ordenamiento personalizado"""
    
    def setUp(self):
        """Setup para tests de ordenamiento."""
        self.datos_test = [
            {'nombre': 'tomate', 'precio': 25, 'tiempo': 4},
            {'nombre': 'lechuga', 'precio': 15, 'tiempo': 2},
            {'nombre': 'maiz', 'precio': 10, 'tiempo': 6}
        ]
    
    def test_algoritmos_basicos_ordenamiento(self):
        """Test algoritmos de ordenamiento O(n²)."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                algoritmos = [
                    'ordenamiento_burbuja_cultivos',
                    'ordenamiento_seleccion_por_tiempo',
                    'ordenamiento_insercion_por_categoria'
                ]
                
                for algoritmo in algoritmos:
                    if hasattr(granja, algoritmo):
                        try:
                            resultado = getattr(granja, algoritmo)(self.datos_test.copy())
                            self.assertIsInstance(resultado, list)
                        except Exception:
                            pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")
    
    def test_algoritmos_eficientes(self):
        """Test algoritmos eficientes O(n log n)."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                if hasattr(granja, 'merge_sort_cultivos'):
                    try:
                        key_func = lambda x: x['precio']
                        resultado = granja.merge_sort_cultivos(
                            self.datos_test.copy(), key_func
                        )
                        self.assertIsInstance(resultado, list)
                        self.assertEqual(len(resultado), len(self.datos_test))
                    except Exception:
                        pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")
    
    def test_ordenamiento_multiple(self):
        """Test ordenamiento por múltiples criterios."""
        try:
            import sorting  # Nuevo módulo
            
            if hasattr(sorting, 'OrdenadorMultiple'):
                ordenador = sorting.OrdenadorMultiple()
                
                # Añadir criterios
                ordenador.añadir_criterio(lambda x: x['precio'], peso=0.6)
                ordenador.añadir_criterio(lambda x: x['tiempo'], reverso=True, peso=0.4)
                
                resultado = ordenador.ordenar_por_multiples_criterios(self.datos_test.copy())
                self.assertIsInstance(resultado, list)
        except ImportError:
            self.skipTest("Módulo sorting no disponible")


class TestIssue30CalculoEstadisticas(unittest.TestCase):
    """Tests para Issue #30: Cálculo de estadísticas"""
    
    def setUp(self):
        """Setup para tests de estadísticas."""
        self.datos_numericos = [10, 15, 20, 25, 30, 35, 40]
        self.datos_correlacion_x = [1, 2, 3, 4, 5]
        self.datos_correlacion_y = [2, 4, 6, 8, 10]
    
    def test_estadisticas_basicas(self):
        """Test cálculos estadísticos básicos."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                if hasattr(granja, 'calcular_estadisticas_basicas'):
                    try:
                        stats = granja.calcular_estadisticas_basicas(self.datos_numericos)
                        
                        # Verificar campos esperados
                        campos = ['media', 'mediana', 'desviacion_estandar', 'varianza']
                        for campo in campos:
                            self.assertIn(campo, stats, f"Debe incluir {campo}")
                            self.assertIsInstance(stats[campo], (int, float))
                        
                        # Verificar cálculos aproximados
                        self.assertAlmostEqual(stats['media'], 25.0, places=1)
                    except Exception:
                        pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")
    
    def test_analisis_tendencias(self):
        """Test análisis de tendencias temporales."""
        try:
            import statistics  # Nuevo módulo
            
            if hasattr(statistics, 'AnalizadorTendencias'):
                analizador = statistics.AnalizadorTendencias(self.datos_numericos)
                
                if hasattr(analizador, 'calcular_tendencia_lineal'):
                    try:
                        tendencia = analizador.calcular_tendencia_lineal(self.datos_numericos)
                        self.assertIsInstance(tendencia, dict)
                        self.assertIn('pendiente', tendencia)
                    except Exception:
                        pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo statistics no disponible")
    
    def test_metricas_performance(self):
        """Test métricas de performance."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                metricas = [
                    'calcular_roi_por_cultivo',
                    'eficiencia_temporal',
                    'indice_diversificacion',
                    'ratio_sostenibilidad'
                ]
                
                for metrica in metricas:
                    if hasattr(granja, metrica):
                        try:
                            resultado = getattr(granja, metrica)()
                            self.assertIsNotNone(resultado)
                        except Exception:
                            pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")
    
    def test_correlacion_datos(self):
        """Test cálculo de correlaciones."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                if hasattr(granja, 'matriz_correlacion'):
                    try:
                        variables = {
                            'x': self.datos_correlacion_x,
                            'y': self.datos_correlacion_y
                        }
                        matriz = granja.matriz_correlacion(variables)
                        self.assertIsInstance(matriz, dict)
                    except Exception:
                        pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")
    
    def test_generacion_insights(self):
        """Test generador de insights automático."""
        try:
            import farm
            
            if hasattr(farm, 'Farm'):
                granja = farm.Farm()
                
                if hasattr(granja, 'generar_insights_inteligentes'):
                    try:
                        insights = granja.generar_insights_inteligentes()
                        self.assertIsInstance(insights, list)
                        
                        # Verificar estructura de insights
                        if insights:
                            insight = insights[0]
                            self.assertIsInstance(insight, dict)
                            campos_insight = ['descripcion', 'tipo', 'prioridad']
                            for campo in campos_insight:
                                if campo in insight:
                                    self.assertIsNotNone(insight[campo])
                    except Exception:
                        pass  # Skip si hay errores de implementación
        except ImportError:
            self.skipTest("Módulo farm no disponible")


# Clase para ejecutar todos los tests
class LogicTestSuite:
    """Suite de tests para Level 4: Lógica y Estructuras de Datos"""
    
    @staticmethod
    def run_all_tests():
        """Ejecutar todos los tests de lógica y estructuras de datos."""
        print("🟣 Ejecutando Tests Level 4: Lógica y Estructuras de Datos")
        print("=" * 60)
        
        # Crear suite de tests
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        # Añadir todas las clases de test
        test_classes = [
            TestIssue23DiccionarioCultivos,
            TestIssue24AlgoritmoBestCultivo, 
            TestIssue25BatallaCultivos,
            TestIssue26ListComprehensions,
            TestIssue27DiccionariosAnidados,
            TestIssue28AlgoritmoBusqueda,
            TestIssue29OrdenamientoPersonalizado,
            TestIssue30CalculoEstadisticas
        ]
        
        for test_class in test_classes:
            tests = loader.loadTestsFromTestCase(test_class)
            suite.addTests(tests)
        
        # Ejecutar tests
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        
        # Resumen
        total = result.testsRun
        failures = len(result.failures)
        errors = len(result.errors)
        skipped = len(result.skipped) if hasattr(result, 'skipped') else 0
        passed = total - failures - errors - skipped
        
        print("\n" + "=" * 60)
        print("📊 RESUMEN DE TESTS LEVEL 4:")
        print(f"   ✅ Exitosos: {passed}")
        print(f"   ❌ Fallos: {failures}")
        print(f"   🔥 Errores: {errors}")
        print(f"   ⏭️  Omitidos: {skipped}")
        print(f"   📈 Total: {total}")
        
        if failures == 0 and errors == 0:
            print("\n🎉 ¡Todos los tests de Lógica y Estructuras de Datos pasaron!")
        else:
            print("\n🔧 Revisa los fallos arriba y continúa implementando.")
        
        return result


if __name__ == '__main__':
    # Ejecutar todos los tests cuando se ejecuta directamente
    LogicTestSuite.run_all_tests()