import os
from modelos.petshop import Petshop
from modelos.avaliacao import Avaliacao

class ProgramaExpresso:
    def __init__(self):
        self.Petshops = [
            Petshop('PetBrilho', 'Bichos em geral'),
            Petshop('CãoBom', 'Cães'),
            Petshop('Like a Cat', 'Gatos')
        ]

    def finalizar_app(self):
        os.system("cls")
      
        print("Finalizando o app\n")

    def voltar_menu_principal(self):
        input("Digite uma tecla para voltar ao menu principal: ")

    def mostrar_subtitulo(self, texto):
        os.system("cls")
        linha = '*'*(len(texto))
        print(texto)
    
        print()

    def escolher_opcoes(self):
        self.mostrar_subtitulo  ('''
    𝓟𝓮𝓽 𝓢𝓱𝓸𝓹 𝓔𝔁𝓹𝓻𝓮𝓼𝓼𝓸''')
                               
        print("1 - Cadastrar Petshop")
        print("2 - Listar Petshops")
        print("3 - Avaliar Petshop")
        print("4 - Ver Média de Avaliações")
        print("5 - Sair\n")

    def opcao_invalida(self):
        self.mostrar_subtitulo("Opção inválida\n".ljust(20))
        self.voltar_menu_principal()

    def listarPetshops(self):
        self.mostrar_subtitulo('Listando os Petshops'.ljust(20))
        print("Nome:".ljust(27), "Categoria:".ljust(34))
        for Petshop in self.Petshops:
            print(Petshop)

    def avaliacao(self):
        self.mostrar_subtitulo("Avaliar Petshop\n".ljust(20))
        self.listarPetshops()

        nome_Petshop = input("Digite o nome do Petshop que deseja avaliar: ")
        Petshop_encontrado = False

        for Petshop in self.Petshops:
            if nome_Petshop == Petshop.nome:
                Petshop_encontrado = True
                while True:
                    nota = int(input("Digite uma nota de 1 a 5 para avaliar este Petshop: "))
                    if 1 <= nota <= 5:
                        Petshop.adicionar_avaliacao(nota)
                        print(f"Você avaliou o Petshop {nome_Petshop} com a nota {nota}.")
                        break
                    else:
                        print("Por favor, digite uma nota válida (entre 1 e 5).")

        if not Petshop_encontrado:
            print("Petshop não encontrado.")

        self.voltar_menu_principal()

    def ver_media_avaliacoes(self):
        self.mostrar_subtitulo("Média de Avaliações dos Petshops\n".ljust(20))
        for Petshop in self.Petshops:
            print(Petshop.calcular_media_avaliacoes())

        self.voltar_menu_principal()

    def cadastrar_novo_Petshop(self):
        nome_do_Petshop = input("Digite o nome do novo Petshop: ")
        categoria = input(f'Digite a categoria do Petshop {nome_do_Petshop}: ')
        Petshop_novo = Petshop(nome_do_Petshop, categoria)
        self.Petshops.append(Petshop_novo)
        print(f"Você cadastrou o Petshop: {nome_do_Petshop}")

    def main(self):
        while True:
            try:
                self.escolher_opcoes()
                opcao_digitada = int(input("Digite a opção desejada: "))
                if opcao_digitada == 1:
                    print("Você escolheu cadastrar Petshop\n" )
                    self.cadastrar_novo_Petshop()
                elif opcao_digitada == 2:
                    self.listarPetshops()
                    self.voltar_menu_principal()
                elif opcao_digitada == 3:
                    self.avaliacao()
                elif opcao_digitada == 4:
                    self.ver_media_avaliacoes()
                elif opcao_digitada == 5:
                    print("Você escolheu sair do aplicativo\n")
                    self.finalizar_app()
                    break
                else:
                    self.opcao_invalida()
            except ValueError:
                print("Por favor, digite um número válido.")

if __name__ == "__main__":
    programa = ProgramaExpresso()
    programa.main()