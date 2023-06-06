import pandas as pd 
import numpy as np 

#************************** CREACION DE DATAFRAME *************************
# Ruta al archivo
archivo = 'informacion layout corbiz CM.xlsx'
# DF Usuarios-Almacén Corbiz
df_usu_alm = pd.read_excel(archivo, sheet_name='USUARIOS Y ALMACEN CORBIZ')
# DF Empresarios
df_empresarios = pd.read_excel(archivo, sheet_name='EMPRESARIOS')
# DF Productos
df_productos = pd.read_excel(archivo, sheet_name='PRODUCTOS')
# Tipo de Pago 
df_tipo_pago = pd.read_excel(archivo, sheet_name='TIPO DE PAGO')

#************************** SELECCION DE eO *************************
def genera_pedido():
    # Selecciona aleatoriamente 1 fila de la columna Empresario
    eO = df_empresarios['Empresario'].sample(n=1)
    # ingresar eO manualmente:
    # eO = df_empresarios[df_empresarios['Empresario'] == '0000000CGM']['Empresario']

    #************************** Obtener descuento *************************
    descuento = df_empresarios[df_empresarios['Empresario'] == eO.values[0]]['DesctoPed'].values[0]

    #************************** Obtener almacén *************************
    almacen = df_usu_alm['CEDIS'].sample(n=1)

    #************************** Obtener Cajero *************************
    # Obtiene el valor de la izquierda del almacen seleccionado
    cajero = df_usu_alm[df_usu_alm['CEDIS'] == almacen.values[0]]['CAJERO'].values[0]

    #************************** Obtener país *************************
    pais = 'MEX'
    #************************** Obtener periodo *************************
    periodo = 202306

    # Generar un DF que agregue aleatorioamente de 5 a 15 códigos de productos, seguido de la cantidad, y en la primera columna, ingresar en cada fila el valor "d"
    df_pedidos = pd.DataFrame(columns=['Detail', 'CODIGO', 'CANTIDAD'])

    #************************** Obtener lista de productos *************************
    for i in range(np.random.randint(5, 16)):
        df_pedidos.loc[i] = ['d', df_productos['CODIGO'].sample(n=1).values[0], np.random.randint(1, 17)]

    # Eliminar duplicados de la columna CODIGO
    df_pedidos = df_pedidos.drop_duplicates(subset=['CODIGO'])

    #************************** Obtener tipo de pago *************************
    tipo_pago = df_tipo_pago['Clave tipo'].sample(n=1).values[0]

    #************************** Cálculo con descuentos *************************
    # si el descuento es 0.4, obtener el valor de la columna -40% del DT df_productos de cada CODIGO del DF df_pedidos
    if descuento == 0.4:
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-40%'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-40%'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)

    # si el descuento es 0.35, obtener el valor de la columna -35% del DT df_productos de cada CODIGO del DF df_pedidos
    elif descuento == 0.35:
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-35%'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-35%'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)

    # si el descuento es 0.3, obtener el valor de la columna -30% del DT df_productos de cada CODIGO del DF df_pedidos
    elif descuento == 0.3:
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-30%'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-30%'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)

    # si el descuento es 0.25, obtener el valor de la columna -25% del DT df_productos de cada CODIGO del DF df_pedidos
    elif descuento == 0.25:
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-25%'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-25%'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)

    # si el descuento es 0.2, obtener el valor de la columna -20% del DT df_productos de cada CODIGO del DF df_pedidos
    elif descuento == 0.2:
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-20%'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['-20%'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)

    # si el descuento es CA, obtener el valor de la columna PRECIO SUGERIDO del DT df_productos de cada CODIGO del DF df_pedidos
    elif descuento == 'CA':
        df_pedidos['Precio unitario'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['PRECIO SUGERIDO'].values[0]).round(2)
        df_pedidos['Subtotal'] = df_pedidos['CODIGO'].apply(lambda x: df_productos[df_productos['CODIGO'] == x]['PRECIO SUGERIDO'].values[0])
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].astype(float)
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'] * df_pedidos['CANTIDAD']
        df_pedidos['Subtotal'] = df_pedidos['Subtotal'].round(2)


    # Del DF df_pedidos, obtener el valor de la columna PRECIO SUGERIDO y sumarla para obtener el total
    import math

    total = math.ceil(df_pedidos.iloc[:, 4].sum()) # ceil redondea hacia arriba

    # Crear el DF header
    df_header = pd.DataFrame(
        {
            'col1': 'h',
            'col2': eO.values[0],
            'col3': almacen,
            'col4': cajero,
            'col5': pais,
            'col6': periodo,
        }
    )

    # Crea el DF pay
    df_pay = pd.DataFrame({'col1':['p'], 'col2': tipo_pago, 'col3': total})

    # crea DF pedido_2
    df_pedidos_2 = df_pedidos[['Detail', 'CODIGO', 'CANTIDAD']]
    # Renombrar las columnas
    df_pedidos_2.columns = ['col1', 'col2', 'col3']
    # Agregar columnas vacias al DF pay
    df_pay[['col4', 'col5', 'col6']] = ""

    # Concatenar los DFs
    df_final = pd.concat([df_header, df_pedidos_2, df_pay], axis=0, ignore_index=True)
    # Sustituir los valores NaN por ''
    df_final = df_final.loc[:, 'col1':'col6'].fillna('')

    return df_final


df_final = None  # Variable auxiliar para almacenar el DataFrame final

# Generador de pedidos
for i in range(1, 51):
    df = genera_pedido()
    if df_final is None:
        df_final = df
    else:
        df_final = pd.concat([df_final, df], axis=0, ignore_index=True)

# Exportar el DataFrame final a un archivo CSV
df_final.to_csv('pedidos_generados_5000.csv', index=False, header=False)



    




