import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lookup


def test_returns_dict():
     cep_info = lookup.get_CEP(CEP='67120938')
     isinstance(cep_info, dict)
