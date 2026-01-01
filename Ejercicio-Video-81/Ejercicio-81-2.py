from cryptography.fernet import Fernet

texto = "x?1_P-1M.4!eM"
key = Fernet.generate_key()  #   Genero llave en bytes
objeto_cifrado = Fernet(key)
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)

texto_desencriptado_byte = objeto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado_byte)
texto_desencriptado=texto_desencriptado_byte.decode()
print(texto_desencriptado)