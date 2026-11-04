# Implementação
def validar_documento(documento):
    if not documento or not isinstance(documento, str):
        return False
    doc_limpo = documento.replace(".", "").replace("-", "")
    return doc_limpo.isdigit() and len(doc_limpo) == 11

# Testes Unitários
def test_documento_11_digitos():
    assert validar_documento("12345678901") is True

def test_documento_formatado():
    assert validar_documento("123.456.789-00") is True

def test_documento_menos_11_digitos():
    assert validar_documento("1234567890") is False

def test_documento_mais_11_digitos():
    assert validar_documento("123456789012") is False

def test_documento_com_letras():
    assert validar_documento("123.abc.789-00") is False

def test_documento_vazio():
    assert validar_documento("") is False