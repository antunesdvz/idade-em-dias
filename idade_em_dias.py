def idade_em_dias():
    idade = int(input("Digite sua idade: "))
    idade_dias = idade * 365
    idade_segundos = idade_dias * 24 * 60 * 60
    print(f"Sua idade em dias é: {idade_dias} dias")
    print(f"Sua idade em segundos é: {idade_segundos} segundos")

idade_em_dias()