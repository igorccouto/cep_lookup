import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lookup


def test_returns_bool():
    validated_cep = lookup.validate_CEP(CEP='67120938')
    assert isinstance(validated_cep, bool)

def test_valid_CEP_as_input_returns_true():
    validated_cep = lookup.validate_CEP(CEP='67120938')
    assert validated_cep

def test_invalid_CEP_as_input_returns_false():
    invalid_ceps =  ['6712093', '671209388']
    for cep in invalid_ceps:
        validated_cep = lookup.validate_CEP(CEP=cep)
        assert not validated_cep
