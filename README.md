# API Projects

Esto es una API REST de un CRUD de tareas en un proyecto, usando Flask con Python 3.7 y de base de datos MongoDB.

<!-- ### Requisitos previos:
* Python 3.7.*
* Docker -->

### Configuración del entorno Local

#### Instalación de Python

##### Windows:
Tienes que ir a [Python 3.7.2](https://www.python.org/downloads/release/python-377/) descargar el instalador y ejecutar el asistente de instalación.

##### Ubuntu:
Solo basta con ejecutar:
```bash
sudo apt-get install python3
```

#### Instalación de Docker y Docker Compose

##### Windows: 
Para instalar Docker basta con ir a [Docker For Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows) bajar el instalador y ejecutarlo, con esto Docker estará instalado, en este mismo instalador ya viendo integrado Docker Compose

#### Ubuntu:

Debe actualizar los repositorios e instalar los paquetes necesarios para el uso de docker:

```bash
sudo apt-get update

sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
```

Agregar docker a los repositorios oficiales.

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add 

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
```

Por ultimo solo debe instalar Docker

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

Para que docker funcione sin necesidad ejecutarse con sudo debe usar el siguiente comando y reiniciar su PC.

```bash
 sudo usermod -aG docker <your-user>
```

Para docker compose ejecuta estos comandos:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

### Ejecución de la aplicación:

Para poder ejecutar esta aplicación de manera simple, solo debe ejecutar el script **start.sh**, este script instalara las dependencias necesarias para ejecutar el proyecto, creara un contenedor de Docker corriendo MongoDB.

* **Nota**: El **script.sh** solo funciona en Ubuntu, en Windows deberá ejecutar los comandos de este archivo en su consola

```bash
bash start.sh
```

La aplicación estará corriendo en el puerto 5000 [API Project](http://localhost:5000)

#### Con Docker

Para poder ejecutar toda la aplicación en Docker debe ejecutar estos comandos:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

Al ejecutar estos comandos la aplicación tambíen correra en [Localhost](http://localhost:5000)


### Documentación de API

#### Postman
Para poder consumir y probar la API se tiene que usar postman o CURL, para usar postman primero se tiene que descarar de [aquí](https://www.postman.com/downloads/) e instalar.

En la carpeta postman hay 2 archivos:
* API Task.postman_collection.json
* api-task.postman_environment.json

El primero es los endpoints y el segundo es el ambiente de la API, para importarlos en Postman, debe seleccionar el botón de *import* ubicado en la parte superior izquierda, se deberá abrir un recuadro, seleccionamos *Upload Files* abrirá un explorador de archivos y seleccionamos los 2 anteriores, esto importará automáticamente los endpoints para probar.

#### Curl

Para probar con Curl, debe insalarse, en Windows solo vaya a este enlace [Curl For Windows](https://winampplugins.co.uk/curl/) descargue el insalador y curl estará instalado.

En Ubunto curl ya viene instalado por defecto, en caso contrario solo ejecute:

```bash
sudp apt-get install curl
```

**Tipo de datos:**
* status : Boolean
* description: String
* duration: Int
* recordedTime: Int

**Get All Task**

Solo debe sustituiar los **{}** con **true** o **false**
```bash
curl -L -X GET 'http://localhost:5000/api/task?status={}'
```

**Add New Task**

Sustituir {} con los valores deseados
```bash
curl -L -X POST 'http://localhost:5000/api/task' \
-H 'Content-Type: application/json' \
--data-raw '{
    "description":"{}",
    "duration":{},
    "recordedTime":{},
    "status":{}
}'
```

**Search Task**

Sustituir por el parametro de busqueda
```bash
curl -L -X GET 'http://localhost:5000/api/task/search?q={}'
```

**Update Task**

Sustituir los valores correspondientes
```bash
curl -L -X PUT 'http://localhost:5000/api/task/<id task>' \
-H 'Content-Type: application/json' \
--data-raw '{
    "description":{}
    "duration":{},
    "recordedTime":{},
    "status":{}
}'
```

**Delete Task**
```bash
curl -L -X DELETE 'http://localhost:5000/api/task/<id task>'
```

**Bulk Insert**
```bash
curl -L -X POST 'http://localhost:5000/api/task/bulk'
```