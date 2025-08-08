"""Sistema de Inventario - Gestión de items y recursos"""

class Inventario:
    """Maneja el inventario del jugador"""
    
    def __init__(self):
        # Issue #10: cultivos debería ser una lista, no None
        self.cultivos = None
        
        # Issue #11: semillas debería ser una lista
        self.semillas = "tomate, maíz"  # Debería ser lista
        
        # Issue #4: Faltan variables importantes
        # TODO: Añadir dinero, herramientas, etc.
        
    def agregar_cultivo(self, cultivo):
        """Añade un cultivo al inventario"""
        # Issue #11: No se puede hacer append a None
        self.cultivos.append(cultivo)
        
    def remover_cultivo(self, cultivo):
        """Remueve un cultivo del inventario"""
        # Issue #11: Método incompleto
        pass
        
    def contar_cultivos(self):
        """Cuenta cuántos cultivos hay"""
        # Issue #10: No se puede hacer len() de None
        return len(self.cultivos)
        
    def ordenar_por_valor(self):
        """Ordena cultivos por su valor"""
        # Issue #11: Falta implementar sort con key
        pass
        
    def mostrar_inventario(self):
        """Muestra el contenido del inventario"""
        # Issue #1: Print mal formateado
        print === INVENTARIO ===
        print("Cultivos:", self.cultivos)
        print("Semillas:", self.semillas)