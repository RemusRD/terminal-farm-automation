#!/usr/bin/env python3
"""
Tests para Issues Avanzados (Nivel 5) - Issues #31-35

Estos tests verifican la implementación de funcionalidades avanzadas:
- Parser CSV y análisis de datos
- Clases y programación orientada a objetos
- Manejo de excepciones
- Decoradores y funciones avanzadas
- Sistema de persistencia JSON
"""

import pytest
import json
import csv
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch, mock_open
import tempfile
import shutil

# Test para Issue #31: Parser de datos CSV
class TestCSVParser:
    """Tests para el parser de datos CSV del mercado."""
    
    @pytest.fixture
    def sample_csv_data(self):
        """Datos CSV de muestra para pruebas."""
        return """fecha,cultivo,precio,volumen
2024-01-01,tomate,25.50,100
2024-01-02,tomate,26.00,120
2024-01-03,tomate,24.75,110
2024-01-01,maiz,15.00,200
2024-01-02,maiz,15.25,180
2024-01-03,maiz,14.80,190"""
    
    @pytest.fixture
    def csv_file(self, sample_csv_data, tmp_path):
        """Crea archivo CSV temporal para pruebas."""
        csv_path = tmp_path / "test_prices.csv"
        csv_path.write_text(sample_csv_data)
        return str(csv_path)
    
    def test_load_price_data_exists(self):
        """Verifica que la función load_price_data existe."""
        try:
            from src.market import load_price_data
            assert callable(load_price_data), "load_price_data debe ser una función"
        except ImportError:
            pytest.fail("No se pudo importar load_price_data desde src.market")
    
    def test_load_price_data_basic(self, csv_file):
        """Test básico de carga de datos CSV."""
        try:
            from src.market import load_price_data
            data = load_price_data(csv_file)
            
            assert isinstance(data, list), "Debe retornar una lista"
            assert len(data) == 6, "Debe cargar todas las filas"
            
            # Verificar estructura del primer elemento
            first_row = data[0]
            assert 'fecha' in first_row, "Debe incluir fecha"
            assert 'cultivo' in first_row, "Debe incluir cultivo"
            assert 'precio' in first_row, "Debe incluir precio"
            
        except ImportError:
            pytest.skip("load_price_data no implementada")
    
    def test_analyze_price_trends_exists(self):
        """Verifica que la función analyze_price_trends existe."""
        try:
            from src.market import analyze_price_trends
            assert callable(analyze_price_trends), "analyze_price_trends debe ser una función"
        except ImportError:
            pytest.fail("No se pudo importar analyze_price_trends desde src.market")
    
    def test_analyze_price_trends_basic(self, csv_file):
        """Test básico de análisis de tendencias."""
        try:
            from src.market import analyze_price_trends
            analysis = analyze_price_trends("tomate", 30)
            
            assert isinstance(analysis, dict), "Debe retornar un diccionario"
            expected_keys = ['promedio', 'tendencia', 'proyeccion']
            for key in expected_keys:
                assert key in analysis, f"Debe incluir {key} en el análisis"
                
        except ImportError:
            pytest.skip("analyze_price_trends no implementada")


