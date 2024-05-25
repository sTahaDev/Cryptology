import base64

class SezarX:
    #Data Should Be Short Like "2000" character

    def __init__(self,key) -> None:
        self.key = key
        pass

    def encrypt(self,data):
        dataIDs = []
        encryptedData = ""
        

        for i in data:
            dataIDs.append(ord(i))
            pass

        for index,item in enumerate(dataIDs):
            encryptedData += chr(item + self.key)
            pass

        return encryptedData

    def decrypt(self,data):
        dataIDs = []
        decryptedData = ""

        for index,item in enumerate(data):
            id = ord(item)
            dataIDs.append(id - self.key)
            
            pass

        for i in dataIDs:
            decryptedData += chr(i)

        return decryptedData
        pass

    def encryptImage(self,path):
        encryptedData = ""

        with open(path,"rb") as f:
            byteFormat = base64.b64encode(f.read())
            encryptedData = self.encrypt(byteFormat.decode())

        return encryptedData
        pass

    def decryptImage(self,fileName,data):
           
        with open(fileName,"wb") as f:
            decryptedData = self.decrypt(data)
            decryptedData = base64.b64decode(decryptedData)
            f.write(decryptedData)
            
        pass

