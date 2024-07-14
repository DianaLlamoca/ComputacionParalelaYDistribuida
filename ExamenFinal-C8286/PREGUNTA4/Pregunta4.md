# Pregunta 4 : Implementar un sistema distribuido en Python que simule las tres propiedades del Teorema CAP: consistencia, disponibilidad y tolerancia a particiones. El sistema debe demostrar cómo se comporta bajo diferentes configuraciones.

# En el código debes incluir:

• La simulación de latencia de red en la comunicación entre nodos.

• Un algoritmo de consenso sencillo como Raft o Paxos para gestionar la consistencia.

• Fallos aleatorios en los nodos para simular fallos de red o nodos caídos.

• Registros de operaciones y versiones de datos para gestionar la consistencia eventual.

• Diferentes configuraciones de particiones y curaciones en la red.

# Solución 1: Implementación del algoritmo Raft
**ALGORITMO RAFT:**

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_1.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_2.PNG)

# Solución 2: Implementación de la simulación de latencia de red en la comunicación entre nodos.

Aquí se realiza la simulación de la latencia al realizar el envío de mensajes:
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_3.PNG)

# Solución 3: Implementación de la función para simular el fallo de nodos.

Para ello, se elige el ID de un nodo de forma aleatoria, el cual representará al nodo fallido. Dicho nodo será eliminado del conjunto de nodos para simular el fallo del nodo.
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_4.PNG)
