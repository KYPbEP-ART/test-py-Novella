from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Player(BaseModel):
    name: str
    level: int

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/players/")
def create_player(player: Player):
    return {"message": f"Создан игрок {player.name} уровня {player.level}"}