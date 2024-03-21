# print(dir(restaurante_praca)) --> Atributos, métodos e propriedades
# print(vars(restaurante_praca)) --> Dicionário dos Atributos e métodos
# self --> Referência da instância naquele momento
# __init__ --> Método construtor
# __str__ --> Método que pega o objeto e mostra em um formato de texto definido por nós

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# Objetos da Classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

Restaurante.listar_restaurantes()