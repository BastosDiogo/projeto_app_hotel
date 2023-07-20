from pydantic import BaseModel
from typing import Optional

class ClienteModel(BaseModel):
    nome: str = "Nome do cliente"
    idade: int = 0
    cpf: str = "99999999999"
    dependentes:list = []
    pets: Optional[list] = []
