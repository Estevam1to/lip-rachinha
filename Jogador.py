class Jogador:
    def __init__(self, nome: str, nivel_habilidade: int, posicao: str):
        self._nome = nome
        self._nivel_habilidade = nivel_habilidade
        self._posicao = posicao

    def get_nome(self) -> str:
        return self._nome

    def set_nome(self, novo_nome: str) -> None:
        self._nome = novo_nome

    def get_nivel_habilidade(self) -> int:
        return self._nivel_habilidade

    def set_nivel_habilidade(self, novo_nivel_habilidade: int) -> None:
        if novo_nivel_habilidade < 1 or novo_nivel_habilidade > 5:
            raise ValueError("O nível de habilidade deve estar entre 1 e 5")
        self._nivel_habilidade = novo_nivel_habilidade

    def get_posicao(self) -> str:
        return self._posicao

    def set_posicao(self, nova_posicao: str) -> None:
        posicoes_validas = ["Linha", "Goleiro"]
        if nova_posicao not in posicoes_validas:
            raise ValueError("A posição do jogador deve ser 'Linha' ou 'Goleiro'")
        self._posicao = nova_posicao
