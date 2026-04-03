def ordenar(x):
    return x[1]
def mayor(x):
    return x["puntaje_total"]

def armar_posicones(pos, rounds):
    posicion_puntaje = []
    #Almaceno el diccionario correspondiente segun la ronda jugada
    dic_round = rounds[pos]
    scores = dic_round['scores']
    #Recorro el diccionario scores almacenando el nombre de cada jugador
    for nombre in scores.keys():
        #Almaceno el diccionario de cada jugador
        puntaje = 0
        concursante = scores[nombre]
        for nota in concursante.values():
            #Sumo el puntaje de cada juez
            puntaje += nota
        posicion_puntaje.append((nombre,puntaje))
    #Utilzo sort para ordenar la lista de tuplas, teniendo como parametro que siempre elija el segundo valor
    posicion_puntaje.sort(reverse = True, key= ordenar)
    return posicion_puntaje
    

def armar_registro(nombre,puntaje,ganadas):
    tabla_final = {
                    "concursante" : nombre,
                    "puntaje_total" : puntaje,
                    "rondas_ganadas" : ganadas,
                    "mejor_puntaje" : puntaje
                    }
    return tabla_final


def sumar_resultado(regist,tabla):
    for conc in tabla:
        punt_verd = regist["mejor_puntaje"] if regist["mejor_puntaje"] > conc["mejor_puntaje"] else conc["mejor_puntaje"]
        if conc["concursante"] == regist["concursante"]:
            conc["puntaje_total"] += regist["puntaje_total"]
            conc["rondas_ganadas"] += regist["rondas_ganadas"]
            conc["mejor_puntaje"] = punt_verd
    return tabla



def calcular_prom(tabla_final,cantidad_rondas):
    for pos in range(len(tabla_final)):
        tabla_final[pos]["promedio_puntaje"] = tabla_final[pos]["puntaje_total"] / cantidad_rondas
    return tabla_final

def empezar_rondas(rounds):
    tabla_final = []
    ganadas = 0
    round_terminado = f""

    for posRonda in range(len(rounds)):
        round_terminado += f"Round Nro {posRonda + 1}  -  {rounds[posRonda]["theme"]}:\n"
        posiciones = armar_posicones(posRonda,rounds)
        #Recorro la lista recuperada de la funcion para determinar quien gano cada ronda
        for posConcursante in range(len(posiciones)):
            #Como la lista esta ordenada puedo directamente preguntar si el concursante es el primero, si es asi,  ya se que gano
            if posConcursante == 0:
                round_terminado += f"El ganador de la ronda es ¡{posiciones[posConcursante][0]}! puntaje:{posiciones[posConcursante][1]}\n"
            else:
                round_terminado += f"Posicion Nro {posConcursante+1}: {posiciones[posConcursante][0]} puntaje:{posiciones[posConcursante][1]}\n"

            if posRonda == 0:
                ganadas = 1 if posConcursante == 0 else 0
                registro = armar_registro(posiciones[posConcursante][0],posiciones[posConcursante][1],ganadas)
                tabla_final.append(registro)  
            else:
                ganadas = 1 if posConcursante == 0 else 0
                registro = armar_registro(posiciones[posConcursante][0],posiciones[posConcursante][1],ganadas)
                tabla_final = sumar_resultado(registro,tabla_final)
        round_terminado += f"\n"
        
                
    return round_terminado, tabla_final

def crear_tabla_final(result):
    tabla = "RESULTADO FINAL\n"
    tabla += (f"{'Cocinero':<15}"    
             f"{'Puntaje':<15}"      
             f"{'Rondas ganadas':<20}"     
             f"{'Mejor ronda':<20}"      
             f"{'Promedio':<15}\n")
    tabla += f"-" * 85
    tabla += f"\n" 
    result.sort(reverse = True, key = mayor)
    for i in range(len(result)):
        tabla += (f"{result[i]['concursante']:<15}"     
                  f"{result[i]['puntaje_total']:<15}"      
                  f"{result[i]['rondas_ganadas']:<20}"        
                  f"{result[i]['mejor_puntaje']:<20}"    
                  f"{result[i]['promedio_puntaje']:<15}\n")
    return tabla     

def resultado(rounds):
    rounds_terminados, result_final = empezar_rondas(rounds)
    print(rounds_terminados)

    result_final = calcular_prom(result_final,len(rounds))
    tabla_de_resultados = crear_tabla_final(result_final)
    print(tabla_de_resultados)
