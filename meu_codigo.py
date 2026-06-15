print("preciso de algumas informacoes as, aluno")
nome = input("qual seu nome aluno?")
print(f"prazer {nome}!")
idade = int(input("qual sua idade aluno?"))
print(f"{idade} anos, que legal!")


print("===== SISTEMA DE NOTAS ESCOLARES =====")

print("preiso saber se voce passou em portugues")
nota1 = float(input("digite a primeira nota de portugues:"))
nota2 = float(input("digite a segunda nota de portugues:"))
media = (nota1 + nota2) / 2
print(f"sua media e: {media}")
if media >= 7:
    print("parabens, voce foi aprovado!")
elif media >= 5:
    print("voce esta de recuperacao, estude mais para passar!")
else:
    print("voce foi reprovado, estude mais, e MUITO importante que voce se dedique aos estudos, para ter um futuro melhor!")
print("vou mandar o pessoal preparar seu boletim")
print("===== FIM =====")