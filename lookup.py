import re
import zeep


WSDL_URL = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

def format_CEP(CEP: str) -> str:
    """Remove invalid characters from CEP.
    Args:
        CEP (str): The CEP string to format.

    Returns:
        str: The formated CEP.
    """
    CEP = re.sub(r'[^0-9]', '', CEP)
    return CEP

def validate_CEP(CEP: str) -> bool:
    """Validade CEP.
    Args:
        CEP (str): The CEP string to validate.

    Returns:
        bool: If True, CEP is valid. Otherwise, false.
    """
    pattern = re.compile('^[0-9]{8}$', re.I)
    match = pattern.match(str(CEP))

    return bool(match)

def get_CEP(CEP: str) -> dict:
    """Retrieves CEP information from Correios WSDL service - consultaCEP.
    Args:
        CEP (str): The CEP string to retrieve.

    Returns:
        dict: The dict contains CEP information.
    """
    client = zeep.Client(WSDL_URL)
    cep_information = client.service.consultaCEP(CEP)
    return cep_information
