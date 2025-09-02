# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

duplicados = []

for item in lista1:
    if item in lista2 and item not in duplicados:
        duplicados.append(item)

print("Valores duplicados:", duplicados)
