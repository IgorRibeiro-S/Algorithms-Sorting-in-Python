from random import randint


def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        pivot = lista[fim]
        indice = inicio
        for c in range(inicio, fim):
            if lista[c] <= pivot:
                aux = lista[c]
                lista[c] = lista[indice]
                lista[indice] = aux
                indice += 1
        aux2 = lista[fim]
        lista[fim] = lista[indice]
        lista[indice] = aux2
        quicksort(lista, inicio, fim - 1)
        quicksort(lista, fim + 1, fim)
        return indice


# SelectionSort = ordenação por comparação
def selectionsort(lista):
    num = len(lista)
    for pos in range(num - 1):
        minimo_ind = pos
        for c in range(pos, num):
            if lista[c] < lista[minimo_ind]:
                minimo_ind = c
        if lista[pos] > lista[minimo_ind]:
            aux = lista[pos]
            lista[pos] = lista[minimo_ind]
            lista[minimo_ind] = aux


# MergeSort = divisão e conquista
def mergesort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)
    if fim - inicio > 1:
        meio = (inicio + fim) // 2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)

        esquerda = lista[inicio:meio]
        direita = lista[meio:fim]
        topo_esquerda = 0
        topo_direita = 0
        for c in range(inicio, fim):
            if topo_esquerda >= len(esquerda):
                lista[c] = direita[topo_direita]
                topo_direita += 1
            elif topo_direita >= len(direita):
                lista[c] = esquerda[topo_esquerda]
                topo_esquerda += 1
            elif esquerda[topo_esquerda] < direita[topo_direita]:
                lista[c] = esquerda[topo_esquerda]
                topo_esquerda += 1
            else:
                lista[c] = direita[topo_direita]
                topo_direita += 1


if __name__ == '__main__':
    li = []
    for d in range(1, 7):
        li.append(randint(1, 45))

    print(li)
    quicksort(li)
    print(li)
