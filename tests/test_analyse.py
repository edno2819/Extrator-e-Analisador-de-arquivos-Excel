from pytest import mark

def test_meu():
    assert 5 == 4

def test_x():
    assert 4==4


def test_y():
    assert 4>=0


@mark.parametrize('entrada', [1, 2, 3 ,4 ,5])
def test_parametrizacao(entrada):
    assert type(entrada) == float

@mark.parametrize('entrada, esperado', [(1, 5), (2, 6), ('tes', 3)])
def test_parametrizacao(entrada, esperado):
    assert entrada + 4 == esperado
