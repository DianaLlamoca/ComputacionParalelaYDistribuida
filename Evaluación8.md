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