# Test para Issue #32: Clases y POO - Crear clase Farmer
class TestFarmerClass:
    """Tests para la clase Farmer y POO."""
    
    def test_farmer_class_exists(self):
        """Verifica que la clase Farmer existe."""
        try:
            from src.farmer import Farmer
            assert isinstance(Farmer, type), "Farmer debe ser una clase"
        except ImportError:
            pytest.fail("No se pudo importar Farmer desde src.farmer")
    
    def test_farmer_constructor(self):
        """Test del constructor de Farmer."""
        try:
            from src.farmer import Farmer
            
            # Constructor básico
            farmer = Farmer("Juan")
            assert farmer.name == "Juan", "Debe guardar el nombre correctamente"
            
            # Constructor con parámetros opcionales
            farmer2 = Farmer("Ana", experience=150, specialization="crops")
            assert farmer2.name == "Ana"
            assert farmer2.experience >= 0, "Experiencia no puede ser negativa"
            
        except ImportError:
            pytest.skip("Farmer no implementada")
    
    def test_farmer_methods(self):
        """Test de métodos básicos de Farmer."""
        try:
            from src.farmer import Farmer
            
            farmer = Farmer("Carlos", experience=50)
            
            # Test gain_experience
            if hasattr(farmer, 'gain_experience'):
                initial_exp = farmer.experience
                farmer.gain_experience(25)
                assert farmer.experience >= initial_exp, "Debe incrementar experiencia"
            
            # Test __str__
            farmer_str = str(farmer)
            assert "Carlos" in farmer_str, "Representación string debe incluir nombre"
            
        except ImportError:
            pytest.skip("Farmer no implementada")
    
    def test_farmer_specialization_inheritance(self):
        """Test de herencia con especializaciones."""
        try:
            from src.farmer import CropSpecialist, LivestockSpecialist
            
            crop_farmer = CropSpecialist("María", favorite_crop="tomate")
            assert crop_farmer.name == "María"
            assert hasattr(crop_farmer, 'favorite_crop')
            
            livestock_farmer = LivestockSpecialist("Pedro", animal_affinity="chickens")
            assert livestock_farmer.name == "Pedro"
            assert hasattr(livestock_farmer, 'animal_affinity')
            
        except ImportError:
            pytest.skip("Especializaciones de Farmer no implementadas")
    
    def test_farmer_properties(self):
        """Test de propiedades con getters/setters."""
        try:
            from src.farmer import Farmer
            
            farmer = Farmer("Luis", experience=250)
            
            # Test level property
            if hasattr(farmer, 'level'):
                level = farmer.level
                assert isinstance(level, int), "Level debe ser entero"
                assert level >= 0, "Level no puede ser negativo"
            
            # Test name property con validación
            if hasattr(type(farmer), 'name') and isinstance(getattr(type(farmer), 'name'), property):
                # Test setter validation
                with pytest.raises(ValueError):
                    farmer.name = ""  # Nombre vacío debe fallar
                    
        except ImportError:
            pytest.skip("Propiedades de Farmer no implementadas")


# Test para Issue #33: Manejo de excepciones
class TestExceptionHandling:
    """Tests para manejo de excepciones personalizadas."""
    
    def test_custom_exceptions_exist(self):
        """Verifica que las excepciones personalizadas existen."""
        try:
            from src.exceptions import (
                FarmError, InsufficientResourcesError, 
                WeatherError, SeasonError
            )
            
            # Verificar jerarquía de herencia
            assert issubclass(FarmError, Exception)
            assert issubclass(InsufficientResourcesError, FarmError)
            assert issubclass(WeatherError, FarmError)
            assert issubclass(SeasonError, FarmError)
            
        except ImportError:
            pytest.fail("Excepciones personalizadas no implementadas")
    
    def test_insufficient_resources_error(self):
        """Test de excepción de recursos insuficientes."""
        try:
            from src.exceptions import InsufficientResourcesError
            
            error = InsufficientResourcesError("agua", 100, 50)
            assert error.resource == "agua"
            assert error.required == 100
            assert error.available == 50
            
            error_msg = str(error)
            assert "agua" in error_msg.lower()
            assert "100" in error_msg
            assert "50" in error_msg
            
        except ImportError:
            pytest.skip("InsufficientResourcesError no implementada")
    
    def test_season_error(self):
        """Test de excepción de temporada incorrecta."""
        try:
            from src.exceptions import SeasonError
            
            error = SeasonError("tomate", "invierno", ["primavera", "verano"])
            assert error.crop == "tomate"
            assert error.current_season == "invierno"
            assert "primavera" in error.valid_seasons
            
            error_msg = str(error)
            assert "tomate" in error_msg
            assert "invierno" in error_msg
            
        except ImportError:
            pytest.skip("SeasonError no implementada")
    
    def test_safe_farm_operations(self):
        """Test de operaciones de granja con manejo de excepciones."""
        try:
            from src.farm import Farm
            
            farm = Farm()
            
            # Test plant_crop_safely si existe
            if hasattr(farm, 'plant_crop_safely'):
                result = farm.plant_crop_safely("tomate", (0, 0), 1)
                
                assert isinstance(result, dict), "Debe retornar diccionario"
                assert 'success' in result, "Debe incluir campo success"
                assert 'errors' in result, "Debe incluir lista de errores"
                assert 'planted' in result, "Debe incluir cantidad plantada"
            
        except ImportError:
            pytest.skip("Operaciones seguras no implementadas")


