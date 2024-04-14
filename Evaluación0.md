# 2) Navigation
 
## Comandos: pwd, cd, ls

### Comando: *pwd* (print working directory)
Este comando muestra el directorio de trabajo actual en el que nos situamos (el cual es 'ubuntu').
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pwd.PNG)

### Comando: *ls*
Este comando muestra los directorios y/o archivos contenidos en el directorio actual en el que nos situamos.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls.PNG)

### Comando: *cd*
Este comando nos permite cambiar o movernos entre los distintos directorios existentes.
#### <sub>**Con ruta de acceso absoluta**.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cd_ruta-absoluta.PNG)
#### <sub>**Con ruta de acceso relativa**.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cd_ruta-relativa.PNG)

# -------------

# 3) Looking Around

## Comandos: ls, less, file

### Comando: *ls*
Este comando lista los directorios y/o archivos existentes.
#### <sub>**ls**: Solo muestra los archivos y/o directorios del directorio de trabajo actual.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls.PNG)

#### <sub>**ls /bin**: Muestra los archivos y/o directorios del directorio /bin.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls%20-%20bin.PNG)

#### <sub>**ls -l**: Muestra los archivos y/o directorios del directorio actual en formato 'long'.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls%20-l.PNG)

#### <sub>**ls -l /bin /etc**: Muestra los archivos y/o directorios de los directorios /bin y /etc en formato 'long'.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls%20-l%20bin%20etc.PNG)

#### <sub>**ls -la**: Muestra los archivos y/o directorios (incluyendo los ocultos) en formato 'long'.</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ls%20-la.PNG)
#### <sub>**ls -l -a**: Muestra los archivos y/o directorios (incluyendo los ocultos por el -a) en formato 'long' (es igual a 'ls -la').</sub>

#### <sub>**CONSIDERACIÓN - COMANDO: 'ls -la ..' o 'ls -l -a ..'**</sub>
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/consideracion.PNG)
**Los dos puntos '..' hacen referencia al directorio que contiene al directorio 'ubuntu', es decir, 'home'. En otras palabras, se obtienen los archivos y/o directorios ocultos y no ocultos del directorio 'home'. 'home' en este caso, puesto que dependerá del directorio actual en donde se encuentre el usuario.**

### Comando: *less*
Este comando permite visualizar archivos de texto mediante un visualizador de archivos de texto.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/less.PNG)

### Comando: *file*
Este comando permite indicar el tipo y/o formato de un archivo.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/file.PNG)

# -------------

# 4) A Guided Tour
### **Directorio root: '/'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/directorioroot.PNG)

### **Directorio boot: '/boot'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/directorio_boot.PNG)

### **Directorio etc: '/etc/**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/directorio_etc.PNG)

### **'bin' y 'usr/bin': '/bin' '/usr/bin'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/bin_usr-bin.PNG)

### **'sbin' y 'usr/sbin': '/sbin' '/usr/sbin'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/sbin_usr-sbin.PNG)

### **Directorio usr: '/usr'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/usr.PNG)

### **Directorio user/local: '/usr/local'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/usr-local.PNG)

### **Directorio var: '/var'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/var.PNG)

### **lib: '/lib'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/lib.PNG)

### **Directorio home: '/home'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/home.PNG)

### **Directorio root: '/root'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/root.PNG)

### **Directorio tmp: '/tmp'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/tmp.PNG)

### **Directorio dev: '/dev'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/dev.PNG)

### **Directorio proc: '/proc'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/proc.PNG)

### **Directorio media: '/media'**
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/media.PNG)

# -------------

# 5) Manipulating Files

## Comandos: cp, mv, rm, mkdir

### Comando: *cp*
Este comando permitirá copiar archivos y/o directorios.
#### *1) cp file1 file2*
Este comando permite copiar los contenidos de los archivos. Sin embargo, hay dos posibilidades:
Si 'file2' no existe, entonces al colocar el comando, dicho archivo se creará automáticamente con el contenido de 'file1' Por otra parte, si 'file2' existe, el contenido de 'file1' se copiará en 'file2':

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp%20file-file2-1.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp-file-file2-2.PNG)

