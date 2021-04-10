def max_sum(vet, inicio, final):
  if inicio == final:
    return inicio, final, vet[inicio]
  else:
    centro = round((inicio + final) / 2 - 0.5)
    inicio_esquerdo, final_esquerdo, soma_esquerdo = max_sum(vet, inicio, centro)
    inicio_direito, final_direito, soma_direito = max_sum(vet, centro + 1, final)
    inicio, final, soma = array_maximos(vet, inicio, centro, final)

    if soma_esquerdo >= soma_direito and soma_esquerdo >= soma:
      return inicio_esquerdo, final_esquerdo, soma_esquerdo
    elif soma_direito >= soma_esquerdo and soma_direito >= soma:
      return inicio_direito, final_direito, soma_direito
    else:
      return inicio, final, soma

def array_maximos(vet, inicio, centro, final):
  soma_esquerdo = -float("inf")
  soma = 0
  for i in range(centro, inicio - 1, -1):
    soma += vet[i]
    if soma > soma_esquerdo:
      soma_esquerdo = soma
      max_esquerdo = i
  soma_direitoeito_2 = -float("inf")
  soma = 0
  for j in range(centro + 1, final + 1):
    soma += vet[j]
    if soma > soma_direitoeito_2:
      soma_direitoeito_2 = soma
      max_dir = j
  return max_esquerdo, max_dir, soma_esquerdo + soma_direitoeito_2

if __name__ == '__main__':
  vetor_1 = [21, 10, -50, 2, 27, -16, -4, 10]
  vetor_2 = [-16, 20, -10, 12, 27, -6, -4, 8]
  print(max_sum(vetor_1, 0, 7))
  print(max_sum(vetor_2, 0, 7))