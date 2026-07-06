import os
import sys
from motor_rag import inicializar_motor, consultar_motor

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    limpiar_pantalla()
    print("==================================================")
    print("        SISTEMA RAG INTERACTIVO - DELCAST          ")
    print("==================================================")
    print("Cargando y procesando la base de datos de conocimiento...")
    
    try:
        # Inicializar el motor RAG una sola vez al arrancar
        indice = inicializar_motor()
        print("\n✅ ¡Base de conocimiento cargada con éxito!")
    except Exception as e:
        print(f"\n❌ Error al inicializar el motor RAG: {e}")
        sys.exit(1)
        
    input("\nPresiona [Enter] para abrir la interfaz de consultas...")
    
    while True:
        limpiar_pantalla()
        print("==================================================")
        print("        SISTEMA RAG INTERACTIVO - DELCAST          ")
        print("==================================================")
        print("Escribe tu pregunta o escribe 'salir' para finalizar.\n")
        
        pregunta = input("🧑 Consulta: ").strip()
        
        # Ignorar inputs vacíos
        if not pregunta:
            continue
            
        # Salir del bucle
        if pregunta.lower() in ['salir', 'exit', 'quit']:
            print("\n👋 ¡Gracias por usar el Asesor RAG! Saliendo...")
            break
            
        print("\n🤖 Buscando en los documentos...")
        try:
            respuesta = consultar_motor(indice, pregunta)
            print("\n-------------------- RESPUESTA --------------------")
            print(respuesta)
            print("---------------------------------------------------")
        except Exception as e:
            print(f"\n❌ Error al consultar el motor RAG: {e}")
            
        input("\nPresiona [Enter] para realizar otra consulta...")

if __name__ == "__main__":
    main()
