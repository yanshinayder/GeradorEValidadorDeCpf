from random import randint
numero = str(randint(100000000, 999999999))

novo_cpf = numero
reverso = 10
total = 0

for index in range(19):
    if index > 8:
        index -= 9
    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        digito = 11 - (total % 11)

        if digito > 9:
            d = 0
        total = 0
        novo_cpf += str(digito)


while True:
    cpf = novo_cpf
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            digito = 11 -(total % 11)

            if digito > 9:
                d = 0
            total = 0
            novo_cpf += str(digito)

    protecao = novo_cpf == str(novo_cpf[0]) * len(cpf)

    if cpf == novo_cpf and not protecao:
        print(f'O Cpf {novo_cpf} é Válido')
        break
    else:
        print(f'O Cpf {novo_cpf} é Inválido')
        break