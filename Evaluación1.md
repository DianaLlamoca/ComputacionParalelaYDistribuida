# **COMANDO 'ps'**

# 1) Monitoreo de procesos por uso excesivo de CPU
## Archivo 'sh' del comando 1
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/SH1.png)

## Salida al ejecutar el archivo bash 1
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Imagen1.png)
<p>Este comando muestra el proceso que se está ejecutando, además del porcentaje de CPU que este utiliza.</p>

# 2) Identificar procesos zombis y reportar
## Archivo 'sh' del comando 2
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_2.PNG)

## Salida al ejecutar el archivo bash 2
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_2a.PNG)
<p>Este comando muestra el proceso zombie detectado (su ESTADO (S), ID y CMD).</p>

# 3) Reiniciar automáticamente un servicio no está corriendo
## Primero, instalamos apache2 en el sistema e iniciamos un servicio:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_3_Ins_Ap%26start.PNG)
## Archivo 'sh' del comando 3
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_3_sh.PNG)

## Salida al ejecutar el archivo bash 2:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_3_op.PNG)
<p>Se puede ver que el sistema se ha reiniciado, razón por la cual, luego de esta acción, el estado del servicio será "activo" aún.</p>

# 4) Verificar la cantidad de instancias de un proceso y actuar si supera un umbral
## Archivo 'sh' del comando 4
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_4_a.PNG)

Este comando está verificando el número de instancias del proceso de nombre "httpd". Además, se establece un umbral de 10 instancias.
Entonces, la variable "count" contiene la cantidad de instancias de dicho proceso.
Con la condicional "if" se establece la condicional de que si la variable "count" es mayor al valor de la variable "MAX_INSTANCES" (que es 10), se mostrará por pantalla el mensaje contenido en "echo", además de mostrarse el nombre del proceso con su cantidad de instancias. 

Sin embargo, en el ordenador donde estoy ejecutando el comando, el proceso de nombre "httpd" no existe. Por ese motivo, estoy usando el proceso de nombre "bash", el cual contiene 2 instancias. Por ese motivo, haré el ejemplo con las variables PROCESS_NAME y MAX_INSTANCES cambiadas para que se vea que el código funciona de igual manera:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_4_a_mod.PNG)

## Salida al ejecutar el archivo bash 4
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_4_op.PNG)
<p>Como puede verse, el código funciona de igual manera.</p>

# 5) Listar todos los procesos de usuarios sin privilegios (UID > 1000)
## Archivo 'sh' del comando 5
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/SH_5.png)

## Salida al ejecutar el archivo bash 5
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/bash_5.png)
<p>Este comando lo que permite es filtrar ciertos procesos de los usuarios tengan un valor de UID mayor a 1000. Por ello, se usa el comando 'awk' y así ejecutar dichas instrucciones.</p>

# 6) Alertar sobre procesos que han estado corriendo durante más de X horas
## Archivo 'sh' del comando 6
![]()

## Salida al ejecutar el archivo bash 6
![]()
<p></p>

# 7) Encontrar y listar todos los procesos que escuchan en un puerto específico
## Archivo 'sh' del comando 7
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Sh_7.png)

## Salida al ejecutar el archivo bash 7
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/bash7.png)
<p>Este comando permite mostrar todos los procesos que escuchan específicamente al puerto 80</p>

# 8) Monitorear la memoria utilizada por un conjunto de procesos y alertar si supera un umbral
## Archivo 'sh' del comando 8
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_8_sh_a.PNG)

Este comando lo que hace es ver si el proceso de nombre "mysqld" está usando más de 1024 de memoria. En caso sea cierto y se cumpla dicha condicional, se mostrará el mensaje que indicará el pid y nombre del proceso que está usando más memoria de la variable indicada como umbral, "MAX_MEM".

Debido a que en el computador que estoy realizando la ejecución no existe el proceso de nombre "mysqld", usaré el proceso "su" (solamente cambiaré esa variable):

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_8_sh_mod.PNG)

## Salida al ejecutar el archivo bash 8
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/ps_8_op.PNG)
<p>El código funciona de la misma forma.</p>


# 9) Generar un informe de procesos que incluya PID, tiempo de ejecución y comando
## Archivo 'sh' del comando 9
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/SH_9.png)

## Salida al ejecutar el archivo bash 9
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/bash9.png)
<p>Este comando genera un informe de procesos en formato de texto en el que se muestran los ID, tiempo de ejecución y CMD de los procesos.</p>

# **COMANDO 'grep'**
# 1) Filtrar errores específicos en logs de aplicaciones paralelas
Debido a que en el ordenador donde estoy realizando la actividad no tengo el directorio "myapp", usaré (para esta comando) el directorio "apache2".

## Archivo 'sh' del comando 1:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/grep1_a.PNG)

Este comando, lo que hace, es buscar (dentro de los archivos con extensión .log) de la ruta /var/log/apache2 si existe alguna coincidencia con la palabra "ERROR".
Sin embargo, al ejecutar el comando y no encontrar ninguna coincidencia con la palabra "ERROR" en los archivos con extensión .log, no devuelve ninguna salida como respuesta.



# 3) Contar el número de ocurrencias de condiciones de carrera registradas:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n1-Im%C3%A1genes/Evaluacion1/grep/grep3.png)

En este caso, se ven los números de ocurrencias de condiciones de carrera registradas para los archivos contenidos en la ruta /var/log/*.log de los archivos con extensión .log, y se ve que no hay dichas condiciones de carrera.

# 8) Monitorizar la creación de procesos no autorizados
Este comando permitirá mostrar la creación de procesos no autorizados y se mostrarán en pantalla:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/grep8_sh.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/grep8_op.PNG)

# 9) Detectar y alertar sobre ataques de fuerza bruta SSH
Este comando buscará los posibles ataques de fuerza bruta SSH en la ruta /var/log/auth.log.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/grep9_sh.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n2-Im%C3%A1genes/grep9_op_.PNG)


# **COMANDO 'pipes'**
Ejercicios:
Indica las actividades que realizan cada uno de los scripts:
## 1) watch "ps aux | grep '[a]pache2' | awk '{print \$1, \$2, \$3, \$4, \$11}'"
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n1-Im%C3%A1genes/Evaluacion1/pipes/pipe1_1.png)
Este script lo que hace es que, de todos los procesos existentes, se busque el proceso 'apache2' y proceder a imprimir las columnas 1,2,3,4 y 11. Dichas columnas corresponden a 'user','pid','%cpu','%mem','command'
