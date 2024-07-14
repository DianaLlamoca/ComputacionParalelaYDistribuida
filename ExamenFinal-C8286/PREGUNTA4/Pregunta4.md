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

# Solución 4: Implementación de la función para simular la partición de los nodos.

Para realizar esta simulación, la función recibirá como argumento el conjunto de nodos restantes (sin el nodo fallido, pues este ha sido removido debido al fallo que presentó). Dicho conjunto de nodos restantes presentará una partición (simulando que hubo un fallo en la red o similar).
![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_5.PNG)
Por ese motivo, esta función realizará la partición de manera aleatoria en un conjunto de 2 particiones.

# Solución 5: Implementación de la función para simular la "curación de la red"

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_6.PNG)

Esta función recibe como parámetro el diccionario donde están almacenadas las particiones, para después realizar el paso de unir ambas particiones que se generaron.
Para ello, primero se realiza la conversión al tipo de dato "list", se mezclan las particiones, y finalmente se crea el diccionario final que almacenará la red sin las particiones.

# Solución 6: Implementación de la función para simular la operación de cuando un nodo quiere aplicar una operación.

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_7.PNG)

Esta función simula la operación (consideré 2 operaciones: lectura y escritura) que realiza cada nodo de forma independiente.

# Solución 7: Implementación de la función que realiza la replicación de la operación local a partir de un nodo a todos los demás

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_8.PNG)

Esta función simula la replicación de una operación realizada por un nodo a todos los demás en la red.


# Función "main" para incluir las funciones creadas

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_9.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_10.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_11.PNG)

# Output de la simulación

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_12.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_13.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_14.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_15.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_16.PNG)

![](https://github.com/DianaLlamoca/ComputacionParalelaYDistribuida/blob/main/ExamenFinal-C8286/PREGUNTA4/Imagenes/IM_17.PNG)
