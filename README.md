# CEP Lookup

CEP (Postal Addressing Code in Portuguese) is the Brazilian Postal Code system. Almost every public place or high-occupancy private spaces, like major commercial buildings and residential condos, are assigned by a CEP.

The standart format is based in a 8-digits code - 00000-000. The complete database is placed in [e-DNE](https://www.correios.com.br/english/correios-a-to-z/e-dne), but Correios (Brazilian Postal Service) provides a free Web Service to retrieve information about Brazilian CEP. This repository retrieves CEP information from there.



## Usage

```{python}
>>> from brazilian_cep_lookup import lookup
>>> cep_info = lookup.get_CEP(CEP='67120938')
>>> print(cep_info)
{
    'bairro': 'Quarenta Horas (Coqueiro)',
    'cep': '67120938',
    'cidade': 'Ananindeua',
    'complemento2': None,
    'end': 'Avenida Governador Hélio da Mota Gueiros 37',
    'uf': 'PA',
    'unidadesPostagem': []
}
```

## Contributors

None yet.
