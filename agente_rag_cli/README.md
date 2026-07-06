# Agente RAG CLI con LlamaIndex y Gemini

Este es un asistente conversacional interactivo basado en terminal (CLI) que utiliza la arquitectura **RAG (Retrieval-Augmented Generation)**. Permite realizar consultas sobre un conjunto de documentos locales de manera precisa, asegurando que las respuestas se basen únicamente en la información provista (mitigando alucinaciones).

## 🚀 Arquitectura y Tecnologías
- **LlamaIndex**: Para la ingesta de datos de la carpeta `data/` y la orquestación del flujo RAG (índice de embeddings y motor de consultas).
- **Gemini (Google GenAI)**:
  - **LLM**: `gemini-2.5-flash` para la generación de respuestas.
  - **Embeddings**: `gemini-embedding-2` para indexar vectorialmente los textos de conocimiento.
- **python-dotenv**: Gestión segura de credenciales locales.

---

## 🛠️ Requisitos e Instalación

### 1. Clonar e ingresar al proyecto
Asegúrate de estar en el directorio raíz del proyecto CLI:
```bash
cd estudio/agente_rag_cli
```

### 2. Configurar la API Key
Crea un archivo `.env` en la raíz del proyecto y agrega tu API Key de Google Gemini:
```env
GOOGLE_API_KEY=tu_api_key_aqui
```

### 3. Crear el Entorno Virtual
Se recomienda utilizar Python 3.10 o superior:
```bash
python3 -m venv venv312
source venv312/bin/activate
```

### 4. Instalar Dependencias
Instala los paquetes necesarios definidos en `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## 💻 Uso de la Aplicación

Para arrancar la interfaz de consola interactiva:
```bash
python app_cli.py
```

### Características del Sistema:
- **Indexación Dinámica**: Carga todos los documentos de texto (`.txt`, `.md`) ubicados dentro de la carpeta `data/` en memoria automáticamente.
- **Control de Alucinaciones**: El sistema está configurado con reglas estrictas de prompt de sistema. Si preguntas algo que no está documentado en los archivos de la carpeta `data/`, responderá exactamente: **"No tengo esa información"**.
