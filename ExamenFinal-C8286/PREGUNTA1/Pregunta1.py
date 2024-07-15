import asyncio

#Se crea la clase que representará al jupyter
class SimularJupyter:
    #Se define el constructor, el cual contendrá una "queue" o cola que maneje los eventos y los eventos con sus tipos correspondientes
    def __init__(self):
        # Se definen los diferentes tipos de evento por celda en un diccionario, donde el valor será la corrutina que representa a ese tipo de evento
        self.eventos = {"error_celda": self.error_celda,"ejecucion_celda":self.ejecucion_celda}

        self.cola_evento=asyncio.Queue() #Esta estructura de datos se encargará de manejar los eventos (cola de eventos)


    #Se crea la corrutina que se encargará de simular cada uno de los eventos
    async def simulacion_eventos(self):
        #Para procesar eventos de manera continua, se usará el bucle "while True"
        while True:
            #Para obtener el evento de la cola de eventos, se hará uso de "await event_queue.get()"
            evento=await self.cola_evento.get()
            #El "await" hará que la corrutina actual se pause hasta que haya un evento disponible en la cola


    #Se crean las corrutinas que se encargarán de simular los diferentes tipos de evento
    async def error_celda(self):
        print("Error al ejecutar la celda")

    async def ejecucion_celda(self):
        print("Celda en ejecucion")


async def main():
    jupyter=SimularJupyter()
    await jupyter.simulacion_eventos()

if __name__=="__main__":
    asyncio.run(main())
