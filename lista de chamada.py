import random

def main():
  print("Lista de chamada")
  i = int(input("digite a quantidade de alunos: "))
  vet = [""] * i
  j = 0

  for i in vet:
    vet [j] = input("digite o nome do aluno: ")
    j = j + 1

  nome = "Murilo Vargas Agrela"
  print("As 6 primeiras letras do seu nome são: ", nome[0:6])
  print("Alunos que vieram hoje \n",vet)
  

      
  return 0
main()