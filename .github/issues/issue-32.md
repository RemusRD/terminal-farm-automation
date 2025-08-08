# Issue #32: Clases y POO - Crear clase Farmer (🔴 Avanzado)

## Descripción
Implementa una clase `Farmer` completa usando programación orientada a objetos, con herencia, encapsulación y polimorfismo.

## Objetivos de Aprendizaje
- Programación Orientada a Objetos (POO)
- Clases, objetos y métodos
- Herencia y polimorfismo
- Encapsulación (propiedades públicas/privadas)
- Métodos especiales (__init__, __str__, __repr__)

## Tareas Específicas

### Tarea 1: Clase Base Farmer
En `src/farmer.py`, implementa la clase base:
```python
class Farmer:
    """Clase que representa un granjero/agricultor."""
    
    def __init__(self, name, experience=0, specialization="general"):
        """
        Inicializa un nuevo granjero.
        
        Args:
            name (str): Nombre del granjero
            experience (int): Puntos de experiencia
            specialization (str): Especialización del granjero
        """
        # TODO: Implementar constructor
        pass
    
    def __str__(self):
        """Representación string del granjero."""
        # TODO: Implementar
        pass
    
    def gain_experience(self, points):
        """Añade puntos de experiencia."""
        # TODO: Implementar
        pass
    
    def get_efficiency_bonus(self, task):
        """Calcula bonificación de eficiencia para una tarea."""
        # TODO: Implementar
        pass
```

### Tarea 2: Especializaciones con Herencia
Implementa clases especializadas:
```python
class CropSpecialist(Farmer):
    """Especialista en cultivos."""
    
    def __init__(self, name, favorite_crop="tomate"):
        super().__init__(name, 0, "crops")
        self.favorite_crop = favorite_crop
    
    def get_efficiency_bonus(self, task):
        """Bonificación especial para tareas de cultivos."""
        # TODO: Implementar bonificaciones específicas
        pass

class LivestockSpecialist(Farmer):
    """Especialista en ganado."""
    
    def __init__(self, name, animal_affinity="chickens"):
        super().__init__(name, 0, "livestock")
        self.animal_affinity = animal_affinity
    
    def get_efficiency_bonus(self, task):
        """Bonificación especial para tareas de ganado."""
        # TODO: Implementar bonificaciones específicas
        pass
```

### Tarea 3: Propiedades y Encapsulación
Implementa propiedades con validación:
```python
class Farmer:
    def __init__(self, name, experience=0, specialization="general"):
        self._name = name
        self._experience = max(0, experience)
        self._specialization = specialization
        self._level = self._calculate_level()
    
    @property
    def name(self):
        """Getter para el nombre."""
        return self._name
    
    @name.setter
    def name(self, value):
        """Setter para el nombre con validación."""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")
        self._name = value.strip()
    
    @property
    def level(self):
        """Nivel calculado basado en experiencia."""
        return self._level
    
    def _calculate_level(self):
        """Método privado para calcular nivel."""
        # TODO: Implementar cálculo de nivel
        pass
```

### Tarea 4: Polimorfismo con Tareas
Implementa sistema polimórfico de tareas:
```python
def execute_farm_task(farmer, task_type, *args, **kwargs):
    """
    Ejecuta una tarea usando polimorfismo.
    
    Args:
        farmer (Farmer): El granjero que ejecuta la tarea
        task_type (str): Tipo de tarea
        *args, **kwargs: Argumentos de la tarea
    
    Returns:
        dict: Resultado de la tarea con bonificaciones aplicadas
    """
    # TODO: Implementar sistema polimórfico
    pass
```

## Criterios de Éxito
- [x] ✅ La clase Farmer tiene constructor y métodos básicos
- [x] ✅ Implementa herencia con clases especializadas
- [x] ✅ Usa propiedades con getters y setters
- [x] ✅ Métodos privados para encapsulación
- [x] ✅ Polimorfismo funcional con diferentes tipos de granjeros
- [x] ✅ Validación de datos en setters

## Archivos a Crear/Modificar
- `src/farmer.py` (nuevo archivo)

## Pistas
- Usa `@property` y `@nombre.setter` para propiedades
- Métodos que empiezan con `_` son "privados"
- `super()` llama métodos de la clase padre
- `isinstance()` para verificar tipos
- Las clases especializadas pueden sobreescribir métodos

## Nivel de Dificultad: 🔴 Avanzado
**Tiempo estimado:** 60-75 minutos

## Tecnologías y Conceptos
- Programación Orientada a Objetos
- Herencia y polimorfismo
- Encapsulación
- Propiedades (properties)
- Métodos especiales
- Validación de datos