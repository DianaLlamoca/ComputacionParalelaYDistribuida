#Algoritmo Dijkstra-Scholten: Terminacion de procesos
import time
import random

class DijkstraScholten:
    def __init__(self, process_id, neighbors):
        self.process_id = process_id
        self.neighbors = neighbors
        self.parent = None
        self.children = set()
        self.active = True

    def send_message(self, recipient):
        print(f"Mensaje enviado al nodo {recipient}")
        recipient.receive_message(self, self.process_id)

    def receive_message(self, sender, sender_id):
        print(f"Mensaje recibido del nodo {sender} al nodo {sender_id}")
        if self.parent is None:
            self.parent = sender
        self.children.add(sender_id)
        self.process_task()

    def process_task(self):
        #Se simula la tarea de procesamiento
        self.active = False
        self.check_termination()

    def check_termination(self):
        if not self.active and not self.children:
            if self.parent:
                self.parent.receive_termination(self.process_id)

    def receive_termination(self, child_id):
        self.children.remove(child_id)
        self.check_termination()



#Algoritmo de Ricart-Agrawala: Exclusion mutua
class RicartAgrawalaMutex:
    def __init__(self, node_id, num_nodes):
        self.node_id = node_id
        self.num_nodes = num_nodes
        self.clock = 0
        self.request_queue = []
        self.replies_received = 0

    def request_access(self):
        self.clock += 1
        self.request_queue.append((self.clock, self.node_id))
        for node in nodes:
            if node.node_id != self.node_id:
                node.receive_request(self.clock, self.node_id)

    def receive_request(self, timestamp, sender_id):
        self.clock = max(self.clock, timestamp) + 1
        self.request_queue.append((timestamp, sender_id))
        self.request_queue.sort()
        self.send_reply(sender_id)

    def send_reply(self, target_id):
        for node in nodes:
            if node.node_id == target_id:
                node.receive_reply(self.node_id)

    def receive_reply(self, sender_id):
        self.replies_received += 1
        if self.replies_received == self.num_nodes - 1:
            self.enter_critical_section()

    def enter_critical_section(self):
        print(f"Nodo {self.node_id} ingresando a la seccion critica")
        self.leave_critical_section()

    def leave_critical_section(self):
        self.replies_received = 0
        self.request_queue = [(t, n) for t, n in self.request_queue if n != self.node_id]
        for timestamp, node_id in self.request_queue:
            self.send_reply(node_id)
        print(f"Nodo {self.node_id} dejando la seccion critica")


#Algoritmo de sincronizacion de relojes: Algoritmo de Berkeley
class BerkeleyNode:
    def __init__(self, node_id, time):
        self.node_id = node_id
        self.time = time

    def adjust_time(self, offset):
        self.time += offset

class BerkeleyMaster:
    def __init__(self, nodes):
        self.nodes = nodes

    def synchronize_clocks(self):
        times = [node.time for node in self.nodes]
        average_time = sum(times) / len(times)
        for node in self.nodes:
            offset = average_time - node.time
            node.adjust_time(offset)
        return [(node.node_id, node.time) for node in self.nodes]

#Algoritmo Cheney para recoleccion de basura:
class CheneyCollector:
    def __init__(self, size):
        self.size = size
        self.from_space = [None] * size
        self.to_space = [None] * size
        self.free_ptr = 0

    def allocate(self, obj):
        if self.free_ptr >= self.size:
            self.collect()
        addr = self.free_ptr
        self.from_space[addr] = obj
        self.free_ptr += 1
        return addr

    def collect(self):
        self.to_space = [None] * self.size
        self.free_ptr = 0
        for obj in self.from_space:
            if obj is not None:
                self.copy(obj)
        self.from_space, self.to_space = self.to_space, self.from_space

    def copy(self, obj):
        addr = self.free_ptr
        self.to_space[addr] = obj
        self.free_ptr += 1
        return addr

