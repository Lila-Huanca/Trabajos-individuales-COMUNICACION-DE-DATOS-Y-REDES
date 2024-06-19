## ¿ Describe la estructura de tablas, elementos y atributos en Amazon DynamoDB ?
### 1. Tablas:
En DynamoDB, los datos se organizan en tablas. Cada tabla contiene un 2. conjunto de ítems.
A diferencia de las bases de datos relacionales, las tablas en DynamoDB no tienen un esquema fijo. Esto significa que cada ítem dentro de una tabla puede tener diferentes atributos.
### 2. Ítems:
Cada ítem es una unidad de datos en DynamoDB y se representa como un conjunto de atributos.
Cada ítem está identificado de manera única dentro de una tabla por su clave primaria.
La clave primaria puede consistir en solo una clave de partición o una combinación de clave de partición y clave de ordenación (sort key).
### 3. Atributos:
Los atributos son los datos específicos que componen cada ítem.
Cada atributo tiene un nombre y un valor asociado.
Los valores pueden ser de varios tipos de datos, como cadenas de texto, números, binarios, listas y mapas anidados.
## ¿ Explica cómo se puede provisionar la capacidad en DynamoDB y por qué es importante para gestionar el rendimiento y los costos ?

La capacidad provisional en DynamoDB es fundamental para asegurar que las aplicaciones puedan manejar eficazmente diferentes cargas de trabajo, mantener un rendimiento óptimo y gestionar de manera eficiente los costos operativos asociados con el servicio de base de datos NoSQL de Amazon.
