"""..."""
import json
from .order_management_exception import orderManagementException
from .order_request import orderRequest


class orderManager:
    """..."""
    def __init__(self):
        pass

    def validateEAN13(self, ean13: str) -> bool:
        """Este método devuelve (bool) si un string almacena un código EAN13"""
        # Si la longitud del código no es 13, entonces no es de tipo EAN13
        if len(ean13) != 13:
            return False
        # Sumamos los números de las posiciones pares (menos la número 13)
        pares = 0
        for number in range(0, 6):
            pares += int(ean13[2 * number])
        # Lo mismo pero ahora con todos los de las impares
        impares = 0
        for number in range(0, 6):
            impares += int(ean13[2 * number + 1])
        # Sumamos los pares con los impares multiplicados por 3 (ponderados)
        impares = impares * 3
        suma = pares + impares
        # Tenemos que comprobar que la diferencia del multiplo de 10 más
        # cercano a suma por arriba y suma sea igual que el ultimo digito
        # de ean13
        # Comprobemos el caso de que esa diferencia sea 0
        modulo = suma % 10
        if modulo == 0:
            return int(ean13[12]) == modulo
        # Veamos si es distinto de 0
        num = 10 - modulo
        if num != int(ean13[12]):
            return False
        return True

    def readProductCodeFromJSON(self, file):
        """..."""
        try:
            with open(file) as fil:
                data = json.load(fil)
        except FileNotFoundError as error:
            raise orderManagementException("Wrong file or "
                                           "file path") from error
        except json.JSONDecodeError as error:
            raise orderManagementException("JSON Decode Error - "
                                           "Wrong JSON Format") from error

        try:
            product = data["id"]
            phone_number = data["phoneNumber"]
            req = orderRequest(product, phone_number)
        except KeyError as error:
            raise orderManagementException("JSON Decode Error - "
                                           "Invalid JSON Key") from error
        if not self.validateEAN13(product):
            raise orderManagementException("Invalid product code")
        # Close the file
        return req
