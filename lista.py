from node import Node


class Lista:
    inicio = None

    def __init__(self):
        self.inicio = None

    def adicionar(self, valor, inicio=False):
        if inicio:
            self.adicionar_no_inicio(valor)
        else:
            self.adicionar_no_fim(valor)

    def adicionar_no_inicio(self, valor):
        novo_valor = Node(valor)
        novo_valor.proximo = self.inicio
        self.inicio = novo_valor

    def adicionar_no_fim(self, valor):
        if (self.inicio == None):
            self.inicio = Node(valor, None)
        else:
            aux = self.inicio

            while (aux.proximo != None):
                aux = aux.proximo

            aux.proximo = Node(valor, None)
            aux.proximo.anterior = aux

    def show(self):
        aux = self.inicio
        print("[", end='')

        while (aux.proximo != None):
            print(f"{aux.valor}", end=', ')
            aux = aux.proximo

        print(f"{aux.valor}]")

    def remover(self, valor):
        if (self.inicio.valor == valor):
            self.inicio = self.inicio.proximo
        else:
            anterior = None
            aux = self.inicio
            while (aux and aux.valor != valor):
                anterior = aux
                aux = anterior.proximo
            if aux:
                anterior.proximo = aux.proximo
            else:
                anterior.proximo = None
