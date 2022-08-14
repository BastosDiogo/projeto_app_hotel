class QuartoModel():
    def __init__(self,
                 numero_quarto: str,
                 camas_adultos: int,
                 camas_criancas: int,
                 valor_diaria: float,
                 permite_pets: bool = False,
            ):
        self.numero_quarto  = numero_quarto
        self.camas_adultos  = camas_adultos
        self.camas_criancas = camas_criancas
        self.valor_diaria   = valor_diaria
        self.permite_pets   = permite_pets

    def modelo_quarto(self):
        payloard = {
                     "numero_quarto" : self.numero_quarto,
                     "numero_camas_adultos" : self.camas_adultos,
                     "numero_camas_criancas" : self.camas_criancas,
                     "valor_diaria" : self.valor_diaria,
                     "permite_pets" : self.permite_pets,
                     "historico_aluguel" : ''
                }

        return payloard