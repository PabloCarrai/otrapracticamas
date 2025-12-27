#   Trabajar con variables de entorno
#   pip install python-dotenv python-decouple
from decouple import config

print(config("MYSQL_HOST"))
print(config("MYSQL_USER"))
print(config("MYSQL_PASSWORD"))
print(config("MYSQL_DB"))
