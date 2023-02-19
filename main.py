from uc3m_logistics import orderManager
import string
from barcode import EAN13
from barcode.writer import ImageWriter

#GLOBAL VARIABLES
letters = string.ascii_letters + string.punctuation + string.digits
shift = 3

# Cambios
def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) + shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (letters.index(letter) - shift) % len(letters)
            encoded = encoded + letters[x]
    return encoded

def main():
    mng = orderManager()
    res = mng.readProductCodeFromJSON("test.json")
    strRes = res.__str__()
    print(strRes)
    EncodeRes = Encode(strRes)
    print("Encoded Res "+ EncodeRes)
    DecodeRes = Decode(EncodeRes)
    print("Decoded Res: " + DecodeRes)
    print("Codew: " + res.product_code)
    with open("./barcodeEan13.jpg", 'wb') as f:
        iw = ImageWriter()
        EAN13(res.product_code, writer=iw).write(f)


if __name__ == "__main__":
    main()
