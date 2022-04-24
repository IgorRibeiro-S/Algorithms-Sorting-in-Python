from random import randint
import time


# Insertion Sort = ordenação por inserção
def insertsort(lista):
    num = len(lista)
    for c in range(1, num):
        aux = lista[c]
        ind = c - 1
        while ind >= 0 and lista[ind] > aux:
            lista[ind + 1] = lista[ind]
            ind -= 1
        lista[ind + 1] = aux


# Selection Sort = ordenação por seleção
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


# Shell Sort = insertion sort melhorado
def shellsort(lista):
    num = len(lista)
    h = num // 2
    while h > 0:
        i = h
        while i < num:
            aux = lista[i]
            ind = i - h
            while ind >= 0 and lista[ind] > aux:
                lista[ind + h] = lista[ind]
                ind -= h
            lista[ind + h] = aux
            i += 1
        h = h // 2


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


# Quick Sort = ordenação por comparação
def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        piv = particao(lista, inicio, fim)
        quicksort(lista, inicio, piv - 1)
        quicksort(lista, piv + 1, fim)


def particao(lista, inicio, fim):
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
    return indice


if __name__ == '__main__':
    li = []
    for d in range(1, 100000):
        li.append(randint(1, 100000))

    print(li)
    antes = time.time()
    quicksort(li)
    depois = time.time()
    total = (depois - antes) * 1000
    print(f"o tempo total foi de {total:.2f} ms")
