import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, EAN13):
        """Para examinar si el código indicado es un eAn13"""
        # Si la longitud del código no es 13, entonces no es de tipo EAN13
        if len(EAN13) != 13:
            return False
        # Sumamos los números de las posiciones impares (menos la número 13)
        impares = 0
        for number in range(0, 5):
            impares += EAN13[2*number]
        # Lo mismo pero ahora con todos los de las pares
        pares = 0
        for number in range(0, 5):
            pares += EAN13[2*number + 1]
        # Sumamos los pares con los impares multiplicados por 3
        impares = impares*3
        suma = impares + pares
        # Ahora, cogemos esa suma y hallamos el resta de 10 menos
        # el resto de la división suma/10
        num = 10 - (suma % 10)
        # Si el dígito 13 del código no es igual al número calculado,
        # el código no cumple el estándar
        if num != EAN13[12]:
            return False
        return True

    def ReadproductcodefromJSON( self, fi ):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req