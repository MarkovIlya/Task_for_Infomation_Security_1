#
import cryptocode
from passlib.hash import md5_crypt
pas = md5_crypt.hash("password")
print(pas)
login_encoded = cryptocode.encrypt("B0$$_of_ADm1nS", pas)
## And then to decode it:
login_decoded = cryptocode.decrypt(login_encoded, pas)
print(login_decoded)
