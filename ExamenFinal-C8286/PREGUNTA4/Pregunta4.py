import time
import random

class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.term = 0
        self.voted_for = None
        self.state = "seguidor"
        self.log = []
        self.commit_index = 0
        self.last_applied = 0
        #Añadiré un diccionario que almacenará las operaciones que se realiza por cada nodo
        self.operaciones={}
    def start_election(self):
        self.state = "candidato"
        self.term += 1
        self.voted_for = self.node_id
        votes = 1
        for peer in self.peers:
            if peer.request_vote(self.term, self.node_id):
                votes += 1
        if votes > len(self.peers) / 2:
            self.state = "lider"
            self.lead()

    def request_vote(self, term, candidate_id):
        if term > self.term:
            self.term = term
            self.voted_for = candidate_id
            return True
        return False

    def lead(self):
        while self.state == "lider":
            self.send_heartbeats()
            time.sleep(1)

    def send_heartbeats(self):
        for peer in self.peers:
            peer.receive_heartbeat(self.term, self.node_id)

    def receive_heartbeat(self, term, leader_id):
        if term >= self.term:
            self.term = term
            self.state = "seguidor"

#Se implementa la función para simular la latencia de la red
def simular_latencia_red(mensaje):
    #Será un tiempo aleatorio entre 0 y 1, para ello se usará la librería "random", así como "time"
    tiempo=time.sleep(random.uniform(0,1))

    #Pasado el tiempo de simulación de latencia, se retorna el mensaje
    return mensaje

#Se implementa la función para simular el fallo de nodos
def simular_fallo_nodos(nodos): #"nodos" será un diccionario, del cual se elegirá un nodo al azar para ser el nodo fallido
    id_nodos= list(nodos.keys()) #Se almacenan los id de los nodos
    id_nodo_fallido=random.choice(id_nodos) #Se elige el id de un nodo al azar
    del nodos[id_nodo_fallido] #Se elimina el nodo fallido del diccionario inicial "nodos" para simular el fallo de nodos
    print(f"El nodo, con ID {id_nodo_fallido}, ha fallado y se eliminó del conjunto de nodos:")
    print(nodos)

#Se implementa la función para simular la partición de los nodos
def simular_particion(nodos):
    #Para simular la partición, se dividirán a los nodos en 2 pequeños grupos
    id_nodos= list(nodos.keys()) #Antes de realizar la división, se obtiene el ID de cada nodo en una lista
    random.shuffle(id_nodos) #Para realizar la partición de manera "aleatoria", se mezclará la lista de forma aleatoria usando "shuffle"
    tam_particion=len(nodos)//2 #Se indicará el tamaño de cada partición, teniendo en cuenta que se dividirán en 2 grupos
    particion1=set(id_nodos[:tam_particion]) #Aquí es donde se crea el conjunto de la primera partición
    particion2=set(id_nodos[tam_particion:]) #Conjunto de la segunda partición
    particiones={"Particion1":particion1,"Particion2":particion2} #Finalmente, se crea el diccionario que contiene las particiones en uno solo
    print(f"Hubo una partición en la red, quedando:",particiones)
    return particiones

#Se implementa la función para simular la "curación de la red"
def simular_curacion(particiones): #Se pasa como parámetro el diccionario donde están las particiones
    #Para simular la curación, se deberán unir las particiones
    print(f"Las particiones antes de realizar la curación de la red es {particiones}")
    #Cada partición se convertirá en una lista para que se puedan unir
    particion1=list(particiones["Particion1"])
    particion2=list(particiones["Particion2"])

    #Se unen las particiones
    particiones_unidas=particion1+particion2

    #Se retornan los nodos unificados en un diccionario
    nodos={nodo_id: Node(nodo_id,particiones_unidas) for nodo_id in particiones_unidas}
    print(f"Se realizó la curación de la red {nodos}")

    return nodos

