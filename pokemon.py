from fastapi import FastAPI, HTTPException
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
    if pokemones:
        return pokemones
    raise HTTPException(status_code=404, detail="Lista vacia")

@app.post('/pokemones', tags=['POKEMONES'])
def agg_pokemones(pokemon: Pokemon):
    
    for i in pokemon.tipos:
        if i not in tipos_pokemon:
            raise HTTPException(status_code=404, detail=f"HABILIDAD NO ENCONTRADA, ASEGURATE DE QUE SEA UNA HABILIDAD EXISTENTE {tipos_pokemon}")
    pokemones.append(pokemon)
    return pokemones
    
 
    
@app.get('/pokemones/{name_pokemon}',tags=['POKEMONES'])
def filtro_pokemon(name_pokemon:str):
    for i in pokemones:
       if i.nombre == name_pokemon:
            return i
       
    raise HTTPException(status_code=404, detail="POKEMON NO ENCONTRADO")