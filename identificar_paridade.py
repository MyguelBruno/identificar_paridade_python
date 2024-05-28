def verificar_paridade(numeros):
  resultados = []
  for numero in numeros:
    if numero % 2 == 0:
      resultados.append(f'{numero} é par')
    else:
      resultados.append(f'{numero} é impar')
  return resultados

entrada = (input('Digite uma sequência de números separados por espaço: \n'))
numeros = list(map(int, entrada.split()))

resultados = verificar_paridade(numeros)

for resultado in resultados:
  print(resultado)