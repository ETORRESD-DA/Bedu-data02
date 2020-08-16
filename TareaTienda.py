
#El dueño de la tienda en linea pozole mio, necesita saber cuantos de sus productos son acredores 
# a paquetes de envió de $90 o $150.Los productos con precio con IVA que rebasen los $150 deberán 
# ocupar el paquete de envió de $90. Por lo contrario usaran el paquete de $150.


precios_sin_iva=[3, 148, 74, 71, 4, 83, 95, 20, 61, 10, 69, 67, 23, 164, 97, 67, 144, 200, 38, 90, 200, 162, 6, 180, 65, 71, 90, 182, 16, 132, 182, 108, 90, 196, 48, 2, 158, 88, 39, 39, 54, 80, 89, 3, 90, 170, 88, 71, 142, 45, 81, 194, 36, 39, 30, 33, 38, 44, 134, 43, 12, 52, 170, 162, 192, 83, 18, 176, 120, 28, 86, 188, 51, 11, 96, 13, 198, 34, 66, 23, 200, 62, 194, 91, 51, 26, 152, 186, 86, 38, 46, 66, 83, 66, 40, 2, 20, 12, 91, 53]

def precio_con_iva(precio):
    return round(precio*1.16,2)

def costo_de_envio(precio):
    if precio>150:
        return 90
    else:
        return 150    

precios_con_iva=list(map(precio_con_iva,precios_sin_iva))
costos_envio=list(map(costo_de_envio,precios_con_iva))
num_costos_envio_90=len(list(filter(lambda x: x == 90,costos_envio)))
num_costos_envio_150=len(list(filter(lambda x: x == 150,costos_envio)))

print(f'Numero de articulos con costo de envio 90: {num_costos_envio_90} y Numero de articulos concosto 150:  {num_costos_envio_150}')