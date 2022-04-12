import cryptocode
from passlib.hash import md5_crypt
from vadim import Point

pas = input()
password = input()
pas = md5_crypt.hash(pas)
print(pas)
login_encoded = cryptocode.encrypt(password, pas)
print(login_encoded)
## And then to decode it:
login_decoded = cryptocode.decrypt(login_encoded, pas)
print(login_decoded)


