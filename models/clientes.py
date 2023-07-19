from mongo.conexao import Pymongo
from base_model.cliente_model import ClienteModel

class Cliente(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._conexao = self.database['clientes']
    
    @property
    def conexao(self):
        return self._conexao
    
    def criar_cliente(self, nome:str, idade:int, cpf:str, dependentes:list=[]):
        cliente = ClienteModel(nome, idade, cpf)
        if len(dependentes) != 0:
            cliente.add_dependentes(dependentes)
        cliente = cliente.modelo_cliente()
        
        try:
            self.conexao.insert_one(cliente)
            return True
        
        except Exception as e:
            print(e)
            return False

