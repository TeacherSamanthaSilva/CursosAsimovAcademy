# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

# Lista de números
numeros = [10, 20, 30, 40, 50]

# Variável para guardar a soma
soma = 0

# Percorre cada número e soma manualmente
for n in numeros:
    soma += n

# Calcula a média
media = soma / len(numeros)

print("Soma:", soma)
print("Média:", media)

numeros = [10, 20, 30, 40, 50]

# Assume que o primeiro é o maior
maior = numeros[0]

# Percorre comparando
for n in numeros:
    if n > maior:
        maior = n

print("Maior valor:", maior)

palavras = ["casa", "computador", "sol", "Python", "teclado"]

print("Palavras com 5 ou mais caracteres:")
for palavra in palavras:
    if len(palavra) >= 5:
        print(palavra)
