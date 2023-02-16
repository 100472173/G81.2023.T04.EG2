import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, EAN13):
        """Para examinar si el código indicado es del tipo eAn13"""
        # Si la longitud del código es distinta de 13 dígitos, no es de tipo EAN13
        if len(EAN13) != 13:
            return False
        # Primero sumamos los números de las posiciones impares (menos la número 13)
        impares = EAN13[0] + EAN13[2] + EAN13[4] + EAN13[6] + EAN13[8] + EAN13[10]
        # Lo mismo pero ahora con todos los de las pares
        pares = EAN13[1] + EAN13[3] + EAN13[5] + EAN13[7] + EAN13[9] + EAN13[11]
        # Multiplicamos el resultado de los impares por 3 y lo sumamos a los pares
        suma = impares*3 + pares
        # Ahora, tenemos que coger esa suma y hallar la resta del número múltiplo de 10 igual o superior a
        # dicho número menos ese número, es decir cuanto falta para llegar del número hasta el múltiplo
        resto = suma % 10
        num = 10 - resto
        # Si el dígito 13 del código no es igual al número calculado, el código no cumple el estándar
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