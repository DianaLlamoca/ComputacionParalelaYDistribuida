from collections import defaultdict
import threading
import random
import time

#Algoritmo de Chandy Lamport
class Chandy_Lamport:
    def __init__(self, process_id):
        self.process_id = process_id
        self.state = None
        self.channels = defaultdict(list)
        self.neighbors = []
        self.marker_received = {}
        self.local_snapshot = None
        self.lock = threading.Lock()

    def set_neighbors(self, neighbors):
        self.neighbors = neighbors
        for neighbor in neighbors:
            self.marker_received[neighbor.process_id] = False

    def initiate_snapshot(self):
        with self.lock:
            self.local_snapshot = self.state
            print(f"Robot {self.process_id} tomando una snapshot local: {self.local_snapshot}")
            self.send_marker_messages()

    def send_marker_messages(self):
        for neighbor in self.neighbors:
            self.send_message(neighbor, 'MARKER')

    def send_message(self, neighbor, message_type, content=None):
        message = (message_type, self.process_id, content)
        neighbor.receive_message(message)

    def receive_message(self, message):
        message_type, sender_id, content = message
        with self.lock:
            if message_type == 'MARKER':
                if not self.marker_received[sender_id]:
                    self.marker_received[sender_id] = True
                    if self.local_snapshot is None:
                        self.local_snapshot = self.state
                        print(f"Robot {self.process_id} tomando una snapshot local: {self.local_snapshot}")
                        self.send_marker_messages()
                    else:
                        self.channels[sender_id].append(content)
                else:
                    self.channels[sender_id].append(content)
            else:
                if self.local_snapshot is not None:
                    self.channels[sender_id].append(content)
                else:
                    self.process_message(message)

    def process_message(self, message):
        # Simulate processing of a normal message
        print(f"El robot {self.process_id} recibió un mensaje desde el robot {message[1]}: {message[2]}")

    def update_state(self, new_state):
        self.state = new_state

#Algoritmo de Raymond para exclusion mutua
class RaymondMutex:
    def __init__(self, node_id, parent=None):
        self.node_id = node_id
        self.parent = parent
        self.token_holder = (parent is None)
        self.request_queue = []

    def request_access(self):
        if self.token_holder:
            self.enter_critical_section()
        else:
            self.request_queue.append(self.node_id)
            self.send_request_to_parent()

    def send_request_to_parent(self):
        if self.parent:
            self.parent.receive_request(self)

    def receive_request(self, requester):
        if not self.token_holder:
            self.request_queue.append(requester.node_id)
            self.send_request_to_parent()
        elif requester.node_id == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token(requester)

    def send_token(self, requester):
        self.token_holder = False
        requester.receive_token(self)

    def receive_token(self, sender):
        self.token_holder = True
        if self.request_queue and self.request_queue[0] == self.node_id:
            self.enter_critical_section()
        else:
            self.send_token_to_next_in_queue()

    def send_token_to_next_in_queue(self):
        next_node_id = self.request_queue.pop(0)
        next_node = [node for node in nodes if node.node_id == next_node_id][0]
        self.send_token(next_node)

    def enter_critical_section(self):
        #La sección crítica será una tarea que consistirá en realizar un time.sleep de 3 segundos
        print(f"Robot {self.node_id} recién va a iniciar la tarea")

        lock=threading.Lock()

        def recurso_critico():
            print(f"Robot {self.node_id} realizando la tarea")
            with lock:
                time.sleep(3)
                print(f"Robot {self.node_id} terminó la tarea")
        recurso_critico()



    def leave_critical_section(self):
        print(f"Robot {self.node_id} dejando la seccion critica")
        if self.request_queue:
            self.send_token_to_next_in_queue()

#Algoritmo de relojes vectoriales
class VectorClock:
    def __init__(self, num_nodes, node_id):
        self.clock = [0] * num_nodes
        self.node_id = node_id

    def tick(self):
        self.clock[self.node_id] += 1

    def send_event(self):
        self.tick()
        return self.clock[:]

    def receive_event(self, received_vector):
        for i in range(len(self.clock)):
            self.clock[i] = max(self.clock[i], received_vector[i])
        self.clock[self.node_id] += 1

#Recolector de basura generacional
class GenerationalCollector:
    def __init__(self, size):
        self.size = size
        self.young_gen = [None] * size
        self.old_gen = [None] * size
        self.young_ptr = 0
        self.old_ptr = 0

    def allocate(self, obj, old=False):
        if old:
            if self.old_ptr >= self.size:
                self.collect_old()
            addr = self.old_ptr
            self.old_gen[addr] = obj
            self.old_ptr += 1
        else:
            if self.young_ptr >= self.size:
                self.collect_young()
            addr = self.young_ptr
            self.young_gen[addr] = obj
            self.young_ptr += 1
        return addr

    def collect_young(self):
        self.old_gen = self.old_gen + [obj for obj in self.young_gen if obj is not None]
        self.young_gen = [None] * self.size
        self.young_ptr = 0

    def collect_old(self):
        self.old_gen = [obj for obj in self.old_gen if obj is not None]
        self.old_ptr = len(self.old_gen)
        self.old_gen += [None] * (self.size - self.old_ptr)

