idade_anos = int(input("Digite sua idade: "))
ano_nascimento = int(input("Digite seu ano de nascimento: "))
idade_dias = idade_anos * 365
idade_segundos = idade_dias * 24 * 60 * 60
print(f"Sua idade em dias é: {idade_dias}")
print(f"Seus segundos vividos é: {idade_segundos}")
