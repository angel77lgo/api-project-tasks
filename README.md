## API Projects

Esto es una API REST de un CRUD de tareas en un proyecto, usando Flask con Python 3.7 y de base de datos MongoDB.

### Requisitos previos:
* Python 3.7.*
* Docker

### Configuración del entorno Local

Para poder ejecutar esta aplicación de manera simple, solo debe ejecutar el script **start.sh**, este script instalara las dependencias necesarias para ejecutar el proyecto, creara un contenedor de Docker corriendo MongoDB.

```bash
bash start.sh
```

La aplicación estará corriendo en el puerto 5000 [API Project](http://localhost:5000)

### Con Docker

Para poder ejecutar toda la aplicación en Docker debe ejecutar estos comandos:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

Al ejecutar estos comandos la aplicación tambíen correra en [Localhost](http://localhost:5000)