#### *2) cp -i file1 file2*
En este comando, a diferencia del anterior, el '-i' indica que si el archivo existe, 'se preguntará' al usuario si desea sobreescribir el contenido:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp%20-i%20file-file2.PNG)

#### *3) cp file1 dir1*
Este comando copia un archivo 'file1' al directorio especificado 'dir1':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp%20file1%20dir1.PNG)

#### *4) cp -R dir1 dir2*
Este comando permite copiar el contenido de 'dir1' a 'dir2'. Si 'dir2' no existiera, este se creará automáticamente al ejecutar el comando:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp%20-R%20dir1%20dir2.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/%C2%B4cp%20-R%20dir1%20dir2-2.PNG)

### Comando: *mv*



### Comando: *rm*
Este comando sirve para borrar archivos y/o directorios:
### *1) rm file1 file2*
Este comando borra los archivos 'file1' y 'file2':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm-1.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm-2.PNG)

### *2) rm -i file1 file2*
Al colocar el '-i' (interactive), se preguntará al usuario si desea borrar dichos archivos:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm%20-i%201.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm%20-i%202.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm%20-i%203.PNG)

### *3) rm -r dir1 dir2*
Este comando borra los directorios (necesariamente debe ir '-r' para especificar que son directorios lo que se va a borrar) 'dir1' y 'dir2':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm%20-r%201.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/rm%20-r%202.PNG)

#### *También se le puede añadir '-i' para que el sistema pregunte si se van a borrar aquellos directorios: rm -r -i dir1 ...

### Comando: *mkdir*
Este comando crea directorios
### *1) mkdir dir ...* (los '...' hacen referencia a que se pueden crear muchos directorios en una sola línea de código)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/mkdir%201.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/mkdir%202.PNG)

# -------------

# 6) Working with Commands

### Comando: *type*
Este comando muestra qué tipo de comando ejecutará el shell:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/type.PNG)

### Comando: *which*
Este comando determina la ubicación exacta de un ejecutable determinado:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/which.PNG)

### Comando: *help*
Este comando es una función de ayuda incorporada disponible para cada una de las funciones integradas del shell:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/help.PNG)

### Comando: *--help*
Este comando muestra la descripción de la sintaxis y las opciones admitidas para dicho comando:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/help(--).PNG)

### Comando: *man*
Este comando muestra el manual del comando que se está colocando en el terminal. Provee información detallada, como la descripción, los autores, entre otros:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/man.PNG)

# -------------

# 7) I/O Redirection

### Standard Output
Para redirigir la salida estándar a un archivo, se usa '>':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Standard%20Output.PNG)

Aquí, la salida del comando 'ls' fue redirigida al archivo 'red.txt', por lo que ya no aparecen los resultados en la pantalla.

Ahora, para agregar 'nuevos' resultados al archivo, se usará '>>':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/StandardOutput2.PNG)

### Standard Input
Para redirigir la entrada estándar desde un archivo en lugar del teclado, se usa '<':
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/StandardINput.PNG)

Aquí se puede ver claramente que se le está pasando el comando 'sort' (es decir, que ordene los elementos contenidos en dicho archivo) y dicho resultado se mostrará en pantalla automáticamente. Es un 'standar 'input'' porque se le está pasando un comando que va a operar sobre ese archivo.

Por otra parte, en la siguiente imagen se muestran las dos operaciones juntas:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/StandardInput2.PNG)

Primero se realiza la operación de input, después la operación de output (es decir, primero se ordena, luego dicho resultado se almacena en un archivo de texto)

### Pipelines
Los 'pipelines' permiten conectar múltiples comandos. Por ejemplo: 'ls -l | less'
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/Pipelines1.PNG)
Aquí lo que se está realizando es que la salida del comando 'ls -l' se colocará en un archivo de texto, pues se especifica 'ls -l | less'.
Es decir, la salida del comando 'ls -l' se introduce en el comando 'less'.

### Filters
Los 'filters' se usan frecuentemente con los pipelines para filtrar información específica. Ejemplos:
#### *sort*:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/sort.PNG)

Aquí estamos listando los archivos y/o directorios para después ordenarlos de manera automática con 'sort'. El uso de '|' indica el uso de pipelines.

