from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.quartos import Quartos


router = APIRouter(prefix="/admin", tags=["admin"])

quartos = Quartos()

@router.get("/buscar-todos-quartos")
async def buscar_todos_quartos():
    """Buscar todos os quartos existentes na collections
    """
    busca = quartos.buscar_todos_quartos()
    if len(busca) == 0:
        return JSONResponse(
            status_code=400,
            content={"ERRO": "Não existem quartos cadastrados."},
        )
    return JSONResponse(status_code=200, content=busca)

@router.get("/buscar-quarto{numero_quarto}")
async def buscar_quarto_por_numero(numero_quarto:str):
    """Buscar quarto apenas por número
    """
    busca = quartos.buscar_quarto_por_numero(numero_quarto)
    if not busca:
        return JSONResponse(
            status_code=400,
            content=busca,
        )
    return JSONResponse(status_code=200, content=busca)


@router.post("/criar-quarto")
async def criar_quartos_exemplos():
    """Criar
    """
    busca = quartos.criar_muitos_quartos_exemplo()
    if busca == False:
        return JSONResponse(
            status_code=400,
            content=busca,
        )
    return JSONResponse(status_code=200, content='Criados')


@router.post("/deletar-quarto")
async def deletar_quartos():
    """Deletar
    """
    quartos.conexao.delete_many({})
    busca = 'Deletados'
    if not busca:
        return JSONResponse(
            status_code=400,
            content=busca,
        )
    return JSONResponse(status_code=200, content=busca)
