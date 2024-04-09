# Navigation
 
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

# Looking Around

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

# A Guided Tour
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

# Manipulating Files

## Comandos: cp, mv, rm, mkdir

### Comando: *cp*
Este comando permitirá copiar archivos y/o directorios.
#### *1) cp file1 file2*
Este comando permite copiar los contenidos de los archivos. Sin embargo, hay dos posibilidades:
Si 'file2' no existe, entonces al colocar el comando, dicho archivo se creará automáticamente con el contenido de 'file1' Por otra parte, si 'file2' existe, el contenido de 'file1' se copiará en 'file2':

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp%20file-file2-1.PNG)
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/cp-file-file2-2.PNG)
