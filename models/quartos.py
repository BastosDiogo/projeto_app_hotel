from mongo.conexao import Pymongo

class Quartos(Pymongo):
    def __init__(self) -> None:
        super().__init__()
        self._conexao = self.database['quartos']
    
    @property
    def conexao(self):
        return self._conexao