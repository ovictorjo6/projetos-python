import random

def monty_hall_game():
    # Configuração inicial
    portas = ['Cabra', 'Cabra', 'Prêmio']
    random.shuffle(portas)
    
    # Jogador escolhe uma porta inicialmente
    escolha_inicial = int(input("Escolha uma porta (1, 2 ou 3): ")) - 1
    
    # Anfitrião revela uma porta com cabra
    portas_reveladas = [i for i in range(3) if i != escolha_inicial and portas[i] == 'Cabra']
    porta_revelada = random.choice(portas_reveladas)
    
    print("O anfitrião revela a porta {}, que tem uma cabra.".format(porta_revelada + 1))
    
    # Jogador decide se troca de porta ou mantém a escolha inicial
    troca = input("Você quer trocar de porta? (sim/não): ").strip().lower()
    if troca == 'sim':
        escolha_final = [i for i in range(3) if i != escolha_inicial and i != porta_revelada][0]
    else:
        escolha_final = escolha_inicial
    
    # Resultado do jogo
    if portas[escolha_final] == 'Prêmio':
        print("Parabéns! Você ganhou o prêmio!")
    else:
        print("Que pena! Você ganhou uma cabra.")
    
    # Mostrar todas as portas para referência
    print("As portas eram: {}".format(portas))

# Executar o jogo
monty_hall_game()
