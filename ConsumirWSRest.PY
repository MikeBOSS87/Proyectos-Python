
import requests
import sys
import json

url = "http://localhost:8080/CronosGlobalNet/WSDatosSencibles/BusquedaPersona/RealizaBusqueda"
peticion = "{ \"Datos\":{\"nombres\": \"Miguel\",\"apellidoP\":\"resendiz\",\"apellidoM\":\"gutierrez\",\"CURP\":\"\",\"fechaNacimiento\": \"\"} }"

PropiedadesURL = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

try:
    respuesta = requests.request( "POST", url, data = peticion, headers = PropiedadesURL )
    PersonasJSON = respuesta.json()

    for i in PersonasJSON[ 'PersonasEncontradas' ]:
        print( "Persona: {} {}" . format( i[ 'FechaNacimiento' ], i[ 'Nombres' ] ) )

except :
    print( "Ocurrio un error"  )