#Para crear el sistema de coordinación de tareas, se creará una clase "Robot" que cohesione cada uno de los algoritmos
class Robot:
    #Se define un constructor el cual contendrá dichos algoritmos para cohesionarlos y crear el sistema de coordinación de tareas
    def __init__(self,nodo_id):
        self.nodo_id = nodo_id
        self.estado={} #Este diccionario indicará el estado en el que se encuentra el robot
        self.vecinos=[] #Esta lista almacenará la lista de los robots que son vecinos

        #Aquí es donde se implementan los algoritmos para cohesionarlos
        self.Chandy_Lamport=Chandy_Lamport(nodo_id)
        self.Raymond_Mutex=RaymondMutex(nodo_id)
        self.Reloj_Vectorial=VectorClock(len(self.vecinos)+1, nodo_id) #El primer parámetro hace referencia al número de nodos totales que debe ser parámetro
        self.Recolector_Gen=GenerationalCollector(random.randint(1,1024))

    #Ya que se hayan cohesionado los algoritmos en 1 sola clase (clase Robot) se hará uso de cada algoritmo.
    #Cada robot tendrá los métodos de los algoritmos distribuidos para que puedan usarlos.

    #Se implementarán los métodos del algoritmo Chandy_Lamport para hacer uso de él.
    #El primer método será el que se encargará de iniciar la toma de snapshots. Para ello, se usará el método "initiate_snapshot".
    def iniciar_snapshot(self):
        self.Chandy_Lamport.initiate_snapshot()

    #Luego, se implementará el método "sender_marker_message" para enviar el mensaje de marcador a todos los nodos vecinos
    def env_marc_msg(self):
        self.Chandy_Lamport.send_marker_messages()

    #Posteriormente, para enviar un mensaje, se llamará al método "send_message" con sus respectivos parámetros
    def env_msg(self,neighbor,message_type,content=None):
        self.Chandy_Lamport.send_message(neighbor,message_type,content=None)

    #Se implementa el método para recibir mensajes, llamanado al método correspondiente
    def rec_msg(self,message):
        self.Chandy_Lamport.receive_message(message)

    #Se implementa el método para procesar un mensaje normal. Para eso se hará uso del método "process_message"
    def proc_msg_normal(self,message):
        self.Chandy_Lamport.process_message(message)

    #Finalmente, se implementa el último método, el cual se encargará de actualizar el estado del robot con la información que este reciba durante la toma de snapshots
    #Por ello, se usará el método "update_state"
    def act_estado(self,new_state):
        self.Chandy_Lamport.update_state(new_state)


    #De la misma forma, se implementan los métodos relacionados a la clase "RaymondMutex" para hacer uso de él
    def solicitar_acceso(self): #Método para solicitar acceso cuando se quiere usar un recurso
        self.Raymond_Mutex.request_access()

    def enviar_soli_al_padre(self): #Método para enviar la solicitud de acceso al nodo padre
        self.Raymond_Mutex.send_request_to_parent()

    def recibir_solicitud(self,requester): #Método que procesa solicitudes de acceso de los demás nodos
        self.Raymond_Mutex.receive_request(requester)

    def enviar_token(self,requester): #Método para enviar un token al nodo que lo solicita
        self.Raymond_Mutex.send_token(requester)

    def recibir_token(self,sender): #Método para recibir el token de un nodo
        self.Raymond_Mutex.receive_token(sender)

    def env_token_sig_nodo(self): #Método para enviar el token al nodo siguiente en la cola de solicitudes
        self.Raymond_Mutex.send_token_to_next_in_queue()

    def entrar_zona_crit(self): #Método que indica que el robot está ingresando a la sección crítica
        self.Raymond_Mutex.enter_critical_section()

    def salir_zona_crit(self): #Método que indica que el robot está saliendo de la sección crítica
        self.Raymond_Mutex.leave_critical_section()


    #Se implementan los métodos de la clase "VectorClock"
    def reloj(self): #Este método se encargará de incrementar el contador local
        self.Reloj_Vectorial.tick()

    def enviar_evento(self): #Método para enviar un evento con el reloj vectorial actual
        self.Reloj_Vectorial.send_event()

    def recibir_evento(self,received_event): #Método que procesa el evento recibido y además actualiza el reloj vectorial local
        self.Reloj_Vectorial.receive_event(received_event)

    #Se implementan los métdos de la clase "GenerationalCollector":
    def asignar(self,obj): #Método que asigna memoria
        self.Recolector_Gen.allocate(obj)

    def recolector_jov(self): #Este método realiza la recolecta, pero en la generación más joven
        self.Recolector_Gen.collect_young()

    def recolector_ant(self): #Este método realiza la recolectar, pero de las generaciones anteriores
        self.Recolector_Gen.collect_old()



robot1=Robot(1)
robot2=Robot(2)
robot3=Robot(3)

robot1.vecinos=[robot2,robot3]
robot2.vecinos=[robot1,robot3]
robot3.vecinos=[robot1,robot2]

#El robot 1 inicia la toma de instantanea
robot1.iniciar_snapshot()
robot2.iniciar_snapshot()

print("=====")

#El robot 2 y 3 compiten por entrar a la zona crítica
robots=[robot2,robot3]
r=[]
for i in range(len(robots)):
    robot=threading.Thread(target=robots[i].entrar_zona_crit())
    robot.start()
    r.append(robot)
for robot in r:
    robot.join()
