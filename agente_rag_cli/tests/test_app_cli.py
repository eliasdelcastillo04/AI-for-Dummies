import pytest
from unittest.mock import patch
import os

# We need to mock Settings before motor_rag is imported
with patch.dict(os.environ, {"GEMINI_API_KEY": "dummy"}):
    with patch('llama_index.core.Settings'):
        with patch('llama_index.llms.google_genai.GoogleGenAI'), \
                patch('llama_index.embeddings.google_genai.'
                      'GoogleGenAIEmbedding'):
            # Import main function directly for testing
            from agente_rag_cli.app_cli import main


def test_main_initialization_error(capsys):
    with patch('agente_rag_cli.app_cli.limpiar_pantalla') as mock_limpiar, \
            patch('agente_rag_cli.app_cli.inicializar_motor') as mock_init, \
            patch('agente_rag_cli.app_cli.langfuse_callback_handler'):

        # Configure the mock for inicializar_motor to raise an exception
        mock_init.side_effect = Exception("Test initialization error")

        # Call the main function and assert that it exits with code 1
        with pytest.raises(SystemExit) as excinfo:
            main()

        assert excinfo.value.code == 1

        # Check standard output
        captured = capsys.readouterr()
        assert "❌ Error al inicializar el motor RAG:" in captured.out
        assert "Test initialization error" in captured.out

        # Verify the mocks were called
        mock_limpiar.assert_called()
        mock_init.assert_called_once()
