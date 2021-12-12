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
# Importacion de librerias base de python
from typing import DefaultDict, Optional
from enum import Enum

# Se importa Pydantic, para definir los modelos de datos y librerias para definicion de modelos, campos y validaciones
from pydantic import BaseModel, Field, EmailStr, PaymentCardNumber

# Se importa el modulo FastAPi de la libreria fastapi
from fastapi import FastAPI, Body, Query, Path

# Se crea una instancia de la clase FastAPI
app = FastAPI()

# Models - Aqui se definen los modelos de datos


class HairColor (Enum):
    red = "red"
    blond = "blond"
    brown = "brown"
    white = "white"
    black = "black"


class Person(BaseModel):
    # atributo: tipo de dato. Cuando se usa la opcion Optional, puede o no cargarse el valor. Y se debe asignar un valor por defecto
    # La libreria Field ayuda a agregar validaciones a nivel de modelo y en cuanto a opciones, funciona igual que los paths y los response
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="First name",
        description="First name of the person"
    )

    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="Last name",
        description="Last name of the person")

    email: EmailStr = Field(
        ...,
        title="Email",
        description="Email of the person"
    )

    payment: PaymentCardNumber = Field(
        default=None,
        title="Payment",
        description="Payment card number of the person"
    )

    age: int = Field(
        ...,
        gt=0,
        le=115,
        title="Age",
        description="Age of the person")

    hair_color: Optional[HairColor] = Field(
        default=None,
        title="Hair color",
        description="Hair color of the person"
    )

    is_married: Optional[bool] = Field(
        default=None,
        title="Relationship status",
        description="Relationship status of the person"
    )

    # Clase para colocar defaults de prueba
    # Si quisiera hacerlo a nivel de atributo, se debera usar el decorador Field con el parametro example seteado
    class Config:
        schema_extra = {
            "example": {
                "first_name": "Oscar Eduardo",
                "last_name": "Chaparro Blancas",
                "email": "oscar.e.chaparro@gmail.com",
                "age": 34,
                "hair_color": "brown"
            }
        }


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="City",
        description="City where the person lives"
    )

    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="State",
        description="State where the person lives"
    )

    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        title="Country",
        description="Country where the person lives"
    )

    class Config:
        schema_extra = {
            "example": {
                "city": "Iztapalapa",
                "state": "CDMX",
                "country": "México"
            }
        }

# Se crea un path operation decorator usando la funcion get
# En el home de la aplicacion se ejecutara nuestra funcion


@app.get("/")  # Path Operation Decorator
def home():  # Path Operation Function
    return {"message": "Hello World"}

# Request and Response Body


@app.post("/person/new")
# El parametro Body es una clase que se encarga de definir el modelo de datos que se va a recibir y al usar ... se dice que es obligatorio
def create_person(person: Person = Body(...)):
    return person

# Validaciones query parameters

# Aqui se definen las Query Validation Parameters que se van a recibir al solciitar los valores de nombre y edad


@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title="Person Name",
        description="The name of the person. It is between 1 and 50 characters",
        example="Oscar Eduardo"
    ),
    # En este caso, se definio desde la validacion que la edad fuera obligatoria, sin embargo, esto debe indicarse dentro del modelo como buena practica
    age: int = Query(
        ...,
        title="Person Age",
        description="The age of the person. It is an obligatory integer",
        example=34
    )
):
    return {name: age}

# Validaciones path parameters


@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="The ID of the person. It is an obligatory integer",
        example=21
    )
):
    return {person_id: "It exists"}

# Validaciones request body


@app.put("/person/update/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="The ID of the person. It is an obligatory integer",
        example=21
    ),
    person: Person = Body(
        ...,
        title="General data",
        description="The person data. It is an obligatory object",
    ),
    location: Location = Body(
        ...,
        title="Location data",
        description="The location of the person. It is an obligatory object",
    )
):
    results = person.dict()
    results.update(location.dict())
    return results
