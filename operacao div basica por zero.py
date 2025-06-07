def main():
  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))

  soma = num1 + num2
  sub = num1 - num2
  mult = num1 * num2

  if num2 == 0:
    div = "divisao por zero nao e permitida"
  else:
    div = num1 / num2

  print("a soma de ", num1, " + ", num2, " = ", soma)
  print("a subtracao de ", num1, " - ", num2, " = ", sub)
  print("a multiplicacao de ", num1, " * ", num2, " = ", mult)
  print("a divisao de ", num1, " / ", num2, " = ", div)
        
  return 0
main()