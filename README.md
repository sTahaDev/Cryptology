## Installation

``` 
git clone https://github.com/sTahaDev/Cryptology/tree/master
```

## Usage

```
from Cryptology import SezarX

crypter = SezarX(key=22)

data = "This is important message"

encryptedData = crypter.encrypt(data)
decryptedData = crypter.decrypt(encryptedData)

print("Decrypted Data: " + decryptedData)
print("Encrypted Data: " + encryptedData)
```
