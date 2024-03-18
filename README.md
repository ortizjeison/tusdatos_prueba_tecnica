
# Prueba técnica Desarrollador Backend Python

## WEB SCRAPING
Para realizar la extracción de los datos, se hizo un proceso de ingeniería inversa del portal web y se determinó que las APIs que éste emplea en su backend.

### Base de datos
Para el almacenamiento de la información, se utilizó un archivo .json, el cual es administrado haciendo uso de la librería pysondb, para tratar dicho archivo como una base de datos, pudiendo así realizar operaciones CRUD con mayor fiabilidad:

![DB Example]("https://raw.githubusercontent.com/ortizjeison/tusdatos_prueba_tecnica/main/static/db.png")

### Casos de prueba
En cuanto a las pruebas de ejecución en paralelo de los servicios consultarDemandado y consultarDemandante, se ejecutan 15 peticiones en paralelo al respectivo endpoint, haciendo uso de un script en javascript ejecutado en un servidor local de nodeJs. Para validar que la información fue extraída correctamente, se valida al finalizar la prueba, que no hay registros en la base de datos de errores (request_errors.json).

![Test Example]("https://raw.githubusercontent.com/ortizjeison/tusdatos_prueba_tecnica/main/static/consola_test.png")

![Test Example]("https://raw.githubusercontent.com/ortizjeison/tusdatos_prueba_tecnica/main/static/consola_test2.png")

La documentación de estas pruebas, puede ser visualizado en documentacion_pruebas.pdf (https://github.com/ortizjeison/tusdatos_prueba_tecnica/blob/main/documentacion_pruebas.pdf)

## API

Para el desarrollo del API se implementaron las librerías Flask y APIFlask.

La documentación del uso del API puede encontrarse en el endpoint:
http://127.0.0.1:5000/apiDoc y en https://app.swaggerhub.com/apis/ortizjeison/my-project/1.0.0

### Autorización y autenticación
Se implementó una autenticación básica, en este caso, los usuarios registrados y sus contraseñas se encuentran en el código (No replicar, es una mala práctica)

## Frontend

Para la vista se desarrolló el endpoint /verResultados, el cual recibe un documento y un tipo de consulta (demandado, demandante). Luego de recibir la petición, se ejecuta el script que realiza las consultas, y finalmente se renderiza las respuestas de forma tabular, este proceso puede tomar unos cuantos minutos, dependiendo la cantidad de registros.

![Vista Resultados]("https://raw.githubusercontent.com/ortizjeison/tusdatos_prueba_tecnica/main/static/vista_resultados.png")

## Authors

- [Jeison Fernelix Ortiz López](https://github.com/ortizjeison)

