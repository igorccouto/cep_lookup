import os
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import lookup


def test_returns_string():
    formatted_cep = lookup.format_CEP(CEP='67120938')
    assert isinstance(formatted_cep, str)

def test_returns_not_empty_string():
    formatted_cep = lookup.format_CEP(CEP='67120938')
    assert formatted_cep != ''

def test_remove_letters_from_input():
    formatted_cep = lookup.format_CEP(CEP='67120938A')
    assert formatted_cep == '67120938'

def test_remove_others_chars_from_input():
    chars = ['-', '_', '/', ',', '@', '&', '*', '(', ')',
             '#', '!', '?', '+', '=', '}', '{', ';', ':',
             '¨', '$', '"']
    for c in chars:
        formatted_cep = lookup.format_CEP(CEP='67120%s938' % c)
        assert formatted_cep == '67120938'
