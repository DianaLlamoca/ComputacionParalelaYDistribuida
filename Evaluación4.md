# ** MÓDULO 1 **
# Laboratorio: Accessing and Analyzing Data by UsingAmazon S3
## Task 1:
### Creando un nuevo CloudFormation Template para crear un bucket:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Creando%20un%20nuevo%20CloudFormation%20template.PNG)
Acá se está creando un bucket y se está configurando el acceso, así como la encriptación del bucket, etc.

Para validar el CloudFormation Template, ejecutaremos el comando **"aws cloudformation validate-template --template-body file://create_bucket.yml"**, y obtendremos el output correspondiente que indica que el template es válido:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/CloudFormation%20template%202.PNG)

Ahora, para crear un CloudFormation stack (pila) desde el template ejecutaremos el siguiente comando: **"aws cloudformation create-stack --stack-name ade-my-bucket  --template-body file://create_bucket.yml"**. Además, el output indica que el stack fue creado:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Stack.PNG)

Para verificar que el stack creó los recursos necesarios , ejecutaremos el siguiente comando para ver el output correspondiente: **"aws s3api list-buckets"**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Stack2.PNG)

En el laboratorio, se indica que debemos eliminar el bucket creado por "restricciones de seguridad del laboratorio". Para ello, usaremos el comando **"aws cloudformation delete-stack --stack-name ade-my-bucket"**:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/EliminarBucket.PNG)

Y ya abremos eliminado el bucket:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/EliminarBucket2.PNG)

Debemos recordar que el bucket que se creó anteriormente, tenía el nombre de "ade-my-bucket"; sin embargo, este no se muestra en la lista. Lo que significa que fue eliminado correctamente.

# --------

## Task 2:
### Carga de datos de muestra a un bucket S3
Primero, se descargará el archivo .csv:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/DescArchCSV.PNG)

Luego, descomprimimos el archivo con el comando 'unzip':

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Desc1.PNG)

Para ver el contenido del archivo .csv, usamos el comando 'cat':

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Desc2.PNG)

Ahora, lo que se realizará, será copiar la data a un bucket S3. 
Sin embargo, primero veremos el nombre del bucket, así que ejecutamos el comando "aws s3api list-buckets":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/C1.PNG)

Para copiar el archivo (o dataset) en el bucket, ejecutamos el siguiente comando: "aws s3 cp lab1.csv s3://LAB-BUCKET-NAME".
El parámetro <LAB-BUCKET-NAME> hace referencia al output que dio el anterior comando, por eso fue importante saber el nombre del bucket:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/C2.PNG)

De esta manera, ya abremos copiado el dataset al bucket S3. Para corroborar ello, usaremos el comando "aws s3 ls s3://LAB-BUCKET-NAME":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/C3.PNG)

Ello indica que se ha cargado correctamenta el archivo csv al bucket.

# --------

## Task 3:
### Consultando los datos con S3 Select:
Primero, iremos al servicio S3 Select y accedemos al bucket en donde hemos colocado el archivo .csv para configurarlo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T3_1.PNG)

Luego de realizar la configuración, en la parte inferior aparecerá el apartado "Consulta SQL", el cual ya contiene una consulta en SQL, que lo que hace es mostrar los 5 primeros registros:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T3_2.PNG)

Se pueden realizar diferentes consultas en S3 Select, por ejemplo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T3_3.PNG)

Acá se muestran los nombres de las primeras 3 filas

# --------

## Task 4:
### Modificar las propiedades de cifrado y el tipo de almacenamiento de un objeto:
Primero, accedemos al apartado "editar clase de almacenamiento" dentro del servicio S3 de Amazon:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T4_1.PNG)

Luego, en "clase de almacenamiento" seleccionamos "Intelligente-Tiering":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T4_2.PNG)

Por último, guardamos cambios de la configuración:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T4_3.PNG)

De esa manera, se modifican las propiedades de cifrado y el tipo de almacenamiento de un objetivo.

# --------

## Task 5:
### Comprimir y consultar el conjunto de datos:
Se comprimirá el archivo con los dos formatos ('zip' y 'gzip') con la finalidad de comparar, después, el size de cada archivo.
El primer paso será comprimir el archivo "lab1.csv" con el comando "zip lab lab1.csv". Para ello, usaremos la terminal de AWS Cloud9:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_1.PNG)

