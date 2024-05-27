# MODULE 4: DESIGN PRINCIPLES AND PATTERNS FOR DATA PIPELINES

# Laboratorio: Querying Data By Using Athena

## Task 1: Creating and querying an AWS Glue database and table in Athena

### *Specify an S3 bucket for query results
Es importante señalar que cuando se usa Athena, lo primero que debe hacerse es especificar un bucket S3 para mantener los resultados de cualquier consulta que se haga. Sin embargo, en el laboratorio se señala que un bucket ya ha sido creado, por lo que solo será necesario elegir dicho bucket.
Para ello, dentro del servicio Athena, iremos al apartado de "Query editor" y elegimos la opción "Configuración" que se encuentra en la parte superior:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen1.PNG)

Una vez allí, seleccionamos "Administrar":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen2.PNG)

En el apartado de "Location of query result", elegimos "Browse S3" y elegimos el bucket que fue creado al iniciar el laboratorio para luego seleccionar "Choose" y guardar:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen3.PNG)


Una vez que se especificó el bucket S3 para almacenar las consultas, se procederá a crear un AWS Glue database mediante el query editor del servicio Athena.

### *Create an AWS Glue database by using Athena query editor
Para ello, volvemos al apartado "Editor" y en la sección de "Consulta 1", procedemos a crear la base de datos con el siguiente comando SQL:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen4.PNG)

Seleccionamos "Ejecutar" y de esa manera un AWS Glue database de nombre "taxidata" es creado:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen5.png)

Si bien aparece el database en la sección de "Base de datos", para comprobar ello, iremos a AWS Glue para verificarlo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen6.PNG)

### *Create a table in the AWS Glue database and import data
En el servicio Athena, en la sección "Tablas y vistas", seleccionamos crear y se desplegarán las siguientes opciones:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen7.PNG)

De las cuales, seleccionamos "Crear una tabla a partir de un origen de datos: Datos del bucket S3". Seleccionamos ello y se mostrará la siguiente interfaz, en donde se pedirá el nombre de la tabla, así como la descripción, entre otros. Colocamos, entonces, la información que se indica en el laboratorio:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen8.PNG)

En "Configuración de la base de datos", como anteriormente ya hemos creado una base de datos llamada "taxidata", la seleccionamos:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen9.png)

En "Conjunto de datos", el cual sirve para especificar la ubicación del bucket de Amazon S3 de los datos, debemos colocar el mismo link que se indica en el laboratorio (seleccionamos esa casilla que aparece en la parte inferior):
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen10.PNG)

En el que si entramos a dicho bucket, para ver su contenido, podremos ver el conjunto de datos que contiene:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen11.PNG)

Después, respecto a las demás configuraciones, en "Formato de datos" se seleccionará CSV (que indica el formato en el que se encuentran los datos). Para "Detalles de columna", se elegirá "Agregar columnas en bloque" (esto provee la opción de agregar, de manera rápida, metadata a la tabla, como los nombres de las columnas y sus data types) y colocamos lo que se indica en el laboratorio para finalmente colocar "Agregar":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen12.PNG)

Se puede verificar lo anterior, para finalmente seleccionar "Crear tabla":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen13.PNG)

### *Preview data in the AWS Glue table
Para visualizar la data, en el apartado de "Datos-->"Base de datos", seleccionamos "taxidata":
En la sección "Tablas", al lado derecho de "yellow" (en los 3 puntos), seleccionaremos "Vista previa de la data":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen14.PNG)

A lo cual, se hará (por defecto, al seleccionar esta opción) una consulta de los 10 primeros datos de la tabla:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen15.PNG)

En conclusión, en esta primera parte, lo que se hizo fue crear un AWS Glue database y una tabla usando el query editor de Athena. Además, se conectó un AmazonS3 dataset a la tabla y se definió el schema para esa misma tabla usando el "agregar columnas en bloque". Finalmente, una vez creada la tabla, se realizó un "preview" a la data usando el preview table feature
