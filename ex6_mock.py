from unittest.mock import patch

# Implementação
def obter_proximo_cliente():
    pass

def registrar_atendimento(cliente):
    pass

def atender_proximo_cliente():
    cliente = obter_proximo_cliente()
    if not cliente:
        return "Fila vazia"
    
    if registrar_atendimento(cliente):
        return "Atendimento realizado"
    return "Falha no atendimento"

# Testes Unitários
@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_atendimento_realizado_sucesso(mock_obter, mock_registrar):
    mock_obter.return_value = "Cliente A"
    mock_registrar.return_value = True
    assert atender_proximo_cliente() == "Atendimento realizado"

@patch(f"{__name__}.obter_proximo_cliente")
def test_fila_vazia(mock_obter):
    mock_obter.return_value = None
    assert atender_proximo_cliente() == "Fila vazia"

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_falha_registrar_atendimento(mock_obter, mock_registrar):
    mock_obter.return_value = "Cliente A"
    mock_registrar.return_value = False
    assert atender_proximo_cliente() == "Falha no atendimento"

@patch(f"{__name__}.obter_proximo_cliente")
def test_obter_proximo_cliente_chamada(mock_obter):
    mock_obter.return_value = None
    atender_proximo_cliente()
    mock_obter.assert_called()

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_registrar_atendimento_cliente_correto(mock_obter, mock_registrar):
    mock_obter.return_value = "Cliente B"
    atender_proximo_cliente()
    mock_registrar.assert_called_with("Cliente B")

@patch(f"{__name__}.registrar_atendimento")
@patch(f"{__name__}.obter_proximo_cliente")
def test_registrar_atendimento_nao_chamada_fila_vazia(mock_obter, mock_registrar):
    mock_obter.return_value = None
    atender_proximo_cliente()
    mock_registrar.assert_not_called()

    #aaa