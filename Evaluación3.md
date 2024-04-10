# *Crear una aplicación web simple*
## *Una vez que ya hayamos instalado Flask en el sistema y creado el archivo 'sample-app.py', ejecutamos la aplicación:*
Si bien hay dos maneras de comprobar si la aplicación web se está ejecutando correctamente, yo usé el método de colocar la URL
en el navegador web:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pagina_web2.png)
Se puede ver que la página funciona correctamente.

## *Configurar la aplicación web para utilizar archivos de sitio web*
### *Primero, debemos crear el directorio 'templates' y, en ese directorio, crear el archivo 'index.html':
Como ya hemos creado el directorio 'templates' con 'mkdir templates', creamos el archivo 'index.html':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/index.png)

### *Creamos, ahora, el directorio 'static' y, en ese directorio, creamos el archivo 'style.css':
Como ya hemos creado el directorio 'static' con 'mkdir static', creamos el archivo 'style.css':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/static.png)

### Ahora, como ya hemos creado los archivos 'index.html' y 'style.css', debemos actualizar el código python que hemos creado para ejecutar la aplicación web 'sample-app.py'
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/index_cambiado.png)
Aquí, para renderizar el archivo HTML de manera automática en Flask, hemos utilizado la función 'render_templates', y por ello hemos modificado el 'return' de la app de python.

### Una vez creado y actualizado los archivos respectivos, procedemos a levantar la página web:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ejec_index_camb.png)
Ahora, en el navegador, copiamos la URL:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pag_levantada.png)
En el navegador se carga dicha interfaz gráfica.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cod_camb_pag_lev.png)
Podemos ver desde la terminal que la aplicación web levantó correctamente.

### Probamos con el método 'curl' para verificar la respuesta del servidor:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pag_lev_2_met.png)

---- 
# Crear un script de Bash para compilar y ejecutar un contenedor Docker
## *Crear directorios temporales para almacenar los archivos del sitio web y copiar los directorios del sitio web y sample_app.py en el directorio temporal*
Primero, para ello, creamos el archivo bash, con el nombre 'sample-app.sh':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/script_sample-app.sh.png)
Entramos al archivo bash y agregamos el 'she-bang':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/she-bang.png)
Además, en el archivo bash, colocamos los comandos para crear los directorios correspondientes y para copiar el directorio del sitio web y el script a 'tempdir':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Modificado.png)

## *Crear un archivo docker (Dockerfile)*
Agregamos los comandos respectivos al archivo bash:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/archivoDOcker.png)

## *Construir el contenedor Docker*
Para construir el contenedor docker, agregamos los dos siguientes comandos en el archivo bash:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/construyendoElContDocker.png)

## *Iniciar el contenedor y comprobar que se está ejecutando*
En el archivo bash, para iniciar el contenedor debemos ejecutar el comando 'docker run' y para comprobar que se está ejecutando (o que este ha sido creado), lo listamos con 'ps -a':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/iniciarElContYComprQueSeEjecuta.png)

Una vez terminado lo anterior, guardamos el archivo bash y lo ejecutamos:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/eJecutado.png)
Como puede verse en la imagen, el primer contenedor que aparece en la lista es el que acabamos de crear.

## *Investiga el contenedor Docker en ejecución y la aplicación web*
Debido a que el contenedor Docker ya está en ejecución, el contenedor Docker creará su propia dirección IP a partir de un espacio de direcciones de red privada. Para ver que la aplicación web se esté ejecutando, en el navegador web colocamos la URL 'http://localhost:8080':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pag_lev_final_docker.png)

Para mostrar todas las direcciones IP utilizadas, colocamos el comando 'ip address':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ips_mostradas.png)

## *Acceder y explorar el contenedor en ejecución*
Para acceder al contenedor, colocamos el comando 'docker exec -it' para entrar en modo '/bin/bash' (por línea de comandos) al contenedor, y para ver qué archivos contiene, usaremos el comando 'ls':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/carpetas_docker.png)

## *Detener y retirar el contenedor*
Para detener el contenedor, usaremos el comando 'docker stop (nombre_del_cont)' y para poder ver que el contenedor ha sido detenido, colocaremos 'docker ps -a':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/docker_cont_stop.png)
Entonces, al haber colocado este comando, la página web ya no debería estar ejecutándose:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pag_caida_stop.png)
Finalmente, como se indica en la Evaluación 3, se debe eliminar el contenedor. Para ello, usaremos el comando 'docker rm (nombre_del_cont)' y para ver que dicha acción ha sido ejecutada, listamos los contenedores con 'docker ps -a':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/docker-final.png)

*-------------------------------EVALUACIÓN 3--------------------------------
