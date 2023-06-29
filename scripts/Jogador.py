from dataclasses import dataclass

@dataclass
class Jogador:
    nome: str
    nivel_habilidade: int
    posicao: str

    def __post_init__(self):
        if self.nivel_habilidade < 1 or self.nivel_habilidade > 5:
            raise ValueError("O nível de habilidade deve estar entre 1 e 5")
        
        posicoes_validas = ["linha", "goleiro"]
        if self.posicao not in posicoes_validas:
            raise ValueError("A posição do jogador deve ser 'linha' ou 'goleiro'")