#   Crear datos aleatorios
# faker
# pip install faker
from faker import Faker
from faker.providers import (
    bank,
    company,
    internet,
    person,
)  #   Estos son los provedores importados

#   Instancio el objeto
fake = Faker("es_AR")
fake.add_provider(
    bank
)  # Esto provee diferentes tipos de datos sobre diferentes tematicas fake
fake.add_provider(company)
fake.add_provider(internet)
fake.add_provider(person)

for n in range(10):
    #print(fake.name())  # me traigo nombres aleatorios(fake)
    #print(fake.address())  # Lo mismo pero para direcciones
    #print(fake.text())  # Lo mismo pero textos
    #print(fake.bban())  # numeros cuentas bancarias fake
    #print(fake.first_name())  #   Igual pero con nombres iniciales
    print(fake.email()) 
