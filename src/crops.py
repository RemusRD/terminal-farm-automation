"""Sistema de Cultivos - Definiciones y lógica de cultivos"""

# Issue #2: Los tipos de datos están mal definidos
class Cultivo:
    """Representa un cultivo en la granja"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        
        # Issue #2: Estos deberían tener los tipos correctos
        self.tiempo_crecimiento = "3"  # Debería ser int
        self.precio = "15.50"  # Debería ser float
        self.necesita_agua = "si"  # Debería ser bool
        self.dias_plantado = "0"  # Debería ser int
        
        # Issue #23: Falta usar diccionario para datos de cultivos
        # Los datos están hardcodeados en lugar de venir de un diccionario
        
    def puede_cosechar(self):
        """Verifica si el cultivo está listo para cosechar"""
        # Issue #3: Error de tipos - no se puede comparar string con string así
        return self.dias_plantado >= self.tiempo_crecimiento
        
    def regar(self):
        """Riega el cultivo"""
        # Issue #9: Falta lógica para cambiar necesita_agua
        print(f"Regando {self.nombre}")
        
    def crecer(self):
        """Hace crecer el cultivo un día"""
        # Issue #3: No se puede sumar 1 a un string
        self.dias_plantado = self.dias_plantado + 1

# Issue #23: Debería existir un diccionario con todos los tipos de cultivos
# CULTIVOS_DISPONIBLES = {
#     "tomate": {
#         "tiempo": 3,
#         "precio": 15.50,
#         "semilla_costo": 5
#     },
#     ...
# }