from tkinter import *
from tkinter import ttk

import requests
import sys
import json

url = "http://localhost:8080/CronosGlobalNet/WSDatosSencibles/BusquedaPersona/RealizaBusqueda"
peticion = "{\r\n    \"Datos\": {\r\n        \"nombres\": \"Miguel\",\r\n        \"apellidoP\": \"resendiz\",\r\n        \"apellidoM\": \"\",\r\n        \"CURP\":\"\",\r\n        \"fechaNacimiento\": \"\"\r\n    }\r\n}"

PropiedadesURL = {
    'content-type': "application/json",
    'cache-control': "no-cache"
}

try:
    frmBusquedaPersona = Tk()
    frmBusquedaPersona.title( 'Busqueda de personas' )
    frmBusquedaPersona.geometry( '1500x500' )
    frmBusquedaPersona[ 'bg' ] = 'light gray'

    respuesta = requests.request( "POST", url, data = peticion, headers = PropiedadesURL )
    PersonasJSON = respuesta.json()

    dgvPersonas = ttk.Treeview( frmBusquedaPersona, selectmode = "browse" )
    dgvPersonas.grid( row = 1, column = 1, padx = 20, pady = 20 )
    dgvPersonas[ "columns" ] = ( "Col1", "Col2", "Col3", "Col4" )
    dgvPersonas[ "show" ] = "headings"

    dgvPersonas.column( "Col1", width = 180, anchor = CENTER )
    dgvPersonas.column( "Col2", width = 150, anchor = CENTER )
    dgvPersonas.column( "Col3", width = 200, anchor = CENTER )
    dgvPersonas.column( "Col4", width = 150, anchor = CENTER )

    dgvPersonas.heading( "Col1", text = "CURP", anchor = CENTER )
    dgvPersonas.heading( "Col2", text = "FECHA DE NACIMIENTO", anchor = CENTER )
    dgvPersonas.heading( "Col3", text = "NOMBRE(S)", anchor = CENTER )
    dgvPersonas.heading( "Col4", text = "APELLIDO PATERNO", anchor = CENTER )

    for i in PersonasJSON[ 'PersonasEncontradas' ]:
        #print( "Persona: {} {}" . format( i[ 'FechaNacimiento' ], i[ 'Nombres' ] ) )
        dgvPersonas.insert( "", 'end', iid = i[ 'PersonaObjId' ], values = ( i[ 'CURP' ], i[ 'FechaNacimiento' ], i[ 'Nombres' ], i[ 'APaterno' ] ) )

    dgvPersonas.pack()

    frmBusquedaPersona.mainloop(  )
except ValueError:
    print( "Ocurrio un error en general." )