#Se crea la clase "Message" con los atributos que se solicitan en la pregunta:
class Message:
    #La clase debe tener atributos para el sender, content y timestamp
    def __init__(self,sender,content,timestamp):
        self.sender=sender
        self.content=content #En este caso, el contenido del mensaje será una lista que almacene el "tipo" del mensaje, así como el "contenido" --> [mensaje_tipo,mensaje_contenido]
        self.timestamp=timestamp #El timestamp será importante para calcular el tiempo en el algoritmo de Berkeley

#Se crea la clase "Node" con los métodos y atributos que se solicitan en la pregunta 3:
class Node:
    def __init__(self,node_id,total_nodes):
        self.node_id=node_id
        self.total_nodes=total_nodes
        #Teniendo en cuenta de que se van a enviar mensajes a otros nodos, además de que los algoritmos necesitan de los nodos vecinos.
        #Entonces se creará una lista que almacene a los vecinos de cada nodo
        self.vecinos=[]
        #Además, cada nodo tendrá una instancia de los algoritmos creados para cohesionarlos (con los parámetros correspondientes a cada clase por algoritmo)
        self.Dijkstra_Scholten=DijkstraScholten(node_id,self.vecinos)
        self.RicardAgrawala=RicartAgrawalaMutex(node_id,total_nodes)
        self.Berkeley=BerkeleyNode(node_id,time.time())
        self.Cheney=CheneyCollector(random.randint(1,1024)) #El tamaño será un valor numérico aleatorio entre 1 y 1024

    #Se implementan los métodos que se solicitan en la pregunta 3:
    #Antes de implementar el método para enviar mensajes, será necesario crear un método que se encargue de agregar los vecinos para cada nodo.
    #De esa manera, el nodo podrá enviar mensajes a sus nodos vecinos
    def añadir_vecino(self,vecino):
        self.vecinos.append(vecino)

    #Ahora, se implementará el método para enviar mensajes
    def enviar_mensajes(self,nodo_destino,content):
        #El mensaje deberá ser una instancia de la clase "Message" que se creó anteriormente
        mensaje=Message(self.node_id,content,time.time())
        #Dicho mensaje se envía al nodo destino (para ello, se implementará un método donde el nodo destino lo reciba)
        nodo_destino.recibir_mensajes(mensaje)

    def recibir_mensajes(self, mensaje):
        #Cuando el mensaje es recibido, este (al ser una instancia de la clase "Message", tiene el atributo "content").
        #Ese atributo es el que especifica el tipo de mensaje que se está recibiendo, así como su contenido, para en base a ello se llamen a los
        #métodos correspondientes de "receive_message" o "receive request" de los algoritmos distribuidos
        contenido=mensaje.content
        mensaje_tipo,mensaje_contenido=contenido[0],contenido[1] #Pues el atributo "content" es una lista


        #Pueden haber tres casos: que el mensaje sea del tipo "DijkstraScholten", "RicardAgrawala". "Berkeley".
        #Caso 1: Si el tipo de mensaje es DijkstraScholten --> se llamará al método "receive_message" o "receive_termination"
        #de la clase que representa a ese algoritmo
        if mensaje_tipo=="DijkstraScholten":
            #Dependiendo del contenido del mensaje, se llamará a uno de esos dos métodos
            if mensaje_contenido=="recibir_mensaje":
                self.Dijkstra_Scholten.receive_message(mensaje.sender) #Se le pasa el parámetro que representa al nodo que le envió ese mensaje
            elif mensaje_contenido=="recibir_terminacion":
                self.Dijkstra_Scholten.receive_termination(mensaje.sender) #Se le pasa el parámetro que representa al nodo que le envió ese mensaje

        #Caso 2: Si el tipo de mensaje es RicardAgrawala. Debido a que hay dos métodos "receive", el contenido del mensaje
        #será el que determinará a qué método llamar
        if mensaje_tipo=="RicardAgrawala":
            if mensaje_contenido=="recibir_solicitud":
                self.RicardAgrawala.receive_request(mensaje.timestamp,mensaje.sender)
            elif mensaje_contenido=="recibir_respuesta":
                self.RicardAgrawala.receive_reply(mensaje.sender)

        #Caso 3: Si el tipo de mensaje hace referencia al algoritmo de sincronización de relojes
        if mensaje_tipo=="Berkeley":
            if mensaje_contenido=="ajustar_tiempo":
                #El nodo maestro, antes de calcular el tiempo promedio, debe ajustar los tiempos recibidos teniendo en cuenta el retraso de la red:
                self.Berkeley.adjust_time(mensaje.timestamp-self.Berkeley.time)

    #Se implementa el método para enviar los mensajes de terminación
    def env_msg_term(self):
        for v in self.vecinos:
            #Se usa el método "enviar_mensajes" definido arriba y se pasa los parámetros correspondientes
            v.enviar_mensajes(self,self.node_id,["DijkstraScholten","recibir_terminacion"]) #"content", como se indicó arriba, será una lista que indica el "mensaje_tipo" y "mensaje_contenido"-->[mensaje_tipo,mensaje_contenido]


    #Se implementa el método para detectar la terminación de procesos
    def detectar_terminacion(self):
        if not self.Dijkstra_Scholten.active: #Si no está activo, entonces se devuelve True indicando la detección de terminación de procesos
            return True
        else:
            return False #De lo contrario, se devolverá False

