def bubble_sort(lista):
    tamanho_lista = len(lista)

    troca = False
    passadas = 0
    for i in range(tamanho_lista):
        passadas += 1
        for j in range(0, tamanho_lista - i - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                troca = True
        if troca:
            print("Swap")
            troca = False
        else:
            break

    return lista, passadas

lista_desordenada = [13, 95, 119, 184, 96, 102, 21, 48, 137, 57, 99, 5, 45, 170, 154, 146]
print("Unordered List:")
print(lista_desordenada, len(lista_desordenada))

print("Ordered List:")
print(bubble_sort(lista_desordenada))

