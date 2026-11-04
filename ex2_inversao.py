# Implementação
def inverter_palavras(texto):
    if not texto.strip():
        return ""
    return " ".join(texto.split()[::-1])

# Testes Unitários
def test_frase_varias_palavras():
    assert inverter_palavras("Python é muito interessante") == "interessante muito é Python"

def test_frase_uma_palavra():
    assert inverter_palavras("Python") == "Python"

def test_frase_vazia():
    assert inverter_palavras("") == ""

def test_frase_espacos_extras():
    assert inverter_palavras("  Python   é   legal  ") == "legal é Python"

def test_frase_numeros_letras():
    assert inverter_palavras("Versão 3 de Python") == "Python de 3 Versão"