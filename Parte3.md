# Orientação a Objetos

## Introdução

A orientação a objetos é o tipo de coisa que é mais fácil fazer do que falar. Mas de forma geral ela é um estilo de programação que tenta representar de uma forma mais direta os conceitos do mundo real no código.

Antes de avançarmos no que é a OO, vamos ver o que não é. Antigamente, programávamos (isso mesmo, eu também) no que é conhecido como programação estruturada. Nesse jeito de programar, os arquivos de programas contém funções que fazem tudo o que precisa ser feito, organizados da melhor maneira que o programa dor achar.

Vamos dar uma olhada no exemplo [CarroEstruturado.py](\Exemplos\CarrosEstruturado.py). Execute o programa. Basicamente digitamos carros e ele lista os carros.

Leia o programa e observa algumas coisas.
1. Tudo está dentro de um mesmo módulo. (Vamos falar de módulos daqui a pouco)
1. o array `carros` contém todos os carros inseridos.
1. Cada carro é um `dictionary`.
1. O programa cuida de tudo: interação com o usuário, vida da coleção de carros e da criação de cada carro individualmente

Mas aqui podemos identificar conceitos diferentes:
- Carro é uma entidade do mundo real
- A coleção de carros também é. Dependendo da aplicação, ela pode ser o estoque, por exemplo, ou talvez a coleção de carros antigos de alguém.
- A interação com o usuário não é uma "coisa" do mundo real, mas é uma função bem específica do programa.

Vamos supor que queiramos controlar o estoque de caminhões. Como você faria? Duas possibilidade:
1. Copiar todo o arquivo e criar o `CaminhoesEstruturado.py`
1. Ou, criar um array `Caminhoes` e duplicar as funções de salvar e imprimir

É aí que a POO (Programação Orientada a Objetos) mostra sua força.

Olhe o arquivo [Carro.py](/Exemplos/Carro.py). Viu como ele só tem coisas relativas ao carro?

> Uma classe é um molde para a criação de objetos. Ela representa os conceitos. Uma classe tem métodos e atributos.

Algumas coisas estranhas:
1. `Class` é a palavra que define uma classe.
1. O método `__init__` é chamado método construtor. Ele cria os objetos.
1. `self` é uma referência ao próprio objeto. Em Python ele é o primeiro parâmetro obrigatório em todos os métodos da classe.
1. `__str__` é outro método especial. Toda vez que o objeto da classe precisar ser convertido para uma `String`, esse método é executado.

> Objetos são as instâncias das classes. Exemplo: Carro é um conceito. Civic é um objeto do tipo Carro. Fiesta é outro objetos. Tanto Civic quanto Fiesta têm os mesmos métodos e atributos definidos pela classe

Agora de uma olhada no arquivo [Estoque.py](/Exemplos/Estoque.py). Veja como é pequeno. Ele só tem a lista, a adição e o método de impressão.

Agora veja [GerenciaEstoque.py](/Exemplos/GerenciaEstoque.py). Veja que esse aquivo não é uma classe. Ele é o que chamamos de _Controlador_, é um programa que cria objetos e gerencia sua execução.

Veja como tudo ficou organizado e pequeno.

## Estudo

Baixe o [livro](/Arquivos/Aprendendo%20Java%20na%20Marra%20-%20Avan%C3%A7ado.201511.pdf). Os exemplos e algumas coisas estão em Java, mas você consegue portar para Python.

Leia os seguintes capítulos e escreva todos os exemplos:
- 1 a 7
- 9
- 11 e 12 (quando o livro cita `ArrayList` pode considerar uma lista simples em Python `[ ]`)
- 16 a 21

