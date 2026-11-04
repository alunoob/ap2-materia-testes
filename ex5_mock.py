from unittest.mock import patch

# Implementação
def verificar_permissao(usuario):
    return False

def acessar_sistema(usuario):
    if verificar_permissao(usuario):
        return "Acesso autorizado"
    return "Acesso negado"

# Testes Unitários
@patch(f"{__name__}.verificar_permissao")
def test_usuario_com_permissao(mock_permissao):
    mock_permissao.return_value = True
    assert acessar_sistema("admin") == "Acesso autorizado"

@patch(f"{__name__}.verificar_permissao")
def test_usuario_sem_permissao(mock_permissao):
    mock_permissao.return_value = False
    assert acessar_sistema("convidado") == "Acesso negado"

@patch(f"{__name__}.verificar_permissao")
def test_verificar_permissao_chamada(mock_permissao):
    acessar_sistema("admin")
    mock_permissao.assert_called()

@patch(f"{__name__}.verificar_permissao")
def test_chamada_usuario_correto(mock_permissao):
    acessar_sistema("joao")
    mock_permissao.assert_called_with("joao")

@patch(f"{__name__}.verificar_permissao")
def test_simular_dois_cenarios(mock_permissao):
    mock_permissao.side_effect = [True, False]
    assert acessar_sistema("user1") == "Acesso autorizado"
    assert acessar_sistema("user2") == "Acesso negado"