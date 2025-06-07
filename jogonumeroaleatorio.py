import random

def main():
  print("Bem vindo ao jogo de adivinhação!")
  numAleatorio = random.randint(1, 200)

  tentativas = 0
  numDigitado = 0

  while numDigitado != numAleatorio:
    numDigitado = int(input("Digite um número: "))

    if numDigitado == numAleatorio:
      print("Parabéns, você acertou!")
      break
    elif numDigitado < numAleatorio:
      print("o número digitado é menor que o número aleatório\n")
    else:
      print("o número digitado é maior que o número aleatório\n")
      tentativas += 1

  print("Você acertou com ",tentativas," tentativas")
      
  return 0
main()