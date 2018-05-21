"""
 classe principal

"""
from Aula01 import Aula01Classe

# função principal
def main():
    # instância de Aula01Classe
    mostra = Aula01Classe.Minha_Primeira_Classe()
    #  chama a função mostra algo
    mostra.mostra_Algo("Minha primeira chamada de função de outra classe")


if __name__ == '__main__':
    # chamada da função principal
    main()
    __Author__ = 'Gorfo'