
import requests
import sys
import json

url = "http://localhost:8080/CronosGlobalNet/WSDatosSencibles/BusquedaPersona/RealizaBusqueda"
peticion = "{\r\n    \"Datos\": {\r\n        \"nombres\": \"Miguel\",\r\n        \"apellidoP\": \"resendiz\",\r\n        \"apellidoM\": \"gutierrez\",\r\n        \"CURP\":\"\",\r\n        \"fechaNacimiento\": \"\"\r\n    }\r\n}"

PropiedadesURL = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

try:
    respuesta = requests.request( "POST", url, data = peticion, headers = PropiedadesURL )
    PersonasJSON = respuesta.json()

    for i in PersonasJSON[ 'PersonasEncontradas' ]:
        print( "Persona: {} {}" . format( i[ 'FechaNacimiento' ], i[ 'Nombres' ] ) )

except :S
    print( "No se pudo conectar al servidor: localhost:8080"  )
