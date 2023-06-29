class Estoque:
    def __init__(self) -> None:
        self.estoque = []

    def adicionar(self, produto):
        self.estoque.append(produto)

    def __str__(self) -> str:
        texto = ""
        for produto in self.estoque:
            texto += produto.__str__() + "\n"

        return texto