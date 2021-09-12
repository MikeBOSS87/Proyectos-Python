
import requests
import sys
import json
from tkinter import *
from tkinter import ttk

frmBusquedaPersona = Tk()
frmBusquedaPersona.title( 'Busqueda de personas' )
frmBusquedaPersona.geometry( '1700x800' )
frmBusquedaPersona[ 'bg' ] = 'light gray'

url = "http://localhost:8080/CronosGlobalNet/WSDatosSencibles/BusquedaPersona/RealizaBusqueda"
peticion = "{\r\n    \"Datos\": {\r\n        \"nombres\": \"Miguel\",\r\n        \"apellidoP\": \"resendiz\",\r\n        \"apellidoM\": \"gutierrez\",\r\n        \"CURP\":\"\",\r\n        \"fechaNacimiento\": \"\"\r\n    }\r\n}"

PropiedadesURL = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}
respuesta = requests.request( "POST", url, data = peticion, headers = PropiedadesURL )
PersonasJSON = respuesta.json()

for i in PersonasJSON[ 'PersonasEncontradas' ]:
    print( "Persona: {} {} {}" . format( i[ 'CURP' ], i[ 'FechaNacimiento' ], i[ 'Nombres' ] ) )


tv = ttk.Treeview( frmBusquedaPersona, columns = ( "Col1", "Col2" ) )
tv.column( "#0", width = 80 )
tv.column( "Col1", width = 80, anchor = CENTER )
tv.column( "Col2", width = 80, anchor = CENTER )

tv.heading( "#0", text = "Producto", anchor = CENTER )
tv.heading( "Col1", text = "Precio", anchor = CENTER )
tv.heading( "Col2", text = "Cantidad", anchor = CENTER )

tv.pack()

frmBusquedaPersona.mainloop(  )
