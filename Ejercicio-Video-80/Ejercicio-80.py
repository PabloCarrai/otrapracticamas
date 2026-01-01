#   generar passwords y encriptarlos
# pip install werkzeug
import random
from werkzeug.security import generate_password_hash

minus = "abcdefghijklmnoparstuvwxyz"
mayus = minus.upper()
numeros = "0123456789"
simbolos = "!#$%&()*+,-./:;<=>?@[]^_{|}~¿¡"
base = minus + mayus + numeros + simbolos

longitud = 12
for _ in range(10):
    muestra = random.sample(base, longitud)
    password = "".join(muestra)
    password_encriptado = generate_password_hash(password)
    print(f"Pass: {password} Encriptado:  {password_encriptado}")
