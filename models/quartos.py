from mongo.conexao import Pymongo
from base_model.quarto_model import QuartoModel
class Quartos(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._conexao = self.database['quartos']
    
    @property
    def conexao(self):
        return self._conexao
    
    def criar_muitos_quartos_exemplo(self):
        lista_quartos = []
        for numero_quarto in range(1,11):
            numero_quarto = str(numero_quarto)
            quarto = QuartoModel(numero_quarto, 0, 0, 0,).modelo_quarto()
            lista_quartos.append(quarto)
        try:
            self.conexao.insert_many(lista_quartos)
        
        except Exception as e:
            print(e)
            return False
            
    def buscar_todos_quartos(self):
        try:
            busca = list(self.conexao.find({},{"_id":0}))
            return busca
        except Exception as e:
            print(e)
            return []
    
    def buscar_quarto_por_numero(self, numero_quarto:str):
        numero_quarto = str(numero_quarto)
        try:
            busca = list(self.conexao.find({'numero_quarto': numero_quarto},{"_id":0}))
            return busca
        
        except Exception as e:
            print(e)
            return []


    def editar_quartos(self, payload: dict):
        update = {}
        for chave, valor in payload.items():
            update[chave] = valor
        update.pop('numero_quarto')

        try:
            self.conexao.update_one(
                {"numero_quarto": payload['numero_quarto']},
                {"$set": update}
            )
            return True

        except Exception as erro:
            print(erro)
            return False


    def criar_quarto(self, payload: dict):
        numeros_dos_quartos = list(self.conexao.distinct('numero_quarto',{"status": "ativo"}))
        if len(numeros_dos_quartos) == 0:
            numero_ultimo_quarto = 1
        else:
            numeros_dos_quartos.sort()
            numero_ultimo_quarto = str(int(numeros_dos_quartos[-1]) + 1)

        update_organizado = {"numero_quarto": numero_ultimo_quarto,"status":"ativo"}
        for chave, valor in payload.items():
            update_organizado[chave] = valor

        try:
            self.conexao.insert_one(update_organizado)
            return True

        except Exception as erro:
            print(erro)
            return False