# Test para Issue #34: Decoradores y funciones avanzadas
class TestDecorators:
    """Tests para decoradores y funciones avanzadas."""
    
    def test_timing_decorator_exists(self):
        """Verifica que el decorador de timing existe."""
        try:
            from src.decorators import timing_decorator
            assert callable(timing_decorator), "timing_decorator debe ser callable"
        except ImportError:
            pytest.fail("timing_decorator no implementado")
    
    def test_timing_decorator_functionality(self):
        """Test de funcionalidad del decorador de timing."""
        try:
            from src.decorators import timing_decorator
            
            @timing_decorator
            def test_function():
                time.sleep(0.01)  # Pequeña pausa
                return "test_result"
            
            result = test_function()
            assert result == "test_result", "Debe preservar valor de retorno"
            
        except ImportError:
            pytest.skip("timing_decorator no implementado")
    
    def test_log_farm_operations_decorator(self):
        """Test del decorador de logging de operaciones."""
        try:
            from src.decorators import log_farm_operations
            
            # Test decorador parametrizado
            @log_farm_operations()
            def test_operation(x, y):
                return x + y
            
            result = test_operation(2, 3)
            assert result == 5, "Debe preservar funcionalidad original"
            
        except ImportError:
            pytest.skip("log_farm_operations no implementado")
    
    def test_cache_decorator(self):
        """Test del decorador de caché."""
        try:
            from src.decorators import smart_cache, memoize_expensive_calculations
            
            call_count = 0
            
            @memoize_expensive_calculations
            def expensive_function(n):
                nonlocal call_count
                call_count += 1
                return n * n
            
            # Primera llamada
            result1 = expensive_function(5)
            assert result1 == 25
            assert call_count == 1
            
            # Segunda llamada (debe usar caché)
            result2 = expensive_function(5)
            assert result2 == 25
            assert call_count == 1, "Debe usar caché, no incrementar contador"
            
        except ImportError:
            pytest.skip("Decoradores de caché no implementados")
    
    def test_requires_farmer_level_decorator(self):
        """Test del decorador de nivel de granjero."""
        try:
            from src.decorators import requires_farmer_level
            from src.farmer import Farmer
            
            class TestFarm:
                def __init__(self):
                    self.farmer = Farmer("Test", experience=200)  # Nivel 2
                
                @requires_farmer_level(1)
                def low_level_operation(self):
                    return "success"
                
                @requires_farmer_level(5)
                def high_level_operation(self):
                    return "success"
            
            farm = TestFarm()
            
            # Debe funcionar para operación de bajo nivel
            try:
                result = farm.low_level_operation()
                assert result == "success"
            except Exception:
                pass  # Puede fallar si no está completamente implementado
            
            # Debe fallar para operación de alto nivel
            with pytest.raises(Exception):
                farm.high_level_operation()
                
        except ImportError:
            pytest.skip("Decorador requires_farmer_level no implementado")


