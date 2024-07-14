# Pregunta 3:
## Implementa un sistema distribuido en Python para la ejecución de tareas científicas en una red de computadoras, utilizando los siguientes algoritmos:
• 1. Dijkstra-Scholten para la detección de terminación de procesos distribuidos.

• 2. Ricart-Agrawala para la exclusión mutua en el acceso a recursos compartidos.

• 3. Sincronización de relojes para asegurar que todos los nodos tengan una vista consistente del tiempo.

• 4. Algoritmo de recolección de basura (Cheney) para gestionar la memoria en los nodos de computación.

# Instrucciones
## Crear una clase Message.
* Esta clase debe tener atributos para el remitente (sender), el contenido (content) y la marca de tiempo (timestamp).

## Crea una clase Node:
• Cada nodo debe tener un identificador (node_id), el número total de nodos en la red (total_nodes), y una referencia a la red.
• Implementa métodos para enviar mensajes a otros nodos, manejar solicitudes de exclusión mutua utilizando el algoritmo de Ricart-Agrawala, y detectar la terminación de procesos distribuidos con el algoritmo de Dijkstra-Scholten.
• Implementa un método para sincronizar los relojes de los nodos.
• Implementa un método para realizar la recolección de basura utilizando el algoritmo de Cheney.

## Crea una clase Network:
• Esta clase debe manejar la creación y la coordinación de los nodos en la red.
• Implementar métodos para iniciar y detener la red de nodos.


## Simulación


========================

# Solución 1: Implementación de los algoritmos distribuidos
Algoritmo Dijkstra-Scholten:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA3/Imagenes/I1.PNG)

Algoritmo Ricard Agrawala:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA3/Imagenes/I2.PNG)

Algoritmo Berkeley:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA3/Imagenes/I3.PNG)

Algoritmo Chenney Collector:

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA3/Imagenes/I4.PNG)

# Solución 2: Creación de la clase "Message"
Las instrucciones indican que se debe crear la clase con los atributos "sender", "content" y "timestamp":

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA3/Imagenes/I5.PNG)
