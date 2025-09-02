import random

# 1) Sorteia um número secreto de 1 a 10
numero_secreto = random.randint(1, 10)

print("=== Jogo do Número Secreto ===")
print("Tente adivinhar o número de 1 a 10. Você tem 3 tentativas!\n")

# 2) Laço principal: até 3 tentativas
for tentativa in range(1, 4):
    # 3) Ler entrada com validação (não consome tentativa se digitar errado)
    while True:
        entrada = input(f"Tentativa {tentativa}: digite um número: ")
        try:
            chute = int(entrada)
            break
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")

    # (opcional) Aviso se estiver fora do intervalo, mas seguimos o jogo
    if chute < 1 or chute > 10:
        print("Obs.: o número secreto está entre 1 e 10.")

    # 4) Verifica acerto e dá dica
    if chute == numero_secreto:
        print("🎉 Parabéns! Você acertou!")
        break
    elif chute < numero_secreto:
        print("Dica: o número secreto é MAIOR.\n")
    else:
        print("Dica: o número secreto é MENOR.\n")

# 5) Se não houve acerto (sem break), o for-else executa
else:
    print(f"😢 Suas tentativas acabaram! O número secreto era {numero_secreto}.")
