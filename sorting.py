from random import randint


def selection_sort(lista):
    num = len(lista)
    for pos in range(num - 1):
        minimo_ind = pos  # 3
        for c in range(pos, num):
            if lista[c] < lista[minimo_ind]:
                minimo_ind = c
        if lista[pos] > lista[minimo_ind]:
            aux = lista[pos]
            lista[pos] = lista[minimo_ind]
            lista[minimo_ind] = aux


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
    selection_sort(li)
    print(li)