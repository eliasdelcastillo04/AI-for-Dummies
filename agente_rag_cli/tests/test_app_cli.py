import pytest
import sys
import os
from unittest.mock import MagicMock

# Mock motor_rag module completely before importing app_cli to avoid Gemini API calls during import
sys.modules['motor_rag'] = MagicMock()

# Agrega el directorio padre al sys.path para poder importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app_cli import main

def test_main_initialization_exception(mocker, capsys):
    # Mock limpiar_pantalla to prevent clearing the console during tests
    mocker.patch('app_cli.limpiar_pantalla')

    # Mock inicializar_motor to raise an exception
    mocker.patch('app_cli.inicializar_motor', side_effect=Exception("Test initialization error"))

    # Run main() and check that sys.exit(1) is called
    with pytest.raises(SystemExit) as e:
        main()

    assert e.value.code == 1

    # Verify the output
    captured = capsys.readouterr()
    assert "Error al inicializar el motor RAG: Test initialization error" in captured.out
