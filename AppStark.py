from funciones_heroes import *
from data_stark import *
altura_float(lista_personajes)
peso_float(lista_personajes)
no_inteligencia(lista_personajes)

while True:
    match menu():
        case"1":
            limpiar_pantalla()
            print("Nombres de heroes:")
            mostrar_dato(mapear_lista(lambda hero: hero["nombre"], lista_personajes))
        case"2":
            limpiar_pantalla()
            print("Nombres de heroes y su altura:")
            mostrar_dato(mapear_lista(lambda hero: (hero["nombre"],hero["altura"]), lista_personajes))
        case"3":
            limpiar_pantalla()
            print(f"La altura mas alta es: {calcular_mayor(mapear_lista(lambda hero: hero["altura"], lista_personajes))}")
        case"4":
            limpiar_pantalla()
            print(f"La altura mas baja es: {calcular_menor(mapear_lista(lambda hero: hero["altura"], lista_personajes))}")
        case"5":
            limpiar_pantalla()
            print(f"El promedio de las alturas es: {calcular_promedio(mapear_lista(lambda hero: hero["altura"], lista_personajes))}")
        case"6":
            limpiar_pantalla()
            print(f"El heroe mas alto es: {nombre_campo_max("a")}")
        case"7":
            limpiar_pantalla()
            print(f"El heroe mas bajo es: {nombre_campo_min("a")}")
        case"8":
            limpiar_pantalla()
            print(f"El heroe mas pesado es: {nombre_campo_max("p")}")
        case"9":
            limpiar_pantalla()
            print(f"El heroe menos pesado es: {nombre_campo_min("p")}")
        case"10":
            limpiar_pantalla()
            mostrar_dato(mapear_lista(lambda nombre: nombre["nombre"],filtrar_lista(lambda hero: hero["genero"] == "M", lista_personajes)))
        case"11":
            limpiar_pantalla()
            mostrar_dato(mapear_lista(lambda nombre: nombre["nombre"],filtrar_lista(lambda hero: hero["genero"] == "F", lista_personajes)))
        case"12":
            limpiar_pantalla()
            print(calcular_mayor(mapear_lista(lambda hero: hero["altura"], filtrar_lista(lambda gen:gen["genero"] == "M",lista_personajes))))
        case"13":
            limpiar_pantalla()
            print(calcular_mayor(mapear_lista(lambda hero: hero["altura"], filtrar_lista(lambda gen:gen["genero"] == "F",lista_personajes))))
        case"14":
            limpiar_pantalla()
            print(calcular_menor(mapear_lista(lambda hero: hero["altura"], filtrar_lista(lambda gen:gen["genero"] == "M",lista_personajes))))
        case"15":
            limpiar_pantalla()
            print(calcular_menor(mapear_lista(lambda hero: hero["altura"], filtrar_lista(lambda gen:gen["genero"] == "F",lista_personajes))))
        case"16":
            limpiar_pantalla()
            print(calcular_promedio(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "M", lista_personajes))))
        case"17":
            limpiar_pantalla()
            print(calcular_promedio(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "F", lista_personajes))))
        case"18":
            limpiar_pantalla()
            print(igualar_max(calcular_mayor(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "M", lista_personajes))),lista_personajes,"a"))
        case"19":
            limpiar_pantalla()
            print(igualar_max(calcular_mayor(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "F", lista_personajes))),lista_personajes,"a"))
        case"20":
            print(igualar_max(calcular_menor(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "M", lista_personajes))),lista_personajes,"a"))
        case"21":
            limpiar_pantalla()
            print(igualar_max(calcular_menor(mapear_lista(lambda alt: alt["altura"], filtrar_lista(lambda hero: hero["genero"] == "F", lista_personajes))),lista_personajes,"a"))
        case"22":
            limpiar_pantalla()
            print(contador_lista(mapear_lista(lambda hero: hero["color_ojos"], lista_personajes), "color_ojos"))
        case"23":
            limpiar_pantalla()
            print(contador_lista(mapear_lista(lambda hero: hero["color_pelo"], lista_personajes), "color_pelo"))
        case"24":
            limpiar_pantalla()
            print(contador_lista(mapear_lista(lambda hero: hero["inteligencia"], lista_personajes), "inteligencia"))
        case"25":
            limpiar_pantalla()
            print(enlistar(lista_personajes, "color_ojos", "nombre"))
        case"26":
            limpiar_pantalla()
            print(enlistar(lista_personajes, "color_pelo", "nombre"))
        case"27":
            limpiar_pantalla()
            print(enlistar(lista_personajes, "inteligencia", "nombre"))
        case"28":
            limpiar_pantalla()
            print("Nos vemos!")
            break
        case _:
            limpiar_pantalla()
            print("Ingrese un numero entre las opciones")
    pausar()
    limpiar_pantalla()
print("Fin del programa")


