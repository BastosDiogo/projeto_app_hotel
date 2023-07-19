class ClienteModel():
    def __init__(self, nome:str, idade:int, cpf:str):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._dependentes = []
    
    def add_dependentes(self, dependentes: list):
        self._dependentes = dependentes
        print(f'Dependentes adicionados: {self._dependentes}')
    
    def modelo_cliente(self):
        payloard = {
                     "nome" : self._nome,
                     "idade" : self._idade,
                     "cpf" : self._cpf,
                     "dependentes" : self._dependentes,
                }

        return payloard