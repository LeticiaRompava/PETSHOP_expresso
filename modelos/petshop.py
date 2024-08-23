class Petshop:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.avaliacoes = []

    def adicionar_avaliacao(self, nota):
        self.avaliacoes.append(nota)

    def calcular_media_avaliacoes(self):
        if not self.avaliacoes:
            return "Sem avaliações ainda."
        else:
            media = sum(self.avaliacoes) / len(self.avaliacoes)
            return f'{self.nome}    Média de estrelas: {media:.2f} ({len(self.avaliacoes)} avaliações)'

    def __str__(self):
        return f'Nome: {self.nome.ljust(20)}  Categoria: {self.categoria.ljust(22)}'
    