#Se crea la clase "Network" que se solicita en la pregunta 3.
class Network:
    def __init__(self,numero_nodos):
        self.nodos=[] #Esta lista almacenará los nodos creados
        for nodo in range(numero_nodos):
            self.nodos.append(Node(nodo,numero_nodos)) #Pues la clase "Node" definida arriba tiene como parámetros el ID y el total de nodos

        self.vecinos=[] #Esta lista almacenará los vecinos del nodo, que será necesaria para implementar los métodos de "iniciar" y "detener" la red
        self.vecinos_local=[] #Esta será una variable "auxiliar", que servirá solo para que los vecinos estén ubicados en la posición de la lista, posición que corresponde al ID del nodo actual
        #Es decir, [nodo_0],[vecino1_vecino2];[nodo_1],[vecino1,vecino2] y así sucesivamente.
        for nodo in self.nodos:
            for nodo2 in self.nodos:
                if nodo.node_id != nodo2.node_id:
                    self.vecinos_local.append(nodo2)
            self.vecinos.append(self.vecinos_local)
            self.vecinos_local=[]

    #Se implementan los métodos que se indican en la pregunta 3: para iniciar y detener la red de nodos.

    #Método para iniciar la red de nodos:
    def iniciar(self):
        #Para iniciar la red, se empezará iniciando los algoritmos.
        #Algoritmo de Dijkstra-Scholten: Se crearán instancias de dicha clase para inicializarla
        Procesos=[DijkstraScholten(self.nodos[i],self.vecinos[i]) for i in range(len(self.nodos))]

        print("Procesos",Procesos)

        #Cada proceso tendrá los métodos y atributos de la clase DijkstraScholten, lo que significa que podrán enviar, recibir mensajes, etc.
        #Ejemplo de donde un proceso envía un mensaje a otro proceso:
        Procesos[0].send_message(Procesos[1])

    #Se implementa el método detener
    def detener(self):
        #Cada nodo realizará la función de detener a sus vecinos. Para ello, se llamará de manera recursiva a la función
        for vecino in range(len(self.vecinos)):
            for vecino2 in range(len(self.vecinos[vecino])):
                if vecino!=vecino2:
                    print(f"Nodo {vecino2} detenido por el nodo {vecino}")


if __name__ == "__main__":
    #Creando los nodos. En este caso, serán 3
    red=Network(3)
    #print("nodo 0",red.nodos[0])
    #print("vecinos del nodo 0",red.vecinos[0])
    red.iniciar()
    print("------------")
    red.detener()