#Se implementa la función para simular la operación de cuando un nodo quiere aplicar una operación.
def aplicar_operacion(nodo,operacion):
    #Ese nodo es el que aplicará la operación, por lo que se le agregará dicha operación a su "log" local
    nodo.log.append(operacion)

    #Debido a que el atributo "commit_index" almacena el índice de la última operación que se realizó
    #(dicha operación también involucra a los demás nodos), de tal forma que "commit_index" servirá para asegurar la consistencia en la red,
    #este deberá actualizarse, comparando el valor actual del "commit_index" con el índice de la última operación que
    #se realizó en el "log". Para ello, se hará uso de la función "max" y así elegir el índice de la última operación hecha
    nodo.commit_index=max(nodo.commit_index, len(nodo.log)-1)

    #Ahora, se creará un bucle "for" para aplicar las operaciones que quedaron pendientes en el registro local.
    #Para ello, se usará el atributo "last_applied", que representa el índice de la última operación que se aplicó de forma local en el nodo
    #por lo que también será necesario usar el "commit_index", pues se deben aplicar las operaciones que quedaron pendientes en el log local
    for i in range(nodo.last_applied+1,nodo.commit_index+1):

        #Se aplican las operaciones pendientes
        operacion=nodo.log[i] #Se itera sobre las operaciones que aún no se han aplicado localmente

        #Consideré dos operaciones: lectura y escritura (el parámetro "operacion" es un diccionario que almacena la operación a realizar)
        #Y se realizará una simulación de cuando ya se completan las operaciones pendientes
        if operacion["tipo"]=="lectura":
            nodo.operaciones["tipo"]=operacion["tipo"]
            nodo.operaciones["dato"]=operacion["dato"]
            print(f"Se realizó la operación pendiente de lectura para el nodo {nodo.node_id}")
            print(nodo.operaciones)

        if operacion["tipo"]=="escritura":
            nodo.operaciones["tipo"] = operacion["tipo"]
            nodo.operaciones["dato"]=operacion["dato"]
            print(f"Se realizó la operación pendiente de escritura para el nodo {nodo.node_id}")
            print(nodo.operaciones)

#La operación local realizada anteriormente por el nodo, debe ser replicada en todos los demás
def replicar_operacion(nodo_lider,operacion):
    #Se usa el bucle "flor" para realizar la simulación del envío de la operación a los otros nodos
    for id_nodos_peers in nodo_lider.peers:
        if nodo_lider.node_id!=id_nodos_peers:
            #Se realiza el envío del mensaje, haciendo uso de la función "simular_latencia_red" que recibe como parámetro el mensaje
            simular_latencia_red(operacion)
            print(f"Se replicó el mensaje {operacion} para el nodo {id_nodos_peers} desde el nodo {nodo_lider.node_id}")


def main():
    nodos={} #En este diccionario, se almacenarán los nodos


    #Se almacena el ID del nodo, y un objeto de la clase "Node" que hace referencia a ese nodo
    nodos={nodo_id:Node(nodo_id,list(nodos.keys())) for nodo_id in range(5)} #Crearé 5 nodos para simular cada una de las operaciones

    #Se simula el fallo de la red:
    simular_fallo_nodos(nodos)

    print("===========")

    #Se simula la partición de la red:
    particiones=simular_particion(nodos)

    print("===========")

    #Se simula la "curación" de la red:
    nodos=simular_curacion(particiones)

    print("===========")

    #Se simula la aplicación de operaciones pendientes locales a cada uno de los nodos:
    for nodo in nodos.values():
        operacion = {"tipo": random.choice(["lectura", "escritura"]),
                     "dato": random.randint(1, 100), }

        #Se realizan las operaciones locales
        aplicar_operacion(nodo,operacion)
        aplicar_operacion(nodo,operacion)

    print("===========")

    #Se simula la replicación de las operaciones que hizo un nodo a los nodos restantes:
    nodos=list(nodos.values())
    print(f"El nodo {nodos[1].node_id} va a replicar la operacion local que hizo {nodos[1].operaciones} a los nodos restantes")
    replicar_operacion(nodos[1],nodos[1].operaciones)


if __name__ == "__main__":
    main()
