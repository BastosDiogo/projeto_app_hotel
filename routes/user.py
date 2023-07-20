from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.quartos import Quartos
from models.clientes import Cliente
from base_model.cliente_model import ClienteModel


router = APIRouter(prefix="/user", tags=["user"])

quartos = Quartos()
cliente = Cliente()


@router.put("/cadastrar-cliente")
async def cadastrar_cliente(dados: ClienteModel):
    """Endpoint para o cliente se caastrar na plataforma."""
    payload = dados.dict(exclude_defaults=True, exclude_none=True, exclude_unset=True)
    verificar_paramentros = cliente.verificar_parametros(payload)
    if len(verificar_paramentros) != 0:
        return JSONResponse(
            status_code=400,
            content={
                'EERO':'Parametro(s) Inválido(s)',
                "parametros":verificar_paramentros
            }
        )

    criar = cliente.criar_cliente(payload)
    if not criar:
        return JSONResponse(
            status_code=404,
            content={'EERO':'Por favor verifique os dados cadastrais'},
        )
    return JSONResponse(status_code=200, content=f'Cliente {payload["nome"]} foi cadastrado com sucesso')



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

