def listarCursos(cursos):
    print("Cursos:")
    contador = 1
    for curso in cursos:
        datos = "{0}. Codigo: {1} | Nombre: {2} ({3} Creditos)"
        print(datos.format(contador, curso[0], curso[1], curso[2]))
        contador = contador + 1
    print("   ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input("Ingrese Codigo: ")
        if len(codigo) == 6:
            codigoCorrecto = True
        else:
            print("Codigo incorrecto debe tener 6 digitos")
    nombre = input("Ingrese Nombre: ")
    creditosCorrecto = False
    creditos = int(
        input("Ingrese creditos: ")
    )  # La validacion me tiraba un error loco asi que no lo valido
    curso = (codigo, nombre, creditos)
    return curso


def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese codigo del curso a eliminar")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break
    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese codigo del curso a editar")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break
    if existeCodigo:
        pass
    else:
        cursos=None
    return curso