class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

# Objetos da Classe
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'

restaurante_pizza = Restaurante()

restaurantes = [restaurante_pizza, restaurante_praca]

# print(dir(restaurante_praca)) --> Atributod, métodos e propriedades
# print(vars(restaurante_praca)) --> Dicionário dos Atributos e métodos

print(vars(restaurante_praca))