import pytest
from unittest.mock import MagicMock, patch

# Ajustamos os imports para buscar explicitamente dentro do pacote 'src'
from src.message_service import build_message
from src.zapi_client import ZApiClient

def test_build_message_format_exato():
    """Garante que a mensagem gerada segue rigorosamente o padrão do desafio."""
    nome_teste = "Luciano"
    mensagem_esperada = "Olá, Luciano tudo bem com você?"
    
    resultado = build_message(nome_teste)
    
    assert resultado == mensagem_esperada, f"A mensagem deveria ser exatamente: '{mensagem_esperada}'"

@patch('requests.post')
def test_send_message_sucesso(mock_post):
    """Testa se o método send_message se comporta bem quando a Z-API responde sucesso (200)."""
    # Configura o Mock para simular uma resposta HTTP 200 (Sucesso)
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_post.return_value = mock_response

    # Instancia o cliente da Z-API
    zapi = ZApiClient()
    
    response = zapi.send_message("5581999999999", "Olá, Luciano tudo bem com você?")
    
    assert response.status_code == 200
    mock_post.assert_called_once()  # Garante que a requisição HTTP foi feita exatamente uma vez

@patch('requests.post')
def test_send_message_falha(mock_post):
    """Testa se o sistema lida corretamente quando a Z-API retorna um erro (ex: 400)."""
    # Configura o Mock para simular uma resposta de erro HTTP 400
    mock_response = MagicMock()
    mock_response.status_code = 400
    mock_response.text = "Instance not connected"
    mock_post.return_value = mock_response

    zapi = ZApiClient()
    response = zapi.send_message("5581999999999", "Olá, Luciano tudo bem com você?")
    
    assert response.status_code == 400
    assert "Instance not connected" in response.text