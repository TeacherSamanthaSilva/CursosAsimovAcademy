# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

def cifra_cesar(texto, chave):
    # alfabetos para referência
    alfabeto_minus = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_maius = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    resultado = ""

    for char in texto:
        if char in alfabeto_minus:
            # pega a posição da letra
            pos = alfabeto_minus.index(char)
            # calcula a nova posição (com rotação circular usando %)
            nova_pos = (pos + chave) % 26
            resultado += alfabeto_minus[nova_pos]

        elif char in alfabeto_maius:
            pos = alfabeto_maius.index(char)
            nova_pos = (pos + chave) % 26
            resultado += alfabeto_maius[nova_pos]

        else:
            # se não for letra, mantém igual
            resultado += char

    return resultado


# Testes:
print(cifra_cesar("abc", 1))       # bcd
print(cifra_cesar("ABCDE", 2))     # CDEFG
print(cifra_cesar("Cachorro", -1)) # Bzbgnqqn
print(cifra_cesar("Olá Mundo!", 3))# Roá Pxqgr!
