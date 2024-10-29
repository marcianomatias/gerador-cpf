import random

for _ in range(100):
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    contador_regressivo_1 = 10

    resultado_digito = 0
    for digito in nove_digitos:
        resultado_digito += int(digito) * contador_regressivo_1
        contador_regressivo_1 -= 1
    digito_1 = (resultado_digito * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_regressivo_2 = 11

    resultado_digito_2 = 0
    for digito in dez_digitos:
        resultado_digito_2 += int(digito) * contador_regressivo_2
        contador_regressivo_2 -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

    #print(cpf_gerado)
    # Formata o CPF no padrão XXX.XXX.XXX-YY
    cpf_formatado = f'{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:11]}'

    print(cpf_formatado)