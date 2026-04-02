from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    name: str
    activo: bool = True
    
data = {"id": "123", "name": "John Doe"}
usuario = Usuario(**data)
print(usuario.model_dump_json())