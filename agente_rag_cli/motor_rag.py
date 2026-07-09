import os
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, PromptTemplate
from llama_index.core.callbacks import CallbackManager
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from langfuse.llama_index import LlamaIndexCallbackHandler

# Cargar las variables de entorno (por ejemplo, GOOGLE_API_KEY) de forma segura
load_dotenv()

# [ TAREA 7 ] Configurar LlamaIndex globalmente para usar Gemini
# Configuramos el LLM principal con reintentos
llm = GoogleGenAI(
    model="gemini-2.5-flash",
    max_retries=10
)
# Configuramos el modelo de embeddings de Gemini con un tamaño de lote menor y reintentos automáticos
embed_model = GoogleGenAIEmbedding(
    model_name="models/gemini-embedding-2",
    embed_batch_size=5,  # Reducido de 10 para evitar saturar la cuota de peticiones
    retries=10,
    retry_min_seconds=5.0,
    retry_max_seconds=60.0,
    retry_exponential_base=2.0
)

# Aplicamos la configuración global a LlamaIndex
Settings.llm = llm
Settings.embed_model = embed_model

# [ TAREA 14 ] Configurar el Callback de Langfuse para Telemetría y Observabilidad
langfuse_callback_handler = LlamaIndexCallbackHandler(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST") or os.getenv("LANGFUSE_BASE_URL") or "https://cloud.langfuse.com"
)
Settings.callback_manager = CallbackManager([langfuse_callback_handler])

def inicializar_motor():
    """
    [ TAREA 6 ] Función de ingesta para leer los archivos y crear el índice.
    """
    print("Ingestando documentos desde la carpeta 'data'...")
    # Leemos todos los documentos dentro de 'data' de forma recursiva (incluyendo subcarpetas)
    documentos = SimpleDirectoryReader("data", recursive=True).load_data()
    
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
        
        # Consulta de prueba solicitada por la directiva de MLOps
        pregunta = "¿Qué incluye el Plan Básico y cuál es la política de devoluciones?"
        
        print(f"🧑 Usuario: {pregunta}")
        respuesta = consultar_motor(indice_rag, pregunta)
        print(f"🤖 Asesor: {respuesta}\n")
        
        # Alerta de validación de Langfuse
        print("⚠️  [ALERTA MLOPS] Revisa el panel web de Langfuse (Host: https://cloud.langfuse.com) para verificar la generación exitosa del Trace y los costos/latencias asociados a esta consulta.")
            
    except Exception as e:
        print(f"Error al ejecutar el motor RAG: {e}")
    finally:
        # Asegurar que todas las trazas pendientes sean enviadas a Langfuse antes de terminar
        print("Enviando trazas pendientes a Langfuse...")
        langfuse_callback_handler.flush()