#### *uniq*:
El comando 'uniq' muestra datos sin duplicar, ejemplo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/uniq.PNG)


#### *grep*:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/grep.PNG)
Aquí estamos listando los procesos pertenecientes a 'usr'


#### *fmt*:
El comando 'fmt' lee el texto de entrada estándar y luego genera el texto formateado en la salida estándar:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/fmt.PNG)

En la imagen lo que se está haciendo es ordenar los elementos que están dentro del archivo 'texto.txt', para que después solo se seleccione los elementos no repetidos con 'uniq', para que finalmente se genere el texto formateado en la salida estándar (es decir, en 1 sola fila).

#### *pr*:
El comando 'pr' se utiliza para paginar o columnar archivos para imprimir:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/pr.PNG)

(También puede usarse en conjunto con pipelines)

#### *head*:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/head.PNG)
De la lista de procesos, solo listamos las primeras líneas mediante el comando 'head'.

#### *tail*:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/tail.PNG)
Mostramos solo las últimas lineas de la lista de procesos mediante el comando 'tail'.

#### *tr*:
El comando 'tr' permite manipular texto, ya sea para cambiar frases de mayúscula a minúscula, etc:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/tr.PNG)

Aquí usamos el comando 'tr' en el pipeline. Es decir, del contenido de 'lista.txt', cambia los elementos que contienen la 'a' (minúscula) por la 'A' (mayúscula).

#### *sed*:
El comando 'sed' permite realizar 'traducciones' de texto más sofisticadas:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/sed.PNG)

Mediante dicho comando pudimos reemplazar la palabra 'amarillo' por 'hola', luego de haber ordenado y seleccionado solo datos sin duplicar, mediante los comandos 'sort' y 'uniq', respectivamente.

#### *awk*:
El comando 'awk' permite llevar a cabo acciones determinadas. Por ejemplo:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/awk.PNG)

Aquí se está listando la lista de procesos, colocamos el comando 'grep' para listar todos los procesos que contienen 'usr' en su fila correspondiente y 'awk' para indicar que solo se muestren las columnas 1, 2 y 11 de ese grupo selecto que se estableció mediante el comando 'grep'.

# -------------

# 8) Expansion
Con la expansión, se escribe 'algo' y se expande a otra cosa. Para ello, veámoslo con un ejemplo:
En esta imagen, el comando 'echo' lo único que hace será repetir la frase que se le ha indicado.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/exp1.PNG)

Sin embargo, en el segundo comando de 'echo' (donde hay un '*') significa 'coincidir' con cualquier carácter en un nombre de archivo (en este caso, los nombres de los archivos del directorio actual):
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/exp2.PNG)

# Pathname Expansion
El mecanismo por el cual funcionan los 'comodines' (en el ejemplo anterior, el símbolo '*') se llama *expansión de nombre de ruta*. Para ejemplificar esto, se ejecutarán los siguientes comandos:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/exp_r_1.PNG)

Por ejemplo, en el primer comando, donde se usa 'echo', puede verse que estamos buscando los nombres de los archivos que comiencen con D (seguido de cualquier letra y/o número, símbolo: puede verse como una expresión regular).
En el segundo, indicamos que empiece el nombre del archivo por la letra 's' seguido de cualquier símbolo, también podemos especificarle que empiece con mayúscula o minúscula (comando 4 y 5), aunque también sirve para buscar más allá del directorio en el que nos encontramos (último comando de la imagen)

# Tilde Expansion
El carácter '~', cuando se usa al 'principio' de una palabra, se expande al nombre del directorio de inicio (expandir al directorio home del usuario).
Si no se especifica ningún usuario, se mostrará el directorio del inicio del usuario actual; caso contrario (si existe el otro usuario designado), se mostraría su directorio de inicio:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/exp_til_1.PNG)

El primer comando indica el directorio del inicio del usuario actual (puesto que no se especifica un nombre en concreto seguido de ~)
El segundo comando (puesto que no hay más usuarios creados, solo ubuntu) se mostraría dicho directorio de 'ubuntu' (que en este caso sería equivalente a solo 'echo ~', sin embargo solamente coloqué dicho ejemplo para hacer ambas distinciones de *tilde expansion*)
