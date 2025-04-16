Registo={}
estudante= int(input("Quantos estudantes quer registrar? "))

for i in range (1, estudante+1):
    print(f"\n---estudante {i}---")

    nome=input("digite o nome do estudante: ")
    disciplinas=int(input(f"digite a quantidade da disciplina do {nome}: "))

    notas=[]

    for j in range(1,disciplinas+1):

        nota=float(input(f"digite a nota {j}: "))
        notas.append(nota)
        Registo[nome]=notas
print("\n---REGISTO FINAL---")
for estudante, notas in Registo.items():
    print(f"{estudante}:{notas}: ")