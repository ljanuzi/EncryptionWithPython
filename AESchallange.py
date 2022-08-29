from Crypto.Cipher import AES
import base64
from base64 import b64decode, b64encode

encryptionParams = {
    "key" : "6zun6x5L/ZzE9YIJYvHhd5ycaj+vuY+1ibTtyOyDNvs=",
    "iv" : "iqiHPDvT1i6cx2z6i/Y5Tg=="
}
 
secretKey = base64.b64decode(bytes(encryptionParams["key"], 'utf-8'))
iv = base64.b64decode(bytes(encryptionParams["iv"], 'utf-8'))

def encryptMessage(message):

    #create an AES object
    encryptinObject = AES.new(secretKey, AES.MODE_CBC, iv)

    #add padding to message
    PAD = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    #encode the message
    encodedMessage = PAD(message).encode('utf-8')

    #encrypt the message
    encryptedMessage = encryptinObject.encrypt(encodedMessage)

    return b64encode(encryptedMessage).decode('utf-8')

def decryptMessage(message):

    #create an AES object
    encryptinObject = AES.new(secretKey, AES.MODE_CBC, iv)

print(encryptMessage('{"name":"Learta","lastName":"Januzi"}'))