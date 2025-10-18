## 📘 Documentación

### 1° demo: asincrónica

### 1. Tema, problema y solución

**TEMA**: Este proyecto simula la gestión de “Tienda Aurelio”, una tienda minorista, utilizando datos sintéticos.  
**PROBLEMA**: La falta de integración y acceso a datos provenientes de múltiples bases de datos impide tener una visión clara del negocio y su rentabilidad. Esta situación también obstaculiza el análisis, la visualización y el modelado efectivo de la información.  
**SOLUCIÓN**: El objetivo principal es analizar estas bases de datos. Para ello, se procederá a analizar cada una, identificando sus entidades, atributos, tipos de datos, escalas de medición y las relaciones entre ellas. El resultado será un escenario de datos consistente que permita:

- **Analizar datos**: Identificar el inventario de productos, determinar el volumen de ventas en períodos específicos, comprender la frecuencia de compra de los clientes, analizar la tasa de clientes perdidos, descubrir patrones de compra, entre otras.
- **Visualizar datos**: Crear un dashboard que muestre el crecimiento de la tienda en función de las ventas, los productos y el comportamiento de los clientes.
- **Modelar datos**: Aplicar algoritmos para predecir comportamientos futuros, como la demanda de productos o la tendencia de ventas.

---

### 2. Dataset de referencia: fuente, definición, estructura, tipos y escala de medición

**FUENTE**: Los datos fueron generados con fines educativos. Las bases de datos se crearon para el aprendizaje de análisis, visualización y modelado de datos.Asimismo, presentan poca o nula consistencia, así como datos faltantes o nulos, por lo que, para fines prácticos, se asemejan a los datos de un negocio real.  
**DEFINICIÓN**: La base de datos estructurada en formato Excel representa de manera integral a la “Tienda Aurelio”, e incluye el catálogo de productos, el registro de clientes y las operaciones de venta.

- **Productos (productos.csv)**: Inventario o catálogo de artículos disponibles.
- **Clientes (clientes.csv)**: Registro de la cartera de clientes.
- **Ventas (ventas.csv)**: Registro de las transacciones realizadas.
- **Detalle de Ventas (detalle_ventas.csv)**: Desglose de los productos incluidos en cada venta.

**ESTRUCTURA POR TABLA**: A continuación se detalla la estructura de cada tabla, incluyendo: el nombre, el archivo del dataset, la cantidad de filas, los campos, sus tipos de dato y las escalas de medición.

**Productos (productos.csv)** — ~100 filas

| Campo           | Tipo  | Escala  |
|---------------- |-------|---------|
| id_producto     | int   | Nominal |
| nombre_producto | str   | Nominal |
| categoría       | str   | Nominal |
| precio_unitario | float | Razón   |

**Clientes (clientes.csv)** — ~100 filas

| Campo          | Tipo  | Escala   |
|----------------|-------|----------|
| id_cliente     | int   | Nominal  |
| nombre_cliente | str   | Nominal  |
| email          | str   | Nominal  |
| ciudad         | str   | Nominal  |
| fecha_alta     | date  | Intervalo|

**Ventas (ventas.csv)** — ~120 filas

| Campo          | Tipo  | Escala   |
|----------------|-------|----------|
| id_venta       | int   | Nominal  |
| fecha          | date  | Intervalo|
| id_cliente     | int   | Nominal  |
| nombre_cliente | str   | Nominal  |
| email          | str   | Nominal  |
| medio_pago     | str   | Nominal  |

**Detalle_Ventas (detalle_ventas.csv)** — ~343 filas

| Campo           | Tipo  | Escala |
|-----------------|-------|--------|
| id_venta        | int   | Nominal|
| id_producto     | int   | Nominal|
| nombre_producto | str   | Nominal|
| cantidad        | int   | Razón  |
| precio_unitario | float | Razón  |
| importe         | float | Razón  |

**ESCALAS DE MEDICIÓN**: A continuación se detallan las escalas de medición con ejemplos aplicados al proyecto cuando corresponda. De no ser así, se incluye un ejemplo de referencia con fines didácticos.

- **Nominal**: Categórica sin orden  
  Ejemplos: id, nombre de cliente, email, ciudad, medio de pago, nombre de producto.
- **Ordinal**: Categórica con orden  
  No se han encontrado atributos en esta escala.  
  Ejemplo: Nivel de satisfacción.
- **Intervalo**: Numérica sin cero real  
  Ejemplos: fecha, fecha de alta.
- **Razón**: Numérica con cero absoluto  
  Ejemplos: precio unitario, cantidad, importe.



