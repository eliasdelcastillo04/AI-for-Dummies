import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Set dummy API key to avoid missing API key errors
os.environ["GEMINI_API_KEY"] = "dummy_test_key"

# We must mock llama_index classes before importing motor_rag because it instantiates them at the module level.
import sys
sys.modules['llama_index.llms.google_genai'] = MagicMock()
sys.modules['llama_index.embeddings.google_genai'] = MagicMock()
sys.modules['langfuse.llama_index'] = MagicMock()
sys.modules['llama_index.core'] = MagicMock()
sys.modules['llama_index.core.callbacks'] = MagicMock()
sys.modules['dotenv'] = MagicMock()

import logging
from agente_rag_cli.app_cli import main

class TestAppCLI(unittest.TestCase):
    @patch('agente_rag_cli.app_cli.inicializar_motor')
    @patch('agente_rag_cli.app_cli.logging.error')
    @patch('builtins.print')
    @patch('agente_rag_cli.app_cli.sys.exit')
    def test_inicializar_motor_error(self, mock_exit, mock_print, mock_logging_error, mock_inicializar_motor):
        test_exception = Exception("Test initialization error")
        mock_inicializar_motor.side_effect = test_exception

        # We need sys.exit to actually raise an exception to break the flow,
        # just like a real sys.exit would, otherwise it continues to `input()`
        mock_exit.side_effect = SystemExit(1)

        with self.assertRaises(SystemExit):
            main()

        mock_exit.assert_called_once_with(1)
        mock_logging_error.assert_called_once_with("Error al inicializar el motor RAG", exc_info=True)
        # Check that we print a message that has our exact words
        # The mock string may be split due to pep8 fixes, so check if it contains part of it
        found = False
        for call_args in mock_print.call_args_list:
            if call_args[0] and isinstance(call_args[0][0], str) and "Ocurrió un error interno" in call_args[0][0]:
                found = True
            if call_args[0] and isinstance(call_args[0][0], str):
                self.assertNotIn("Test initialization error", call_args[0][0])
        self.assertTrue(found)

if __name__ == '__main__':
    unittest.main()
