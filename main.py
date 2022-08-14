from models.quartos import Quartos
from base_model.quarto_model import QuartoModel
#from model_base.candidato_model import canditato_model

#candidatos = canditato_model(3)
#conectar = py().database.insert_many(candidatos)
# conectar = list(py().database.find())
# print(conectar)

quartos = Quartos().conexao
lista_quartos = []
for x in range(1,11):
    modelo_quartos = QuartoModel(str(x), 0, 0, 0).modelo_quarto()
    lista_quartos.append(modelo_quartos)
criar_quartos = quartos.insert_many(lista_quartos)

#print(criar_quartos)
mostrar_quartos = list(quartos.find())
print(f'\n{mostrar_quartos}\n')