'''
uvicorn main:app --reload

Esta es la instruccion que se ejecuta dentro de la ventana de la terminal y se entiende como sigue:
    Se usa uvicorn para iniciar el servidor (uvicorn)
    Se usa el nombre de la aplicacion que se encuentra en la carpeta main (main)
    Se usa el nombre de la variable que contiene la aplicacion (app)
    Se agrega un modificador --reload para que se ejecute el servidor cada vez que se modifique algun archivo

Y esto es lo que retorna el comando:
INFO:     Will watch for changes in these directories: ['Z:\\scripts\\MaterialCursosPlatzi\\CursoFastAPI\\fast-api-hello-world']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [20532] using statreload
INFO:     Started server process [24272]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

'''
#Se importa el modulo FastAPi de la libreria fastapi
from fastapi import FastAPI

#Se crea una instancia de la clase FastAPI
app = FastAPI()

#Se crea un path operation decorator usando la funcion get
#En el home de la aplicacion se ejecutara nuestra funcion

@app.get("/")
def home():
    return {"message": "Hello World"}