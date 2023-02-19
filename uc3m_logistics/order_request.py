import json
from datetime import datetime


class orderRequest:
    def __init__(self, idcode, phone_number):
        self.__phone_number = phone_number
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        return self.__phone_number
    @phone.setter
    def phone(self, value):
        self.__phone_number = value

    @property
    def product_code(self):
        return self.__idcode
    @product_code.setter
    def product_code(self, value):
        self.__idcode = value