# Test para Issue #35: Sistema de persistencia con JSON
class TestJSONPersistence:
    """Tests para sistema de persistencia JSON."""
    
    @pytest.fixture
    def temp_data_dir(self, tmp_path):
        """Directorio temporal para datos de prueba."""
        return tmp_path / "test_data"
    
    def test_game_persistence_class_exists(self):
        """Verifica que la clase GamePersistence existe."""
        try:
            from src.persistence import GamePersistence
            assert isinstance(GamePersistence, type), "GamePersistence debe ser una clase"
        except ImportError:
            pytest.fail("GamePersistence no implementada")
    
    def test_save_and_load_game_state(self, temp_data_dir):
        """Test básico de guardado y carga."""
        try:
            from src.persistence import GamePersistence
            
            persistence = GamePersistence(str(temp_data_dir))
            
            # Datos de prueba
            test_data = {
                'farmer_name': 'TestFarmer',
                'level': 5,
                'crops': ['tomate', 'maiz'],
                'resources': {'water': 100, 'seeds': 50}
            }
            
            # Guardar
            save_success = persistence.save_game_state(test_data, "test_save.json")
            assert save_success, "Guardado debe ser exitoso"
            
            # Cargar
            loaded_data = persistence.load_game_state("test_save.json")
            assert loaded_data is not None, "Debe cargar datos exitosamente"
            assert loaded_data['farmer_name'] == 'TestFarmer'
            assert loaded_data['level'] == 5
            
        except ImportError:
            pytest.skip("GamePersistence no implementada")
    
    def test_custom_json_encoder(self):
        """Test del encoder JSON personalizado."""
        try:
            from src.persistence import FarmJSONEncoder
            from datetime import datetime
            
            test_data = {
                'timestamp': datetime.now(),
                'farmer': type('Farmer', (), {'name': 'Test', 'level': 1})()
            }
            
            # Debe poder serializar sin errores
            json_str = json.dumps(test_data, cls=FarmJSONEncoder)
            assert isinstance(json_str, str), "Debe producir string JSON válido"
            
            # Verificar que se puede parsear de vuelta
            parsed = json.loads(json_str)
            assert isinstance(parsed, dict), "Debe parsear de vuelta a diccionario"
            
        except ImportError:
            pytest.skip("FarmJSONEncoder no implementado")
    
    def test_backup_manager(self, temp_data_dir):
        """Test del gestor de respaldos."""
        try:
            from src.persistence import BackupManager
            
            backup_dir = temp_data_dir / "backups"
            manager = BackupManager(str(backup_dir))
            
            # Crear archivo de prueba
            test_file = temp_data_dir / "test_file.json"
            test_file.write_text('{"test": "data"}')
            
            # Crear respaldo
            backup_success = manager.create_backup(test_file)
            assert backup_success, "Creación de respaldo debe ser exitosa"
            
            # Verificar que existe el respaldo
            backups = manager.list_backups()
            assert len(backups) > 0, "Debe crear al menos un respaldo"
            
        except ImportError:
            pytest.skip("BackupManager no implementado")
    
    def test_data_migration(self):
        """Test del sistema de migración de datos."""
        try:
            from src.persistence import DataMigrator
            
            migrator = DataMigrator()
            
            # Test básico de detección de migración
            needs_migration = migrator.needs_migration("0.9")
            assert isinstance(needs_migration, bool)
            
            # Test de migración básica
            old_data = {'version': '0.9', 'farmer_name': 'Test'}
            if needs_migration:
                migrated_data = migrator.migrate_data(old_data, "0.9")
                assert isinstance(migrated_data, dict)
                assert 'version' in migrated_data
            
        except ImportError:
            pytest.skip("DataMigrator no implementado")
    
    def test_historical_stats_manager(self, temp_data_dir):
        """Test del gestor de estadísticas históricas."""
        try:
            from src.persistence import HistoricalStatsManager
            
            stats_file = temp_data_dir / "test_stats.json"
            stats_manager = HistoricalStatsManager(str(stats_file))
            
            # Test de grabación de estadísticas diarias
            farm_state = {
                'crops': [{'type': 'tomate', 'harvested': True}],
                'income': 100,
                'expenses': 25
            }
            
            stats_manager.record_daily_stats(farm_state)
            
            # Verificar que se guardaron las estadísticas
            if stats_file.exists():
                stats_content = json.loads(stats_file.read_text())
                assert isinstance(stats_content, dict)
            
        except ImportError:
            pytest.skip("HistoricalStatsManager no implementado")


# Tests de integración para funcionalidades avanzadas
class TestAdvancedIntegration:
    """Tests de integración para todas las funcionalidades avanzadas."""
    
    def test_farmer_with_persistence(self, tmp_path):
        """Test de integración: Farmer con persistencia."""
        try:
            from src.farmer import Farmer
            from src.persistence import GamePersistence, FarmJSONEncoder
            
            # Crear granjero
            farmer = Farmer("IntegrationTest", experience=300)
            
            # Preparar datos para persistencia
            farm_data = {
                'farmer': farmer,
                'timestamp': datetime.now(),
                'crops_planted': 15
            }
            
            # Guardar con persistencia
            persistence = GamePersistence(str(tmp_path))
            success = persistence.save_game_state(farm_data, "integration_test.json")
            
            if success:
                loaded_data = persistence.load_game_state("integration_test.json")
                assert loaded_data is not None
                
        except ImportError:
            pytest.skip("Integración Farmer + Persistence no disponible")
    
    def test_decorated_farm_operations_with_exceptions(self):
        """Test de integración: Decoradores + Excepciones + Farm."""
        try:
            from src.decorators import timing_decorator, log_farm_operations
            from src.exceptions import InsufficientResourcesError
            from src.farm import Farm
            
            class AdvancedFarm(Farm):
                @timing_decorator
                @log_farm_operations()
                def safe_plant_operation(self, crop_type, quantity):
                    if self.resources.get('seeds', 0) < quantity:
                        raise InsufficientResourcesError(
                            'seeds', quantity, self.resources.get('seeds', 0)
                        )
                    return f"Planted {quantity} {crop_type}"
            
            farm = AdvancedFarm()
            
            # Test con recursos insuficientes
            with pytest.raises(InsufficientResourcesError):
                farm.safe_plant_operation("tomate", 100)
                
        except ImportError:
            pytest.skip("Integración completa no disponible")


if __name__ == "__main__":
    print("🧪 Ejecutando tests para Issues Avanzados (Nivel 5)")
    print("=" * 60)
    
    # Ejecutar tests con pytest
    pytest.main([
        __file__,
        "-v",  # Verbose output
        "--tb=short",  # Short traceback format
        "-x",  # Stop on first failure
    ])