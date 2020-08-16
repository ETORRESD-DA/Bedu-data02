numeros = [14, 186, '252', '60', 245, 216, '210', '768', '765', 180, '671', '228', 780, '1162', 30, '992', '374', '1458', 1615, 1700, 1995, 418, 1633, 48, 1950, 234, 864, '1596', 928, 2070, 2263, 2176, '2145', 1938, 700, 180, '2812', 1748, 2808, 2760, '1435', 2772, 2881, 88, '3960', 1380, '4183', '1536', 4312, '2450', '1326', '4212', 3339, '1296', 1980, 3920, 1311, '1044', '5015', 3840, 4575, '4464', 4473, '384', '2990', '5412', '134', 2992, '3657', 2940, '142', '2736', 2774, 1924, 3375, 3040, 3003, '6864', 4582, '1280', 7695, '2132', '5893', '1596', 5440, 4128, 870, 5456, 6942, 8820, '4186', 5244, 6417, '7896', '7980', 5184, 9215, 6664, 5346, 6700]

def multiplicar_por_9(numero):
    return numero * 9
def convertir_a_enteros(numero):
    return int(numero)
def convertir_true_pares(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
# Convertir strings a numeros
numeros_enteros = list(map(convertir_a_enteros, numeros))
# Multiplicar cada numero por 9
numeros_por_9 = list(map(multiplicar_por_9, numeros_enteros))
# Convertir pares a True
numeros_pares_true = list(map(convertir_true_pares, numeros_por_9))
print(numeros_pares_true)
print(numeros_enteros)