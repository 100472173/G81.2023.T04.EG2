import json
from .order_management_exception import orderManagementException
from .order_request import orderRequest

class orderManager:
    def __init__(self):
        pass

    def validateEAN13(self, ean13):
        """Para examinar si el código indicado es un eAn13"""
        # Si la longitud del código no es 13, entonces no es de tipo EAN13
        if len(ean13) != 13:
            return False
        # Sumamos los números de las posiciones impares (menos la número 13)
        impares = 0
        for number in range(0, 5):
            impares += ean13[2 * number]
        # Lo mismo pero ahora con todos los de las pares
        pares = 0
        for number in range(0, 5):
            pares += ean13[2 * number + 1]
        # Sumamos los pares con los impares multiplicados por 3
        impares = impares*3
        suma = impares + pares
        # Ahora, cogemos esa suma y hallamos el resta de 10 menos
        # el resto de la división suma/10
        num = 10 - (suma % 10)
        # Si el dígito 13 del código no es igual al número calculado,
        # el código no cumple el estándar
        if num != ean13[12]:
            return False
        return True

    def readProductCodeFromJSON(self, file):

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
