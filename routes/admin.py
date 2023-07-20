from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.quartos import Quartos
from base_model.quarto_model import EdicaoQuarto


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

@router.get("/buscar-quarto/{numero_quarto}")
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
    """Criar quartos na base de dados.
    """
    busca = quartos.criar_muitos_quartos_exemplo()
    if busca == False:
        return JSONResponse(
            status_code=400,
            content=busca,
        )
    return JSONResponse(status_code=200, content='Criados')


@router.put("/editar-quarto/{numero_quarto}")
async def editar_quartos(numero_quarto:str, edicao: EdicaoQuarto):
    """Editar quartos da base de dados.
    """
    payload = edicao.dict(exclude_none=True, exclude_unset=True)
    payload['numero_quarto'] = numero_quarto

    atualizacao = quartos.editar_quartos(payload)
    if atualizacao == False:
        return JSONResponse(
            status_code=400,
            content=atualizacao,
        )
    return JSONResponse(status_code=200, content={
         "mensagem": f"Quarto {numero_quarto} atualizado com sucesso!"}
    )



@router.post("/deletar-quarto")
async def deletar_quartos():
    """Deletar quartos.
    """
    quartos.conexao.delete_many({})
    busca = 'Deletados'
    if not busca:
        return JSONResponse(
            status_code=400,
            content=busca,
        )
    return JSONResponse(status_code=200, content=busca)
