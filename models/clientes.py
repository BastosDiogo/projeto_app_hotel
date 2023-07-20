from mongo.conexao import Pymongo
from uuid import uuid1
#from base_model.cliente_model import ClienteModel

class Cliente(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._conexao = self.database['clientes']
    
    @property
    def conexao(self):
        return self._conexao
    

    def verificar_parametros(self, payload:dict):
        parametros = {
            "nome": True if payload.get('nome','') != '' else 'Nome inválido',
            "idade": True if payload.get('idade', 0) > 18 else 'Idade inferior a 18 anos.',
        }
        
        if payload.get('cpf'):
            cpf_existente = list(
                self.conexao.find({"cpf": payload.get('cpf')},{"_id":0, "id":1, "cpf":1})
            )
            cpf = 'CPF existente na base de dados.' if len(cpf_existente) !=0 else True

        else:
            cpf = 'CPF não existente.'

        parametros['cpf'] = cpf

        resposta = {}
        for chave, valor in parametros.items():
            if isinstance(valor, str):
                resposta[chave] = valor

        return resposta


    def criar_cliente(self, payload: dict):
        cliente = {
            "id": str(uuid1()),
            "nome": str(payload['nome']).upper(),
            "idade": int(payload['idade']),
            "cpf": payload['cpf'],
            "pets": payload.get('pets', []),
            "dependentes": payload.get('dependentes', [])
        }
        
        try:
            self.conexao.insert_one(cliente)
            return True
        
        except Exception as e:
            print(e)
            return False

