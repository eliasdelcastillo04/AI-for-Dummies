# Agente RAG CLI con LlamaIndex, Gemini y Langfuse

Este es un asistente conversacional interactivo basado en terminal (CLI) que utiliza la arquitectura **RAG (Retrieval-Augmented Generation)**. Permite realizar consultas sobre un conjunto de documentos locales de manera precisa, asegurando que las respuestas se basen únicamente en la información provista (mitigando alucinaciones), además de integrar telemetría de producción con **Langfuse**.

---

## 🚀 Arquitectura y Tecnologías

- **LlamaIndex**: Framework para la ingesta de datos de la carpeta `data/` y la orquestación del flujo RAG (indexación vectorial y motor de consultas).
- **Gemini (Google GenAI)**:
  - **LLM**: `gemini-2.5-flash` para la generación de respuestas.
  - **Embeddings**: `models/gemini-embedding-2` para indexar vectorialmente los textos de conocimiento.
- **Langfuse**: Observabilidad, monitoreo y telemetría avanzada para evaluar latencias, costos (tokens) y rastrear la ejecución de cada componente del flujo RAG.
- **python-dotenv**: Gestión segura de credenciales locales.

---

## 🛠️ Requisitos e Instalación

### 1. Clonar e ingresar al proyecto
Asegúrate de estar en el directorio raíz del proyecto CLI:
```bash
cd estudio/agente_rag_cli
```

### 2. Configurar el Entorno Virtual
Se recomienda utilizar Python 3.10 o superior (ejemplo con Python 3.12):
```bash
python3 -m venv venv312
source venv312/bin/activate
```

### 3. Instalar Dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Configurar Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto y configura tus credenciales para Google Gemini y Langfuse:
```env
# API Key de Google Gemini
GEMINI_API_KEY="tu_api_key_aqui"

# Configuración de Langfuse para Observabilidad
LANGFUSE_SECRET_KEY="tu_secret_key_aqui"
LANGFUSE_PUBLIC_KEY="tu_public_key_aqui"
LANGFUSE_BASE_URL="https://cloud.langfuse.com"
```

---

## 💻 Uso de la Aplicación

### 1. Colocar documentos de consulta
Agrega todos tus archivos de texto (`.txt`, `.md`, etc.) dentro de la carpeta `data/`. El sistema los leerá e indexará automáticamente.

### 2. Ejecutar la interfaz de consola interactiva
Arranca la aplicación interactiva de consola:
```bash
python app_cli.py
```

### 3. Ejecutar una consulta de prueba rápida
También puedes ejecutar el motor RAG directamente para verificar la integración y enviar una consulta única de prueba:
```bash
python motor_rag.py
```

---

## 🔍 Características y Funciones Clave

- **Indexación Dinámica**: Carga todos los documentos ubicados dentro de la carpeta `data/` de forma reciclada automáticamente en memoria.
- **Control de Alucinaciones**: El sistema está configurado con reglas estrictas de prompt de sistema. Si preguntas algo que no se encuentra documentado en los archivos provistos, el asesor responderá exactamente: **"No tengo esa información"**.
- **Monitoreo de Telemetría**: Cada consulta realizada a través de la CLI se envía en tiempo real como un Trace a Langfuse. Esto permite rastrear:
  - Latencia de la consulta y de la llamada al LLM.
  - Consumo detallado de tokens de entrada y salida (costos).
  - Pasos detallados del pipeline de LlamaIndex (recuperación de nodos de contexto y síntesis de respuesta).
