#https://github.com/MarkovIlya/Task_for_Infomation_Security_1
import cryptocode
from passlib.hash import md5_crypt
pas = input()
password = input()
pas = md5_crypt.hash(pas)
print(pas)
login_encoded = cryptocode.encrypt(password, pas)
print(login_encoded)
## And then to decode it:
login_decoded = cryptocode.decrypt(login_encoded, pas)
print(login_decoded)
