from random import randint, choice
from data_stark import *
from os import system


def mapear_lista(funcion, lista:list)->list:
    """_summary_

    Args:
        funcion (_type_): Funcion para mapear
        lista (list): Lista que se va a mapear

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste y con lo que especifiques en la funcion,
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno

def filtrar_lista(funcion, lista:list)->list:
    """_summary_

    Args:
        funcion (_type_): Funcion para filtrar
        lista (list): Lista que se va a filtrar

    Returns:
        list: Se creara una lista con los datos de la lista que ingresaste luego de ser filtrados en base a tu funcion
    """
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno

def for_each_lista(funcion, lista:list)->None:
    """_summary_

    Args:
        funcion (_type_): Funcion para cada elemento
        lista (list): Lista que se va a iterar/recorrer
    """
    for el in lista:
        funcion(el)

def mostrar_heroe(un_heroe:dict)->str:
    """_summary_

    Args:
        un_heroe (dict): Diccionario con los datos del heroe

    Raises:
        ValueError: No se habria ingresado un diccionario

    Returns:
        str: Retorna la lista con los datos del heroe
    """
    if isinstance(un_heroe,dict):
        print(f"Nombre: {un_heroe["nombre"]}\n Identidad: {un_heroe["identidad"]}\n Empresa: {un_heroe["empresa"]}\n Altura: {un_heroe["altura"]}\n Peso: {un_heroe["peso"]}\n Genero: {un_heroe["genero"]}\n Color de ojos: {un_heroe["color_ojos"]}\n Color de pelo: {un_heroe["color_pelo"]}\n Fuerza: {un_heroe["fuerza"]}\n Ingeligencia: {un_heroe["inteligencia"]}\n")
    else:
        raise ValueError("No se ingreso ningun diccionario")

def mostrar_dato(un_heroe:list)->str:
    """_summary_

    Args:
        un_heroe (list): Lista con los datos del heroe

    Raises:
        ValueError: No se habria ingresado un diccionario

    Returns:
        str: Printea los datos del heroe por linea
    """
    if isinstance(un_heroe,list):
        for el in un_heroe:
            print(el)
    else:
        raise ValueError("No se ingreso ningun diccionario")

def swap_lista(lista:list, valor1, valor2):
    """_summary_

    Args:
        lista (list): lista a swapear
        valor1 (_type_): primer valor a swapear
        valor2 (_type_): segundo valor a swapear
    """
    aux = lista[valor1]
    lista[valor1] = lista[valor2]
    lista[valor2] = aux

def ordenar_lista(criterio, lista)->None:
    """_summary_

    Args:
        criterio (_type_): criterio sobre como se debe ordenar
        lista (_type_): lista que se desea ordenar
    """
    for i in range(len(lista) - 1):
        for j in range(i + 1, len(lista)):
            if criterio(lista[i], lista[j]):
                swap_lista(lista, i, j)

def mostrar_heroe_fila(un_heroe: dict)->str:
    """_summary_

    Args:
        un_heroe (dict): lista de datos del heroe

    Returns:
        str: Los datos del heroe sobre una fila
    """
    print(f"{un_heroe["nombre"]} {un_heroe["identidad"]:<8} {un_heroe["empresa"]:<10} {un_heroe["altura"]} {un_heroe["peso"]:2} {un_heroe["genero"]:<18} {un_heroe["color_ojos"]:<12} {un_heroe["color_pelo"]:<12} {un_heroe["fuerza"]:<12} {un_heroe["inteligencia"]:<20}")

def mostrar_heroes(heroes:list)->None:
    """_summary_

    Args:
        heroes (list): Lista de superheroes

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(heroes,list):
        cant = len(heroes)
        print("                             ***Lista de Heroes***")
        print("  Nombre Identidad Empresa Altura Peso Genero ColorOjos ColorPelo Fuerza Ingeligencia")
        print("-----------------------------------------------------------------------------------------------------------------------")
        for i in range(cant):
            mostrar_heroe_fila(heroes[i])
        print()
    else:
        raise ValueError("Eso no es una lista")

def definir_campo(campo:str)->str:
    """_summary_

    Args:
        campo (str): Valores: n = nombre ; i = identidad ; e = empresa ; a = altura ; p = peso ; f = fuerza ; int = inteligencia; g = genero

    Raises:
        ValueError: No se ingreso un valor valido

    Returns:
        str: La palabra completa
    """
    match campo:
        case "n":
            retorno = "nombre"
        case "i":
            retorno = "identidad"
        case "e":
            retorno = "empresa"
        case "a":
            retorno = "altura"
        case "p":
            retorno = "peso"
        case "f":
            retorno = "fuerza"
        case "int":
            retorno = "inteligencia"
        case "g":
            retorno = "genero"
        case _: raise ValueError("No es un campo valido")
    return retorno

def ordenar_heroes(heroes:list, campo:str, asc:bool = True):
    """_summary_

    Args:
        heroes (list): Lista de heroes
        campo (str): Campo a ordenar
        asc (bool, optional): True = Ascendente, False = Descendente. Defaults to True.

    Raises:
        ValueError: No se habria ingresado ninguna lista
    """
    if isinstance(heroes,list):
        atributo = definir_campo(campo)
        tam = len(heroes)
        for i in range(tam - 1):
            for j in range(i + 1, tam):
                if heroes[i][atributo] > heroes[j][atributo] if asc else heroes[i][atributo] < heroes[j][atributo]:
                    swap_lista(heroes, i, j)  
    else:
        raise ValueError("No se ingreso ninguna lista") 

