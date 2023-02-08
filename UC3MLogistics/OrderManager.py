import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest

class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13( self, eAn13 ):
        # PLEASE INCLUDE HERE THE CODE FOR VALIDATING THE GUID
        # RETURN TRUE IF THE GUID IS RIGHT, OR FALSE IN OTHER CASE
        if len(eAn13) > 13:
            return False
        pais = eAn13[0:1]
        if pais != 84:
            return False
        impares = eAn13[0] + eAn13[2] + eAn13[4] + eAn13[6] + eAn13[8] + eAn13[10]
        pares = eAn13[1] + eAn13[3] + eAn13[5] + eAn13[7] + eAn13[9] + eAn13[11]
        suma = impares*3 + pares
        i = 0
        while i > suma:
            i += 10
        num = i - suma
        if num != eAn13[12]:
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