# Issue #25: Sistema de batalla de cultivos

## 🟣 Level 4: Lógica y Estructuras de Datos

### Descripción
Crear un sistema de batalla automática entre cultivos donde diferentes plantas compiten por recursos, territorio y supervivencia usando algoritmos de simulación.

### Objetivo de Aprendizaje
- Implementar sistemas de simulación
- Trabajar con algoritmos de combate
- Manejar estados complejos de objetos
- Crear lógica de eventos aleatorios

### Tareas Específicas

1. **Añadir propiedades de batalla a cultivos en `src/crops.py`:**
   ```python
   # Extender CULTIVOS_DB con:
   'estadisticas_batalla': {
       'ataque': 15,           # Agresividad del cultivo
       'defensa': 10,          # Resistencia a ataques
       'velocidad': 8,         # Orden de ataque
       'salud_maxima': 100,    # Puntos de vida
       'habilidades': ['drenar_agua', 'crecer_rapido'],
       'tipo_batalla': 'agresivo'  # 'agresivo', 'defensivo', 'equilibrado'
   }
   ```

2. **Implementar clase `BatallaCultivos` en nuevo archivo `src/battle.py`:**
   ```python
   class BatallaCultivos:
       def __init__(self, cultivo1, cultivo2, terreno='normal'):
           # Inicializar batalla
           
       def simular_batalla(self):
           # Algoritmo de batalla por turnos
           
       def aplicar_habilidad(self, cultivo, habilidad, objetivo):
           # Sistema de habilidades especiales
   ```

3. **Algoritmo de batalla:**
   - Turnos basados en velocidad
   - Cálculo de daño: `max(1, atacante.ataque - defensor.defensa)`
   - Modificadores por tipo de terreno
   - Eventos aleatorios (tormentas, plagas)
   - Sistema de ventajas por tipo (verduras vs frutas vs granos)

4. **Habilidades especiales:**
   - `drenar_agua`: Reduce recursos del oponente
   - `crecer_rapido`: Aumenta estadísticas temporalmente
   - `espinas`: Daño de contrarreque
   - `regenerar`: Recupera salud
   - `envenenar`: Daño por turnos

### Archivos Afectados
- `src/crops.py` (estadísticas de batalla)
- `src/battle.py` (nueva clase)
- `src/farm.py` (integración de batallas)

### Tests Esperados
- Simulación de batalla completa funciona
- Habilidades se activan correctamente
- Modificadores de terreno aplican
- Eventos aleatorios ocurren
- Resultados son consistentes con lógica

### Ejemplo de Uso
```python
tomate = Cultivo('tomate')
maiz = Cultivo('maiz')

batalla = BatallaCultivos(tomate, maiz, terreno='fertil')
resultado = batalla.simular_batalla()

print(f"Ganador: {resultado['ganador']}")
print(f"Turnos: {resultado['turnos']}")
print(f"Log: {resultado['log_batalla']}")
```

### Criterios de Éxito
- [ ] Todos los cultivos tienen estadísticas de batalla
- [ ] Clase BatallaCultivos completamente implementada
- [ ] Al menos 5 habilidades especiales funcionando
- [ ] Sistema de ventajas por tipo
- [ ] Eventos aleatorios integrados
- [ ] Tests cubren diferentes escenarios
- [ ] Log detallado de la batalla

### Dificultad: 🟣🟣🟣 Muy Alto
### Tiempo Estimado: 75-90 minutos
### Conceptos: Simulación, algoritmos de combate, programación orientada a objetos, eventos aleatorios