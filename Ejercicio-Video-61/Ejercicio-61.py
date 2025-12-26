#   json
import json

# json_str = '{"Nombre":"Oscar","edad":29,"pais":"mexico"}'  # json
# print(json_str)
# print(type(json_str))
# python_dict = json.loads(json_str)    #Genero un json a partir de un string
# print(python_dict)
# print(type(python_dict))
# print(python_dict["edad"])
# print(python_dict["pais"])

# data = {
#     "youtuber": "Marlinga",
#     "nombre": "Portinga",
#     "edad": 23,
#     "cursos": ["PHP", "Python", "JavaScript", "C", "Node.js"],
# }
# json_data = json.dumps(data)  #   Obtengo un json a partir de un diccionario real
# print(json_data)
# print(type(json_data))

# json_data = json.dumps(data, indent=4, separators=(", ", " : "), sort_keys=True)
# print(json_data)

# json_data = json.JSONEncoder().encode({"lenguajes": ["Python", "JavaScript"]})
# print(json_data)
# print(type(json_data))
# python_dic=json.JSONDecoder().decode(json_data)
# print(python_dic)
# print(type(python_dic))


class Curso:
    def __init__(self, codigo, nombre, creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos


curso_1 = Curso("9841", "Lenguaje", 4)
print(curso_1)
json_object_data = json.dumps(curso_1.__dict__)
print(json_object_data)

python_dict = json.loads(json_object_data)
print(python_dict)
