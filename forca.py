import random

lista_palavras_secretas = []

with open('palavras_secretas.txt', 'r') as arquivo_palavras:
    for linha in arquivo_palavras:
        lista_palavras_secretas.append(linha.strip())

tamanho_lista_palavras_secretas = len(lista_palavras_secretas) - 1

num_palavra_aleatoria = random.randint(0, tamanho_lista_palavras_secretas)

palavra_secreta = lista_palavras_secretas[num_palavra_aleatoria]

underscores_palavra_secreta = ["_"] * len(palavra_secreta)

tentativas = 8


def logica_chutar_final():
    global tentativas

    if chute_letra_usuario == "chutar":
        print("Quer mesmo tentar acertar a palavra secreta? se errar você perde.\n")

        chutar_s_ou_n = input('Digite "sim" ou "nao": ')
        print()

        if chutar_s_ou_n == "sim":

            for letra in underscores_palavra_secreta:
                print(letra, end=" ")

            chute_final = input("  Digite seu chute: ")

            if chute_final == palavra_secreta:

                print("\nA palavra secreta é:")
                print(palavra_secreta.upper())

                return True
            else:

                print("\nErrado")

                tentativas = 0
                return True
        else:
            print("\nIsso lhe custou uma vida.\n")


print("Voce está jogando Forca!\n\n")

print('Digite "chutar" se acha que sabe qual é a palavra secreta\n')

print("A dica é: Frutas\n")

while tentativas > 0:

    if "_" in underscores_palavra_secreta:
        print(f"Vidas restantes: {tentativas}")

    for letra in underscores_palavra_secreta:
        print(letra, end=" ")

    if "_" not in underscores_palavra_secreta: break

    chute_letra_usuario = input(" - Digite seu chute: ")

    print()

    chute_nao_eh_letra = not chute_letra_usuario.isalpha()
    chute_n_tem_nada = chute_letra_usuario == ""
    chute_ta_errado = chute_letra_usuario not in palavra_secreta or chute_letra_usuario in lista_palavras_secretas or len(chute_letra_usuario) > 1

    if logica_chutar_final(): break

    if chute_n_tem_nada:

        print("Ei, digite alguma coisa pra jogar\n")

    elif chute_nao_eh_letra:

        print("Ei, digite apenas LETRAS\n")

    elif chute_letra_usuario in lista_palavras_secretas:

        print('Ei, se sabe qual é a palavra secreta, digite "chutar"\n')

    for i in range(len(palavra_secreta)):

        if chute_letra_usuario.lower() == palavra_secreta[i]:
            underscores_palavra_secreta[i] = chute_letra_usuario.upper()

    if chute_ta_errado:
        tentativas -= 1

print("\n")

resultado_do_jogo = "Voce ganhou." if tentativas > 0 else "Voce perdeu."

if "perdeu" in resultado_do_jogo:
    print(f"A palavra secreta era: {''.join(palavra_secreta.upper())}")

print()

print(resultado_do_jogo)
