def main():
  idade = int(input("Digite sua idade:"))

  if idade >= 18:
   print("Entrada Liberada")
  elif idade >= 16:
    acompanhante = input("possui um acompanhante? (s/n) ") 
    if acompanhante == "s" or acompanhante == "S":
      print("Entrada Liberada")
    else:
      print("Entrada Negada")

  else: 
    print("Entrada Negada")
  
  return 0
main()