def altura_float(lista):
    """_summary_

    Args:
        lista (_type_): Lista de alturas para pasar a float
    """
    for i in lista:
        i["altura"] = float(i["altura"])

def peso_float(lista):
    """_summary_

    Args:
        lista (_type_): Lista de pesos a pasar a float
    """
    for i in lista:
        i["peso"] = float(i["peso"])

def no_inteligencia(lista):
    """_summary_

    Args:
        lista (_type_): Lista de pesos a pasar a float
    """
    for i in lista:
        if i["inteligencia"] == "":
            i["inteligencia"] = "no tiene"

def igualar_max(max, lista,campo):
    """_summary_

    Args:
        max (_type_): valor maximo
        lista (_type_): lista a iterar/recorrer
        campo (_type_): campo a igualar con el max

    Returns:
        _type_: el valor del campo igualado a max
    """
    for i in lista:
        if max == i[definir_campo(campo)]:
            return i["nombre"]

def nombre_campo_max(campo):
    """_summary_

    Args:
        campo (_type_): campo a buscar el nombre mayor

    Returns:
        _type_: el nombre de ese campo mayor
    """
    maximo = (calcular_mayor(mapear_lista(lambda hero:hero[definir_campo(campo)], lista_personajes)))
    return (igualar_max(maximo, lista_personajes,campo))

def nombre_campo_min(campo):
    """_summary_

    Args:
        campo (_type_): nombre de ese campomenor

    Returns:
        _type_: el nombre de ese campo menor
    """
    minimo = (calcular_menor(mapear_lista(lambda hero:hero[definir_campo(campo)], lista_personajes)))
    return (igualar_max(minimo, lista_personajes,campo))

def pausar():
    system("pause")

def limpiar_pantalla():
    system("cls")

def menu()->str:
    """_summary_

    Returns:
        str: Menu de stark
    """
    limpiar_pantalla()
    print("      Menu de Stark")
    print("1-Mostrar nombres")
    print("2-Mostrar nombres junto a su altura")
    print("3-Mostrar la altura maxima")
    print("4-Mostrar la altura minima")
    print("5-Mostrar el promedio de las alturas")
    print("6-Mostrar nombre del heroe mas alto")
    print("7-Mostrar nombre del heroe mas bajo")
    print("8-Mostrar nombre del heroe mas pesado")
    print("9-Mostrar nombre del heroe menos pesado")
    print("10-Nombre de heroees masculinos")
    print("11-Nombre de heroees femeninos")
    print("12-Altura max masculino")
    print("13-Altura max femenino")
    print("14-Altura min masculino")
    print("15-Altura min femenino")
    print("16-Altura promedio masculinos")
    print("17-Altura promedio femeninos")
    print("18-Nombre altura max masculino")
    print("19-Nombre altura max femenino")
    print("20-Nombre altura min masculino")
    print("21-Nombre altura min femenino")
    print("22-Cantidad colores de ojos")
    print("23-Cantidad colores de pelo")
    print("24-Cantidad clasificacion inteligencia")
    print("25-Listar todos los superhéroes agrupados por color de ojos.")
    print("26-Listar todos los superhéroes agrupados por color de pelo.")
    print("27-Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("28-Salir")
    return  input("Ingrese opcion: ")

def contador_lista(lista,campo):
    """_summary_

    Args:
        lista (_type_): lista a iterar/recorrer
        campo (_type_): campo que  se itera/recorre

    Returns:
        _type_: Diccionario con la cantidad de propietarios a cada uno
    """
    campo = {}
    for el in lista:
        campo[el] = 0
    
    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1
    
    return campo

def totalizar_lista(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a sumar

    Raises:
        ValueError: No se habria ingresado una lista

    Returns:
        int: Suma todos sus elementos
    """
    if isinstance(lista, list):
        total = 0
        for el in lista:
            total += el
        return total
    raise ValueError("Eso no es una lista")

def calcular_promedio(lista:list)->float:
    """_summary_

    Args:
        lista (list): lista a calcular promedio

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        float: El promedio del total de la lista
    """
    if isinstance(lista, list):
        cant = len(lista)
        if cant == 0:
            raise ValueError("No esta definido el promedio de una lista vacia")
        return totalizar_lista(lista) / cant
    raise ValueError("Eso no es una lista")

def calcular_mayor(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a calcular mayor

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        int: Devuelve el mayor numero de la lista
    """
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        mayor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] > mayor:
                mayor = lista[i]
        return mayor
    raise ValueError ("No es una lista")

def calcular_menor(lista:list)->int:
    """_summary_

    Args:
        lista (list): lista a calcular mayor

    Raises:
        ValueError: La lista habria estado vacia
        ValueError: No se habria ingresado una lista

    Returns:
        int: Devuelve el mayor numero de la lista
    """
    if isinstance(lista,list):
        if len(lista) == 0:
            raise ValueError("La lista esta vacia")
        menor = lista[0]
        for i in range(1, len(lista)):
            if lista[i] < menor:
                menor = lista[i]
        return menor
    raise ValueError ("No es una lista")

def enlistar(lista:list, campo1, campo_agrupar):
    """_summary_

    Args:
        lista (list): lista a iterar/recorrer
        campo1 (_type_): campo dato principal
        campo_agrupar (_type_): campo a clasificar

    Returns:
        _type_: diccionario con los clasificados en sus lugares
    """
    campo = {}
    for el in mapear_lista(lambda hero:hero[campo1], lista):
        campo[el] = ""
    for i in lista:   
        for j in campo.keys():
            if i[campo1] == j:
                campo[j] += f" {i[campo_agrupar]},"
    
    return campo