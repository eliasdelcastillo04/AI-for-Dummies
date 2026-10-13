import sys
import os
from unittest.mock import patch, MagicMock

# Add parent directory to sys.path to import app_cli
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# Mock motor_rag to avoid initializing GoogleGenAI which requires API key
sys.modules['motor_rag'] = MagicMock()

from app_cli import limpiar_pantalla  # noqa: E402


@patch('app_cli.os.system')
@patch('app_cli.os.name', 'nt')
def test_limpiar_pantalla_windows(mock_system):
    """Test that limpiar_pantalla uses 'cls' when os.name is 'nt'."""
    limpiar_pantalla()
    mock_system.assert_called_once_with('cls')


@patch('app_cli.os.system')
@patch('app_cli.os.name', 'posix')
def test_limpiar_pantalla_posix(mock_system):
    """Test that limpiar_pantalla uses 'clear' when os.name is not 'nt'."""
    limpiar_pantalla()
    mock_system.assert_called_once_with('clear')
