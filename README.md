## Installation

``` 
git clone https://github.com/sTahaDev/Cryptology.git
```
> 'git' should already be downloaded

## Usage

```
#Import SezarX Algorithm
from Cryptology import SezarX

#Create New Algorithm with Your Secret Key
crypter = SezarX(key=22)

#Your Important Data
data = "This is important message"

#Encrypt and Decrypt data
encryptedData = crypter.encrypt(data)
decryptedData = crypter.decrypt(encryptedData)

print("Decrypted Data: " + decryptedData)
print("Encrypted Data: " + encryptedData)
```
