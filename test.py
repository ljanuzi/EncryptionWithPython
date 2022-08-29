import Crypto
from Crypto.Cipher import AES
import base64
from base64 import b64decode, b64encode
from Crypto.Util.Padding import pad

# For Generating AES Cipher text
secret_key = base64.b64decode(bytes("6zun6x5L/ZzE9YIJYvHhd5ycaj+vuY+1ibTtyOyDNvs=", 'utf-8'))
iv = base64.b64decode(bytes("iqiHPDvT1i6cx2z6i/Y5Tg==", 'utf-8'))
obj = AES.new(secret_key, AES.MODE_CBC, iv)

message = '{"name":"Learta","lastName":"Januzi"}'
# print(message)
PAD = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
unpad= lambda s: s[:-ord(s[len(s)-1:])]
# print(PAD(message))
encoded_text = PAD(message).encode('utf-8')

encrypted_text = obj.encrypt(encoded_text)
# print(encrypted_text)



mesazhiRronitDitjonit = "Yr/Uhpe5oICaS055udpcK98y9qAbzicJnZ/2MzGvnrcCkxh6Id9bINcb5I1fZb8V"
mesazhiRronitDitjonit = base64.b64decode(bytes(mesazhiRronitDitjonit,'utf-8'))
ivd= mesazhiRronitDitjonit[:16]

dobj = AES.new(secret_key,AES.MODE_CBC, ivd)

decrypted_text = unpad(dobj.decrypt(mesazhiRronitDitjonit[16:])).decode('utf-8')

#decrypted_text = dobj.decrypt(mesazhiRronitDitjonit)
#decoded_text = base64.b64decode(bytes(decrypted_text,'utf-8'))