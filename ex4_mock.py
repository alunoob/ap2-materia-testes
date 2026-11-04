from unittest.mock import patch

# Implementação
def gerar_codigo():
    return "USR-0000"

def criar_identificacao(nome):
    codigo = gerar_codigo()
    return f"Usuário {nome} cadastrado com código {codigo}."

# Testes Unitários
@patch(f"{__name__}.gerar_codigo")
def test_mensagem_gerada_corretamente(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    resultado = criar_identificacao("Carlos")
    assert resultado == "Usuário Carlos cadastrado com código USR-1234."

@patch(f"{__name__}.gerar_codigo")
def test_gerar_codigo_foi_chamada(mock_gerar_codigo):
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called()

@patch(f"{__name__}.gerar_codigo")
def test_chamada_apenas_uma_vez(mock_gerar_codigo):
    criar_identificacao("Carlos")
    mock_gerar_codigo.assert_called_once()

@patch(f"{__name__}.gerar_codigo")
def test_simular_diferentes_codigos(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-9999"
    assert criar_identificacao("Ana") == "Usuário Ana cadastrado com código USR-9999."

@patch(f"{__name__}.gerar_codigo")
def test_comportamento_nomes_diferentes(mock_gerar_codigo):
    mock_gerar_codigo.return_value = "USR-1234"
    assert criar_identificacao("Maria") == "Usuário Maria cadastrado com código USR-1234."