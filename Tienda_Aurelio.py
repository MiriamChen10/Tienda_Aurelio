
#-*- coding: utf-8 -*-


def mostrar_menu():
    print("Bienvenidos a la Tienda Aurelio")
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Tema, problema y solución")
    print("2. Dataset de referencia. Resumen de fuente y definición")
    print("3. Estructura por table. Descripción y ejemplos")
    print("4. Escalas de medición")
    print("5. Sugerencias y mejoras con Copilot")
    print("6. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-6): ")

    if opcion == 1:
        print("\nTEMA: Este proyecto simula la gestión de “Tienda Aurelio”, una tienda minorista, utilizando datos sintéticos.")
        print("PROBLEMA: La falta de integración y acceso a datos provenientes de múltiples bases de datos impide tener una visión clara del negocio y su rentabilidad. Esta situación también obstaculiza el análisis, la visualización y el modelado efectivo de la información.\n ")
        print("SOLUCIÓN: El objetivo principal es analizar estas bases de datos. Para ello, se procederá a analizar cada una, identificando sus entidades, atributos, tipos de datos, escalas de medición y las relaciones entre ellas. El resultado será un escenario de datos consistente que permita:")
        print("\t -	Analizar datos: Identificar el inventario de productos, determinar el volumen de ventas en períodos específicos, comprender la frecuencia de compra de los clientes, analizar la tasa de clientes perdidos, descubrir patrones de compra, entre otras. ")
        print("\t -	Visualizar datos: Crear un dashboard que muestre el crecimiento de la tienda en función de las ventas, los productos y el comportamiento de los clientes.")
        print("\t -	Modelar datos: Aplicar algoritmos para predecir comportamientos futuros, como la demanda de productos o la tendencia de ventas.\n")
    
    elif opcion == 2:
        print("\nFUENTE: Los datos fueron generados con fines educativos. Las bases de datos se crearon para el aprendizaje de análisis, visualización y modelado de datos. Asimismo, presentan poca o nula consistencia, así como datos faltantes o nulos, por lo que, para fines prácticos, se asemejan a los datos de un negocio real.")
        print("\nDEFINICIÓN: La base de datos estructurada en formato Excel representa de manera integral a la “Tienda Aurelio”, e incluye el catálogo de productos, el registro de clientes y las operaciones de venta.")
        print("\t -	Productos (productos.csv): Inventario o catálogo de artículos disponibles.")
        print("\t -	Clientes (clientes.csv): Registro de la cartera de clientes.")
        print("\t -	Ventas (ventas.csv): Registro de las transacciones realizadas.")
        print("\t -	Detalle de Ventas (detalle_ventas.csv): Desglose de los productos incluidos en cada venta. Es decir, detalla los productos vendidos en cada transacción.\n")

        
    elif opcion == 3:
        
        print("\nESTRUCTURA POR TABLA: A continuación se detalla la estructura de cada tabla, incluyendo: el nombre, el archivo del dataset, la cantidad de filas, los campos, sus tipos de dato y las escalas de medición.")
       
        print("Productos (productos.csv) — ~100 filas")
        print("| Campo".ljust(20)+ "|Tipo".ljust(20)+ "|Escala".ljust(20)+"|".ljust(20))
        print("| ".ljust(20)+ "|".ljust(20)+ "|".ljust(20)+"|".ljust(20))
        print("| id_producto".ljust(20)+ "| int".ljust(20)+"| Nominal".ljust(20)+"|".ljust(20))
        print("| nombre_producto".ljust(20)+ "| str".ljust(20)+"| Nominal".ljust(20)+ "|".ljust(20))
        print("| categoria".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| precio_unitario".ljust(20)+ "| float".ljust(20)+ "| Razon".ljust(20)+ "|".ljust(20)+"\n")

        print("Clientes (clientes.csv) — ~100 filas")
        print("| Campo".ljust(20)+ "|Tipo".ljust(20)+ "|Escala".ljust(20)+ "|".ljust(20))
        print("| ".ljust(20)+ "|".ljust(20)+ "|".ljust(20)+"|".ljust(20))
        print("| id_cliente".ljust(20)+ "| int".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| nombre_cliente".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| email".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| ciudad".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| fecha_alta".ljust(20)+ "| date".ljust(20)+ "| Intervalo".ljust(20)+ "|".ljust(20) + "\n ")

        print("Ventas (ventas.csv) — ~120 filas")
        print("| Campo".ljust(20)+ "| Tipo".ljust(20)+ "| Escala".ljust(20)+ "|".ljust(20))
        print("| ".ljust(20)+ "|".ljust(20)+ "|".ljust(20)+"|".ljust(20))
        print("| id_venta".ljust(20)+ "| int".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| fecha".ljust(20)+ "| date".ljust(20)+ "| Intervalo".ljust(20)+ "|".ljust(20))
        print("| id_cliente".ljust(20)+ "| int".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| nombre_cliente".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| email".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| medio_pago".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20)+"\n ")

        print("Detalle_Ventas (detalle_ventas.csv) — ~343 filas")
        print("| Campo".ljust(20)+ "| Tipo".ljust(20)+ "|Escala".ljust(20)+ "|".ljust(20))
        print("| ".ljust(20)+ "|".ljust(20)+ "|".ljust(20)+"|".ljust(20))
        print("| id_venta".ljust(20)+ "| int".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| id_producto".ljust(20)+ "| int".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| nombre_producto".ljust(20)+ "| str".ljust(20)+ "| Nominal".ljust(20)+ "|".ljust(20))
        print("| cantidad".ljust(20)+ "| int".ljust(20)+ "| Razon ".ljust(20)+ "|".ljust(20))
        print("| precio_unitario".ljust(20)+ "| float".ljust(20)+ "| Razon ".ljust(20)+ "|".ljust(20))
        print("| importe".ljust(20)+ "| float".ljust(20)+ "| Razon ".ljust(20)+ "|".ljust(20)+ "\n ")



    elif opcion == 4:
        print("\nESCALAS DE MEDICIÓN: A continuación se detallan las escalas de medición con ejemplos aplicados al proyecto cuando corresponda. De no ser así, se incluye un ejemplo de referencia con fines didácticos.")
        print("- Nominal: Categórica sin orden")
        print("\t o  Ejemplos: id, nombre de cliente, email, ciudad, medio de pago, nombre de prodcuto.") 
        print("-	Ordinal: Categórica con orden")
        print("\t o	En el proyecto no se han encontrado atributos pertenecientes a dicha escala de medición.") 
        print("\t o	Ejemplos: Nivel de satisfacción. ")
        print("- Intervalo: Numérica sin cero real")
        print("\t o	Ejemplos: fecha, fecha de alta.") 
        print("- Razón: Numérica con cero absoluto")
        print("\t o	Ejemplos: precio unitario, cantidad, importe.\n ") 
   
    elif opcion == 5:
        print("\n Se ha utilizado Copilot con el fin de: ")
        print("\t -	El desarrollo del código inició con un enfoque básico, utilizando conocimientos previos de otros lenguajes de programación. Esto, sumado a la incorporación tardía al curso, el retraso en actividades y el limitado dominio de Python, resultó en una implementación simple con líneas de código que podrían optimizarse para mayor eficiencia.")
        print("\t -	Corregir los tipos de datos de las columnas precio_unitario e importe, cambiándolos de INT a FLOAT para permitir el almacenamiento de valores decimales.")
        print("\t -	Mejorar la visualización de la estructura de las tablas, sus atributos, tipos de datos y escalas de medición mediante el método .ljust(n), que alinea el texto a la izquierda y lo completa con espacios hasta alcanzar n caracteres.")
        print("\t -	Diseñar el Diagrama de Relaciones entre las tablas, con el objetivo de comprender su estructura y identificar redundancias en los atributos. Asimismo se detalló las entidades,atributos y relaciones \n")
        print("\t\t a.	Entidades principales: ")
        print("\t\t\t i.	Clientes (id_cliente, nombre_cliente, email, ciudad, fecha_alta)")
        print("\t\t\t ii.	Productos (id_producto, nombre_producto, categoria, precio_unitario) ")
        print("\t\t\t iii.	Ventas (id_venta, fecha, id_cliente, medio_pago) ")
        print("\t\t\t iv.	Detalle_Ventas (id_venta, id_producto, cantidad, precio_unitario, importe) \n")
        print("\t\t b.	Relaciones: ")
        print("\t\t\t i.	Un cliente puede tener muchas ventas → relación 1:N ")
        print("\t\t\t ii.	Una venta puede tener muchos detalles de venta → relación 1:N ")
        print("\t\t\t iii.	Un producto puede aparecer en muchos detalles de venta → relación 1:N \n")
        
        from PIL import Image
        imagen = Image.open("")
        imagen.show()
        print(imagen.size)



        print("\t -	A través del DER se puede observar que: \n")
        print("\t\t a.	la tabla Detalle_Ventas presenta los atributos nombre_producto y precio_unitario de forma redundante, ya que esta información puede y debe obtenerse de la tabla de Productos a través de la clave foránea de id_producto. ")
        print("\t\t b.	La tabla Ventas presenta los atributos nombre_cliente y el email de forma redundante, ya que está información puede o se debe obtenerse de la tabla Clientes a través de la clave foránea id_cliente.")

    elif opcion == 6:
        print("Muchísimas gracias por visitar la Tienda Aurelio.\n")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")