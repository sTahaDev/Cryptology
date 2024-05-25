from Cryptology import SezarX
import base64

crypter = SezarX(key=22)

data = "merhaba"

encryptedData = crypter.encrypt(data)
print(encryptedData)

decryptedData = crypter.decrypt(encryptedData)
print(decryptedData)
