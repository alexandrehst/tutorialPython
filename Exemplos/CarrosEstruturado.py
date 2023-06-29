def main():
    carros = []
    digita_carros(carros)

def cria_carro(modelo, ano_fab, ano_modelo):
    carro = {}
    carro['modelo'] = modelo
    carro['ano_fab'] = ano_fab
    carro['ano_modelo'] = ano_modelo
    return carro

def salva_carro(carro, carros):
    carros.append(carro)

    return carros

def imprime_carros(carros):
    for carro in carros:
        print(carro)

def digita_carros(carros):
    while True:
        modelo = input('Digite o modelo do carro: ')
        ano_fab = int(input('Digite o ano de fabricação do carro: '))
        ano_modelo = int(input('Digite o ano de modelo do carro: '))
        carro = cria_carro(modelo, ano_fab, ano_modelo)
        salva_carro(carro, carros)

        continua = input('Deseja continuar? (S/N) ')
        if continua == 'N':
            break

    imprime_carros(carros)


if __name__ == "__main__":
    main()