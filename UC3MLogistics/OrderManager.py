import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, EAN13):
        """Para examinar si el código indicado cumple las pautas necesarias para que sea del tipo eAn13"""
        # Si la longitud del código es distinta de 13 dígitos, no es de tipo EAN13
        if len(EAN13) != 13:
            return False
        # Los numeros en posiciones impares de los 13 digitos estan ponderados con un 3.
        # Para comprobar si el codigo es adecuado primero tenemos que realizar la suma de todos los digitos
        # multiplicándolos además por 3 los que están ponderados
        impares = EAN13[0] + EAN13[2] + EAN13[4] + EAN13[6] + EAN13[8] + EAN13[10]
        pares = EAN13[1] + EAN13[3] + EAN13[5] + EAN13[7] + EAN13[9] + EAN13[11]
        suma = impares*3 + pares
        # Ahora, tenemos que coger esa suma y hallar la resta del numero múltiplo de 10 igual o superior a
        # dicho número menos ese número, es decir cuanto falta para llegar del número hasta el múltiplo
        resto = suma % 10
        num = 10 - resto
        # Si el digito 13 del dódigo no es igual al número calculado, el código no cumple el estándar
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