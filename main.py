from Cryptology import SezarX

crypter = SezarX(key=22)

with open("chad.jpeg","rb") as f:
    encryptedData = crypter.encryptImage(f.read())

    with open("chad2.png","wb") as f:
        f.write(crypter.decryptImage(encryptedData))
    pass