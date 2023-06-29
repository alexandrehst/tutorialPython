from Estoque import Estoque
from Carro import Carro


def main():
    estoque = Estoque()
    digita_carros(estoque)

def digita_carros(estoque):
    while True:
        modelo = input('Digite o modelo do carro: ')
        ano_fab = int(input('Digite o ano de fabricação do carro: '))
        ano_modelo = int(input('Digite o ano de modelo do carro: '))

        carro = Carro(modelo, ano_fab, ano_modelo)
        estoque.adicionar(carro)

        continua = input('Deseja continuar? (S/N) ')
        if continua == 'N':
            break
    print(estoque)

if __name__ == "__main__":
    main()