Con el comando anterior, se está comprimiendo el archivo "lab1.csv" a uno .zip de nombre "lab".
Ahora, se va a comprimir el mismo archivo (lab1.csv), pero a .gzip con el comando "gzip -v lab1.csv":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_2.PNG)

El archivo "lab1.csv" fue reemplazado por el archivo .gzip (debido a "-v" en el comando)

Para listar los archivos nuevos en el directorio, colocamos el comando "ls -la". "-la" permite ver el archivo en formato 'long' (lo cual permite ver los permisos y tamaño para cada archivo):

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_3.PNG)

Como puede verse, el archivo .gzip pesa menos que el .zip

Ahora, subimos el archivo .gzip al bucket con el comando "aws s3 cp lab1.csv.gz s3://ade-s3lab-bucket--a32060e0 --cache-control max-age=60":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_4.PNG)

Una vez realizado lo anterior, veremos si podemos usar Amazon S3 Select para consultar el archivo comprimido:

Para ello, vamos a Amazon S3, seleccionamos el bucket y el archivo .gzip. Posteriormente, colocamos la opción "Consultar con S3 Select".
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_5.PNG)

Y seleccionamos ".gzip" en el apartado de "compresión":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_6.PNG)

Y realizamos la consulta SQL:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_8.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T5_7.PNG)

Como puede verse, sí se pueden realizar consultas a un archivo comprimido, de la misma forma que en un archivo no comprimido.

# --------

## Task 6:
### Administrar y probar el acceso restringido para un miembro del equipo:
Primero, vamos a revisar el grupo de IAM DataScienceGroup y la política de IAM adjunta al grupo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_1.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_2.PNG)

Como se indicó en el laboratorio, por fines de seguridad del laboratorio, ya se han creado el grupo y la política de IAM para el equipo de ciencia de datos y un usuario de IAM para Paulo.

Para ver los permisos del grupo "DataScienceGroup" creado, seleccionamos la opción "Policity-For-Data-Science":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_3.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_4.PNG)

Ahora, determinaremos si el usuario "Paulo" puede acceder a los datos en Amazon S3. Para probar su acceso, se emitirán comandos de AWS CLI utilizando sus credenciales. Primero, se debe recuperar su ID de clave de acceso y su clave de acceso secreta, junto con la región de AWS de la cuenta.

Para acceder a ello, vamos a CloudFormation, seleccionamos "Stacks", clickeamos sobre el link que contiene "ADE" en la descripción  y entramos al apartado de "Outputs":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_5.PNG)

Procedemos a copiar ambas claves de acceso:
#### Para la clave de nombre "PauloAccessKey":
Copiamos dicha clave, regresamos a Cloud9 y creamos una variable de nombre AK para almacenar dicho valor:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_6.PNG)

#### Para la clave de nombre "PaulosSecretAccessKey":
Realizamos lo mismo: regresamos a Cloud9, copiamos la clave y creamos una variable de nombre SAK para almacenar dicho valor:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_7.PNG)

Para probar si el usuario "Paulo" puede ejecutar un comando de AWS CLI para el servicio Amazon Elastic Compute Cloud (Amazon EC2), se ejecutará el siguiente comando: "AWS_ACCESS_KEY_ID=$AK AWS_SECRET_ACCESS_KEY=$SAK aws ec2 describe-instances --region us-east-1"
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_8.PNG)

Como puede verse, aparece ese mensaje de error, que es lo esperado. Pues debemos recordar que la política de IAM adjunta al grupo de IAM en el que se encuentra este usuario no tiene permisos para Amazon EC2.

Ahora, probemos si el usuario "Paulo" puede ejecutar comandos de AWS CLI en un objeto S3 con el siguiente comando: "AWS_ACCESS_KEY_ID=$AK AWS_SECRET_ACCESS_KEY=$SAK aws s3api get-object --bucket <LAB-BUCKET-NAME> --key lab1.csv --region us-east-1 pulled_lab.csv"
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_9.PNG)

Para ver el contenido del objeto S3, usemos el comando "cat pulled_lab.csv":
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/T6_10.PNG)

El resultado anterior muestra que el usuario "Paulo" puede ejecutar comandos de AWS CLI en un objeto S3.

# -----------Accessing and Analyzing Data by UsingAmazon S3----------
