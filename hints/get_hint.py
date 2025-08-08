#!/usr/bin/env python3
"""Sistema de Hints - Proporciona pistas progresivas para cada issue"""

import json
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

class HintSystem:
    def __init__(self):
        self.hints_file = Path(__file__).parent / "hints.json"
        self.progress_file = Path(__file__).parent / ".hint_progress.json"
        self.load_hints()
        self.load_progress()
        
    def load_hints(self):
        """Carga los hints desde el archivo JSON"""
        with open(self.hints_file, 'r', encoding='utf-8') as f:
            self.hints = json.load(f)
            
    def load_progress(self):
        """Carga el progreso del usuario"""
        if self.progress_file.exists():
            with open(self.progress_file, 'r') as f:
                self.progress = json.load(f)
        else:
            self.progress = {}
            
    def save_progress(self):
        """Guarda el progreso del usuario"""
        with open(self.progress_file, 'w') as f:
            json.dump(self.progress, f)
            
    def get_hint(self, issue_number):
        """Obtiene el hint apropiado para un issue"""
        issue_key = f"issue_{issue_number}"
        
        if issue_key not in self.hints:
            print(f"❌ No hay hints disponibles para el Issue #{issue_number}")
            return
            
        issue_hints = self.hints[issue_key]
        
        # Inicializar progreso si es primera vez
        if issue_key not in self.progress:
            self.progress[issue_key] = {
                "first_access": datetime.now().isoformat(),
                "hints_shown": 0
            }
            self.save_progress()
            
        # Calcular tiempo transcurrido
        first_access = datetime.fromisoformat(self.progress[issue_key]["first_access"])
        time_elapsed = (datetime.now() - first_access).total_seconds() / 60  # minutos
        
        print(f"\n{'='*60}")
        print(f"HINTS PARA: {issue_hints['titulo']}")
        print(f"{'='*60}\n")
        
        hints_shown = 0
        
        # Mostrar hints según el tiempo transcurrido
        for i in range(1, 4):
            hint_key = f"hint_{i}"
            if hint_key in issue_hints:
                hint = issue_hints[hint_key]
                unlock_time = hint["unlock_after_minutes"]
                
                if time_elapsed >= unlock_time:
                    print(f"{'─'*60}")
                    print(f"HINT {i}:")
                    print(hint["text"])
                    print()
                    hints_shown += 1
                else:
                    minutes_remaining = unlock_time - int(time_elapsed)
                    print(f"{'─'*60}")
                    print(f"HINT {i}: 🔒 Se desbloqueará en {minutes_remaining} minutos")
                    print(f"(Intenta resolver el problema por tu cuenta primero)")
                    print()
                    break
                    
        if hints_shown == 0:
            print("¡El primer hint ya está disponible!")
            print(f"HINT 1:")
            print(issue_hints["hint_1"]["text"])
            
        # Actualizar progreso
        self.progress[issue_key]["hints_shown"] = hints_shown
        self.save_progress()
        
        print(f"{'='*60}")
        print("💡 Recuerda: Los hints están diseñados para guiar tu")
        print("   pensamiento, no para darte la solución directamente.")
        print(f"{'='*60}\n")

def main():
    """Función principal"""
    if len(sys.argv) < 2:
        print("Uso: python get_hint.py [numero_issue]")
        print("Ejemplo: python get_hint.py 9")
        sys.exit(1)
        
    try:
        issue_number = int(sys.argv[1])
    except ValueError:
        print("❌ Por favor proporciona un número de issue válido")
        sys.exit(1)
        
    hint_system = HintSystem()
    hint_system.get_hint(issue_number)

if __name__ == "__main__":
    main()