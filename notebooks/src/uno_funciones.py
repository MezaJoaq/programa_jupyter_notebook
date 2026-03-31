def cant_lines(text):
#Utilizo el metodo split visto en clase, pero agregando como parametro "."
    lineas = text.split(".")
    return len(lineas)

def cant_palabras(text):
    palabras = text.split()
    return len(palabras)

def promedio_palabras_linea(text):
    prom = cant_palabras(text) / cant_lines(text)
    return prom

def lineas_encima_promedio(text):
    prom = promedio_palabras_linea(text)
    lineas_total = "Las lineas cuyas cantidad de palabras esta por encima del promedio son:"
    lineas = text.split(".")
    for i in range(cant_lines(text)):
        linea_act = lineas[i]
        if cant_palabras(linea_act) > prom: 
            lineas_total += f"{linea_act} ({cant_palabras(linea_act)})\n"

    return lineas_total
