def media_notas():
    nome = input("Digite o nome do aluno: ")
    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))
    nota3 = int(input("Digite a terceira nota: "))
    media = (nota1 + nota2 + nota3) / 3

    if media >= 7:
        print(f"{nome} está Aprovado com a média {media}")
    else:
        print(f"{nome} está Reprovado com a média {media}")

media_notas()