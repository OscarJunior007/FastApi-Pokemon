from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

class Pokemon(BaseModel):
    id: Optional[int] = None
    nombre: str
    detalle: str
    tipos: list[str] = [""]
    altura: str
    habilidad: str
    # url:str
   



tipos_pokemon = [
    "Normal",
    "Fuego",
    "Agua",
    "Eléctrico",
    "Planta",
    "Hielo",
    "Lucha",
    "Veneno",
    "Tierra",
    "Volador",
    "Psíquico",
    "Bicho",
    "Roca",
    "Fantasma",
    "Dragón",
    "Siniestro",
    "Acero",
    "Hada"
]
pokemones = []


@app.get('/', tags=['inicio'])
def listar_pokemones():
    return pokemones


@app.post('/pokemones', tags=['POKEMONES'])
def agg_pokemones(pokemon: Pokemon):
    
    for i in pokemon.tipos:
        if i in tipos_pokemon:
            pokemones.append(pokemon)
            return pokemones
    
    print("NO SE AGG POKEMON, TIPO INCORRECTO") ## No se como enviar errores a web jajajajaj
    return []
@app.get('/pokemones/{name_pokemon}',tags=['POKEMONES'])
def filtro_pokemon(name_pokemon:str):
    for i in pokemones:
       if i.nombre == name_pokemon:
            return i
    return[]