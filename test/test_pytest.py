import pytest
from program import num_shelf, name_owner, new_doc

def test_num_shelf():
    assert num_shelf('10006') == '2'

def test_name_owner():
    assert name_owner('10006') == 'Аристарх Павлов'

parametrs = [
    ('passport', '4323', 'Kirill', {'type': 'passport', 'number': '4323', 'name': 'Kirill'})
]

@pytest.mark.parametrize("tip, nomer, name, result", parametrs)
def test_new_doc(tip, nomer, name, result):
    assert new_doc(tip, nomer, name) == result
