import itertools
import random

actions = ["Crear","Modificar","Actualizar","Desplegar","Corrergir", "Debugear","Testear"]
l1 = ["un endpoint", "una aplicación", "una pagina web", "una api","un microservicio","un crud"]
l2 = ["en Flask","en NodeJS","en Spring","en Laravel","en Play for Scala","en Deno","en Django"]


def createTask():
    description = ''.join(random.sample(actions,1)) + " " + ''.join(random.sample(l1,1)) + " " + ''.join(random.sample(l2,1))
    duration = random.randint(59,361)


    recorded = (duration * random.randint(79,101)) / 100

    # status = True if duration == recorded else False

    return {
        "description": description,
        "duration": duration,
        "recordedTime": round(recorded),
        "status": random.sample([False,True],1)[0]
    }
   
