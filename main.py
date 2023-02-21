"""..."""
import string
from barcode import EAN13
from barcode.writer import ImageWriter
from uc3m_logistics import orderManager


# GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3

# Cambios


def encode(word):
    """..."""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            caracter = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[caracter]
    return encoded


def decode(word):
    """..."""
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            caracter = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[caracter]
    return encoded


def main():
    """..."""
    mng = orderManager()
    res = mng.readProductCodeFromJSON("test.json")
    str_res = str(res)
    print(str_res)
    encode_res = encode(str_res)
    print("Encoded Res " + encode_res)
    decode_res = decode(encode_res)
    print("Decoded Res: " + decode_res)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as comodin:
        image_writer = ImageWriter()
        EAN13(res.product_code, writer=image_writer).write(comodin)


if __name__ == "__main__":
    main()
