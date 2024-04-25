# Laboratorio: Accessing and Analyzing Data by UsingAmazon S3
## Creando un nuevo CloudFormation Template para crear un bucket:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Creando%20un%20nuevo%20CloudFormation%20template.PNG)
Acá se está creando un bucket y se está configurando el acceso, así coomo para la encriptación del bucket, etc.

Para validar el CloudFormation Template, ejecutaremos el comando "aws cloudformation validate-template --template-body file://create_bucket.yml", y obtendremos el output correspondiente que indica que el template es válido:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/CloudFormation%20template%202.PNG)

Ahora, para crear un CloudFormation stack (pila) desde el template ejecutaremos el siguiente comando: "aws cloudformation create-stack --stack-name ade-my-bucket  --template-body file://create_bucket.yml". Además, el output indica que el stack fue creado:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Stack.PNG)

Para verificar que el stack creó los recursos necesarios , ejecutaremos el siguiente comando para ver el output correspondiente: "aws s3api list-buckets"
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n4-Im%C3%A1genes/Stack2.PNG)
