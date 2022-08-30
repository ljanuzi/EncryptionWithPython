import json
from Crypto.Cipher import AES
import base64
from base64 import b64decode, b64encode


def getDataFromFile():
    f = open("encryptionParams.json","r")

    dataFromFile = json.load(f)

    return dataFromFile



encryptionParams = {
    
    "key" : getDataFromFile()["key"],
    "iv" : getDataFromFile()["iv"]
}

secretKey = base64.b64decode(bytes(encryptionParams["key"], 'utf-8'))
iv = base64.b64decode(bytes(encryptionParams["iv"], 'utf-8'))

def encryptMessage(message):

    #create an AES object
    encryptinObject = AES.new(secretKey, AES.MODE_CBC, iv)

    #def of func used to add padding to message
    PAD = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

    #encode the message
    encodedMessage = PAD(message).encode('utf-8')

    #encrypt the message
    encryptedMessage = encryptinObject.encrypt(encodedMessage)

    return b64encode(encryptedMessage).decode('utf-8')

def decryptMessage(message):
    
    #init
    message = base64.b64decode(message)
    #create an AES Object
    cipher = AES.new(secretKey, AES.MODE_CBC, iv)

    #def of func used to unpad message
    UNPAD= lambda s: s[:-ord(s[len(s)-1:])]

    #decrypt and return message
    return UNPAD(cipher.decrypt(message)).decode('utf-8')