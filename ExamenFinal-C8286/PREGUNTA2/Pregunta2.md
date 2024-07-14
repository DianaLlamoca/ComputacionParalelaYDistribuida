# Pregunta2:
## Crea un sistema de coordinación de tareas en una red de robots industriales:
• Usa el algoritmo de Chandy-Lamport para tomar instantáneas del estado global de los robots durante la ejecución de n tareas.

• Implementa el algoritmo de Raymond para la exclusión mutua en el acceso a recursos compartidos entre los robots.

• Utiliza relojes vectoriales para asegurar el ordenamiento parcial de los eventos y detectar violaciones de causalidad.

• Integra un recolector de basura generacional para la gestión eficiente de la memoria en los nodos de control de los robots.

# Solución 1: Implementación de los algoritmos distribuidos

## **Algoritmo de Chandy-Lamport:**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM1.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM2.1.PNG)

## **Algoritmo de Raymond:**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM3.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM4.PNG)

## **Algoritmo de relojes vectoriales:**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM5.PNG)

## **Algoritmo de recolector de basura generacional:**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM6.PNG)


## Integración de las clases de los algoritmos en una sola para crear el sistema de coordinación de tareas:
Se crea una clase "Robot" que almacenará todas las clases de los algoritmos distribuidos:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM7.PNG)

Luego de que se haya instanciado cada clase por algoritmo distribuido dentro de la clase "Robot", se implementan los métodos por cada algoritmo:

• Implementación de métodos en la clase robot para el algoritmo "Chandy-Lamport":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM8.PNG)

• Implementación de métodos en la clase robot para el algoritmo "Raymond":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM9.PNG)

• Implementación de métodos en la clase robot para el algoritmo de "relojes vectoriales":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM10.PNG)

• Implementación de métodos en la clase robot para el algoritmo de "recolector de basura generacional":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM11.PNG)

## Simulación: Instanciando objetos a la clase Robot y llamando a algunos métodos:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA2/Imagenes/IM12.PNG)
