import time
import random

# Función para medir el tiempo
def measure_time(function, *args):
    inicio = time.perf_counter()
    result = function(*args)
    fin = time.perf_counter()
    return result, fin - inicio

# --- Algoritmos de Ordenamiento ---

#Bubble Sort.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Indicador para optimizar el proceso si la lista ya está ordenada
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Si no hubo intercambio, se finaliza el algoritmo
            break
    return arr
#Complejidad: O(n2) en el peor de los casos, adecuado para conjuntos de datos pequeños


#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Desplaza los elementos mayores que 'key' hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
#Complejidad: O(n2) en el peor de los casos, pero buen rendimiento en listas pequeñas


#Quick Sort.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    # Seleccionamos el elemento pivote: la mitad del arreglo.
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    # Se aplica recursivamente el algoritmo a cada partición
    return quick_sort(left) + middle + quick_sort(right)
#Complejidad O(n log n), muy eficiente para grandes volúmenes de datos

# --- Algoritmos de Búsqueda ---

#búsqueda lineal.
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index  # Retorna el índice cuando encuentra el elemento
    return -1  # Retorna -1 si el elemento no se encuentra
#Complejidad: O(n), en el peor de los casos recorre todo el arreglo


#búsqueda binaria (requiere que el arreglo esté ordenado).
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
#Complejidad: O(log n), muy eficiente para grandes colecciones de datos


# --- Generación de Datos, Ejecución y Medición ---

if __name__ == '__main__':
    # Generación de una lista aleatoria de números sin repeticiones
    size = 10000
    datos = random.sample(range(1, 100000), size)
    
    # Listas para aplicar los diferentes ordenamientos
    datos_bubble = list(datos)
    datos_insertion = list(datos)
    datos_quick = list(datos)
    
    # Ejecución de los algoritmos
    sorted_bubble, time_bubble = measure_time(bubble_sort, datos_bubble)
    sorted_insertion, time_insertion = measure_time(insertion_sort, datos_insertion)
    sorted_quick, time_quick = measure_time(quick_sort, datos_quick)
    
    print("=== Resultados de Ordenamiento ===")
    print(f"Bubble Sort:    {time_bubble:.6f} segundos")
    print(f"Insertion Sort: {time_insertion:.6f} segundos")
    print(f"Quick Sort:     {time_quick:.6f} segundos")
    
    # Selección de un elemento objetivo para la búsqueda
    target = sorted_quick[size // 2]
    
    # Ejecución y tiempo de la búsqueda en el arreglo 
    index_linear, time_linear = measure_time(linear_search, sorted_quick, target)
    index_binary, time_binary = measure_time(binary_search, sorted_quick, target)
    
    print("=== Resultados de Búsqueda ===")
    print(f"Elemento buscado: {target}")
    print(f"Búsqueda Lineal -> Índice: {index_linear}, Tiempo: {time_linear:.6f} segundos")
    print(f"Búsqueda Binaria -> Índice: {index_binary}, Tiempo: {time_binary:.6f} segundos")