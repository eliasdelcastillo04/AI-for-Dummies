import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, PromptTemplate
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding

# Cargar las variables de entorno (por ejemplo, GOOGLE_API_KEY) de forma segura
load_dotenv()

# [ TAREA 7 ] Configurar LlamaIndex globalmente para usar Gemini
# Configuramos el LLM principal
llm = Gemini(model="models/gemini-1.5-flash")
# Configuramos el modelo de embeddings de Gemini
embed_model = GeminiEmbedding(model_name="models/embedding-001")

# Aplicamos la configuración global a LlamaIndex
Settings.llm = llm
Settings.embed_model = embed_model

def inicializar_motor():
    """
    [ TAREA 6 ] Función de ingesta para leer los archivos y crear el índice.
    """
    print("Ingestando documentos desde la carpeta 'data'...")
    # Leemos todos los documentos (txt, md, etc.) dentro del directorio 'data'
    documentos = SimpleDirectoryReader("data").load_data()
    
    # [ TAREA 7 ] Generar el índice vectorial a partir de los documentos leídos
    print("Generando el índice de embeddings...")
    indice = VectorStoreIndex.from_documents(documentos)
    return indice

def consultar_motor(indice, pregunta):
    """
    [ TAREA 8 ] Función de consulta (El Recomendador).
    Recibe una consulta de texto y busca la respuesta en el índice.
    """
    # Configurar un prompt estricto para evitar alucinaciones
    prompt_estricto = (
        "Eres un asesor experto de la empresa. Responde SOLO basándote en la información "
        "provista en los documentos. Si la respuesta no está, di 'No tengo esa información'.\n"
        "---------------------\n"
        "Contexto provisto:\n"
        "{context_str}\n"
        "---------------------\n"
        "Pregunta: {query_str}\n"
        "Respuesta: "
    )
    qa_prompt_template = PromptTemplate(prompt_estricto)
    
    # Crear el motor de búsqueda (query engine) pasando el prompt personalizado
    query_engine = indice.as_query_engine(text_qa_template=qa_prompt_template)
    
    # Realizar la consulta
    respuesta = query_engine.query(pregunta)
    return respuesta

if __name__ == "__main__":
    # Prueba rápida del sistema
    try:
        indice_rag = inicializar_motor()
        print("\n¡Índice creado con éxito! Probando consultas...\n")
        
        # Consultas de prueba
        preguntas = [
            "¿Cuánto cuesta el plan empresarial y qué incluye?",
            "¿Qué cuidados debo tener con la cámara Canon EOS R5?",
            "¿Cuál es el horario de atención de la oficina?" # Pregunta fuera de los documentos
        ]
        
        for pregunta in preguntas:
            print(f"🧑 Usuario: {pregunta}")
            respuesta = consultar_motor(indice_rag, pregunta)
            print(f"🤖 Asesor: {respuesta}\n")
            
    except Exception as e:
        print(f"Error al ejecutar el motor RAG: {e}")
