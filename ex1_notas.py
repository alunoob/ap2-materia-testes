import pytest

# Implementação
def classificar_produto(quantidade):
    if quantidade < 0:
        return "Quantidade inválida"
    if quantidade == 0:
        return "Sem estoque"
    if 1 <= quantidade <= 5:
        return "Estoque baixo"
    if 6 <= quantidade <= 20:
        return "Estoque normal"
    return "Estoque alto"

# Testes Unitários
def test_produto_sem_estoque():
    assert classificar_produto(0) == "Sem estoque"

def test_produto_estoque_baixo():
    assert classificar_produto(3) == "Estoque baixo"

def test_produto_estoque_normal():
    assert classificar_produto(10) == "Estoque normal"

def test_produto_estoque_alto():
    assert classificar_produto(25) == "Estoque alto"

def test_quantidade_negativa():
    assert classificar_produto(-1) == "Quantidade inválida"

@pytest.mark.parametrize("qtd, esperado", [
    (1, "Estoque baixo"), (5, "Estoque baixo"),
    (6, "Estoque normal"), (20, "Estoque normal"),
    (21, "Estoque alto")
])
def test_valores_limites(qtd, esperado):
    assert classificar_produto(qtd) == esperado

#aaaa
