import random

def jogo():
  # o computador escolhe um número aleatório de 0 a 10
  number = random.randint(0, 10)
  # o usuário tem 5 tentativas para adivinhar o número
  for i in range(5):
    # solicitar que o usuário digite um número
    palpite = input("Digite um número de 0 a 10: ")
    # verificar se o input é válido (um número inteiro na faixa permitida)
    if not palpite.isdigit():
      print("Por favor, digite apenas números inteiros de 0 a 10.")
      continue
    palpite = int(palpite)
    if palpite < 0 or palpite > 10:
      print("Por favor, digite um número inteiro de 0 a 10.")
      continue
    # verificar se o usuário acertou o número
    if palpite == number:
      # calcular a pontuação
      score = 100 - (i * 10)
      print(f"Parabéns, você acertou o número! Sua pontuação é {score}.")
      return
  # se o usuário chegou aqui, é porque não acertou o número
  print("Desculpe, você não conseguiu adivinhar o número. Tente novamente.")

# iniciar o jogo
while True:
  jogo()
  # perguntar se o usuário quer jogar novamente
  again = input("Deseja jogar novamente (s/n)? ")
  if again.lower() != "s":
    break
