#   Fechas(datetime)
import datetime

# from datetime import datetime

# fechaActual = datetime.now()
# print(fechaActual)
# fecha = datetime(2020, 11, 5)
# fecha = datetime(2020, 11, 5, 10, 35, 22)
# print(fecha)
# fechaActual2 = datetime.strftime(fechaActual, "%d/%m/%Y %H:%M:%S")
# fechaActual3 = datetime.strftime(fechaActual, "%B %d %Y %H:%M:%S")
# print(fechaActual3)
# fechaTexto = "Dec 06 2020 12:34:22"
# fechaActual4 = datetime.strptime(fechaTexto, "%b %d %Y %H:%M:%S")
# print(fechaActual4)
# dia = datetime.strftime(fechaActual, "%d")
# dia = int(datetime.strftime(fechaActual, "%d"))
# print(dia)
# horaActual = datetime.strftime(fechaActual, "%H:%M:%S")
# print(horaActual)
# fechaPasada = datetime(1980, 9, 1)
# diferencia = fechaActual - fechaPasada
# print(diferencia)
# print(diferencia.days)
# print(diferencia.total_seconds())
# dia_delta = datetime.timedelta(days=5)
# fechaInicial = datetime.date.today()
# print(fechaInicial)
# fechaFutura = fechaInicial + dia_delta
# print(fechaFutura)
fecha = datetime.datetime.now().isoformat()
print(fecha)