### 3. Información, pasos, pseudocódigo y diagrama del programa (Sprint 1)

#### 3.1 Contenidos accesibles desde el menú

1. Tema, problema y solución.
2. Dataset de referencia.
3. Estructura por tabla.
4. Escalas de medición.
5. Sugerencias y mejoras con Copilot.
6. Salir.

#### 3.2 Pasos

1. Cargar en memoria los textos de esta documentación (por ejemplo, leyendo este `.md` o un módulo `textos.py`).
2. Mostrar un menú numérico con las secciones enumeradas arriba.
3. Según la opción elegida, imprimir el texto correspondiente en pantalla.
4. Permitir volver al menú hasta seleccionar “Salir”.

#### 3.3 Pseudocódigo

```plaintext
Inicio
  Cargar textos/plantillas de documentación en un diccionario
  Mientras True:
    Mostrar menú:
      1. Tema, problema y solución
      2. Dataset de referencia
      3. Estructura por tabla (tipo y escala)
      4. Escalas de medición
      5. Sugerencias y mejoras con Copilot
      6. Salir
    Leer opción
    Si opción == 1..5: imprimir texto asociado
    Si opción == 6: romper bucle
Fin
```

#### 3.4 Diagrama de flujo

El diagrama de flujo se encuentra adjunto en la carpeta de Google Drive, según lo establecido en clase.

---

### 4. Sugerencias y mejoras aplicadas con Copilot

Se ha utilizado Copilot con el fin de:
-	El desarrollo del código inició con un enfoque básico, utilizando conocimientos previos de otros lenguajes de programación. Esto, sumado a la incorporación tardía al curso, el retraso en actividades y el limitado dominio de Python, resultó en una implementación simple con líneas de código que podrían optimizarse para mayor eficiencia.
-	Corregir los tipos de datos de las columnas `precio_unitario` e `importe`, cambiándolos de `INT` a `FLOAT` para permitir el almacenamiento de valores decimales.
-	Mejorar la visualización de la estructura de las tablas, sus atributos, tipos de datos y escalas de medición mediante el método `.ljust(n)`, que alinea el texto a la izquierda y lo completa con espacios hasta alcanzar n caracteres.
-	Uso de Copilot para convertir documentos de Word a Markdown.
-	Diseñar el Diagrama de Relaciones entre las tablas, con el objetivo de comprender su estructura y identificar redundancias en los atributos. Asimismo se detalló las entidades, atributos y relaciones.

Aquí se encuentra el link del Diagrama de Entidad Relacional: https://github.com/MiriamChen10/Tienda_Aurelio/blob/0a7dcd9181b6f68fb658e8b85801797c4c0d18cd/DER%20original.png

#### a. Entidades principales

- i. **Clientes**: id_cliente, nombre_cliente, email, ciudad, fecha_alta
- ii. **Productos**: id_producto, nombre_producto, categoría, precio_unitario
- ii. **Ventas**: id_venta, fecha, id_cliente, medio_pago
- iv. **Detalle_Ventas**: id_venta, id_producto, cantidad, precio_unitario, importe

#### b. Relaciones

- i. Un cliente puede tener muchas ventas → relación 1:N
- ii. Una venta puede tener muchos detalles de venta → relación 1:N
- iii. Un producto puede aparecer en muchos detalles de venta → relación 1:N


-	A través del DER se puede observar que:
- a. la tabla `Detalle_Ventas` presenta los atributos `nombre_producto` y `precio_unitario` de forma redundante, ya que esta información puede y debe obtenerse de la tabla de `Productos` a través de la clave foránea de `id_producto`.
- b. La tabla `Ventas` presenta los atributos `nombre_cliente` y el `email` de forma redundante, ya que está información puede o se debe obtenerse de la tabla `Clientes` a través de la clave foránea `id_cliente`.


### ANEXO

**Materiales de clase**  
**Páginas consultadas**:

- a. Tipos de Datos en Python  
  - i. https://elpythonista.com/tutorial-python/tipos-python  
  - ii. https://www.datacamp.com/es/blog/python-data-types

- Escalas de medición  
  - a. https://www.questionpro.com/blog/es/tipos-de-escalas-de-medicion-para-investigadores/  
  - b. https://www.formpl.us/blog/measurement-scale-type  
  - c. https://ocw.unizar.es/ocw/pluginfile.php/2991/course/section/913/Tema%202_Conceptos%20Basicos%20y%20Escalas%20de%20Medida.pdf

- Uso de Deepseek para revisión de redacción  
- Uso de Copilot para cumplir con el punto 4  
- Uso de Copilot para la búsqueda de estructura del código en Python
