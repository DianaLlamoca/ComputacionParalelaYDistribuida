# MODULE 4: DESIGN PRINCIPLES AND PATTERNS FOR DATA PIPELINES

# Laboratorio: Querying Data By Using Athena

## Task 1: Creating and querying an AWS Glue database and table in Athena
Es importante señalar que cuando se usa Athena, lo primero que debe hacerse es especificar un bucket S3 para mantener los resultados de cualquier consulta que se haga. Sin embargo, en el laboratorio se señala que un bucket ya ha sido creado, por lo que solo será necesario elegir dicho bucket.
Para ello, dentro del servicio Athena, iremos al apartado de "Query editor" y elegimos la opción "Configuración" que se encuentra en la parte superior:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen1.PNG)

Una vez allí, seleccionamos "Administrar":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen2.PNG)

En el apartado de "Location of query result", elegimos "Browse S3" y elegimos el bucket que fue creado al iniciar el laboratorio para luego seleccionar "Choose" y guardar:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n8-Im%C3%A1genes/Imagen3.PNG)
