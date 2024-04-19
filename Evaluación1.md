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

# 3) Reiniciar automáticamente un servicio no está corriendo -ERROOOOOR
## Archivo 'sh' del comando 3
![]()

## Salida al ejecutar el archivo bash 2
![]()
<p></p>

# 4) Verificar la cantidad de instancias de un proceso y actuar si supera un umbral
## Archivo 'sh' del comando 4
![]()

## Salida al ejecutar el archivo bash 4
![]()
<p></p>

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
![]()

## Salida al ejecutar el archivo bash 8
![]()
<p></p>


# 9) Generar un informe de procesos que incluya PID, tiempo de ejecución y comando
## Archivo 'sh' del comando 9
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/SH_9.png)

## Salida al ejecutar el archivo bash 9
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/bash9.png)
<p>Este comando genera un informe de procesos en formato de texto en el que se muestran los ID, tiempo de ejecución y CMD de los procesos.</p>

# **COMANDO 'grep'**
# 1) Filtrar errores específicos en logs de aplicaciones paralelas

# 3) Contar el número de ocurrencias de condiciones de carrera registradas:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n1-Im%C3%A1genes/Evaluacion1/grep/grep3.png)
En este caso, se ven los números de ocurrencias de condiciones de carrera registradas para los archivos contenidos en la ruta /var/log/*.log de los archivos con extensiòn .log, y se ve que no hay dichas condiciones de carrera.

# **COMANDO 'pipes'**
Ejercicios:
Indica las actividades que realizan cada uno de los scripts:
## 1) watch "ps aux | grep '[a]pache2' | awk '{print \$1, \$2, \$3, \$4, \$11}'"
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Evaluaci%C3%B3n1-Im%C3%A1genes/Evaluacion1/pipes/pipe1_1.png)
Este script lo que hace es que, de todos los procesos existentes, se busque el proceso 'apache2' y proceder a imprimir las columnas 1,2,3,4 y 11. Dichas columnas corresponden a 'user','pid','%cpu','%mem','command'
