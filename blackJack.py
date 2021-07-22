import random
from IPython.display import clear_output

bank = 500
deck = list(range(1,14))*4
card_letters = {
    1:"A",
    11:"J",
    12:"Q",
    13:"K",
}

def deal(deck, qtd):
    hand = []
    for i in range(qtd):
        random.shuffle(deck)
        card = deck.pop()
        card = card_letters.get(card, card)
        hand.append(card)
    return hand

def total(hand):
    total = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            if total >=11:
                total+=1
            else:
                total += 11
        else:
            total += card
    return total

def print_results(dealer_hand, player_hand):
    print("O Dealer tem " + str(dealer_hand) + " e um total de " + str(total(dealer_hand))+ " pontos")
    print("O Jogador tem " + str(player_hand) + " e um total de " + str(total(player_hand))+ " pontos")  
    
def bet_value():
    global bank
    bet_verify = False
    while not bet_verify:
        print("\nVocê possui %s" %(bank))
        try:
            bet = int(input("\nValor da aposta: "))
            if bet > bank:
                print("\nSaldo insuficiente, verifique seu caixa e o valor da sua aposta!\n")
                bet_verify = False
                
            elif bet <= bank:
                bet_verify = True
        except:
            print("Entre com um valor válido!")
            bet_verify = False
    return bet

def blackJack(dealer_hand, player_hand):
    if total(dealer_hand) == 21:
        print("O dealer tem um BlackJack!")
        return True
    elif total(player_hand) == 21:
        print("Você tem um Blackjack")
        return True
    return None
        
def add_card(hand):
    add_card = deck.pop()
    add_card = card_letters.get(add_card,add_card)
    hand.append(add_card)
    return hand

def win_check(dealer_hand, player_hand, value):
    global bank
    dealer_total = total(dealer_hand)
    player_total = total(player_hand)
    
    if dealer_total > 21:
        print("O Dealer passou dos 21 pontos! Você Ganhou!")
        bank += value
        return True
    
    elif player_total > 21:
        print("Você passou dos 21 pontos! Vitoria do Dealer!")
        bank -= value
        return True
    
    elif dealer_total > player_total and dealer_total <= 21:
        bank -= value
        print("Vitoria do Dealer!")
        return True
    
    elif dealer_total < player_total and player_total <= 21:
        bank += value
        print("Você Ganhou!")
        return True
    
    elif dealer_total == player_total:
        print("Empate")
        return True
    
    return None

def jogarNovamente():
    clear_output()
    Jogo()

def Jogo():
    global bank
    print("Bem vindo ao BlackJack \n\n")
    if bank<=0:
        print("Você quebrou a banca! Fim de Jogo")
    else:
        value = bet_value()
        player_hand = deal(deck, 2)
        dealer_hand = deal(deck, 1)
        play = False
    
        while not play:
            print_results(dealer_hand, player_hand)
            blackJack(dealer_hand, player_hand)
            print("O que você deseja fazer?\n")
            op = str(input("(P)edir mais uma carta \n(E)ncerrar aposta\n"))
            if op.lower() == "p":
                clear_output()
                add_card(player_hand)
                if total(player_hand) > 21:
                    add_card(dealer_hand)
                    print_results(dealer_hand, player_hand)
                    play = win_check(dealer_hand, player_hand, value)
        
            elif op.lower() == "e":
                clear_output()
                add_card(dealer_hand)
                if total(dealer_hand) <= 15:
                    while total(dealer_hand) <= total(player_hand):
                        add_card(dealer_hand)
                    print_results(dealer_hand, player_hand)
                    play = win_check(dealer_hand, player_hand, value)
                else:
                    blackJack(dealer_hand, player_hand)
                    print_results(dealer_hand, player_hand)
                    play = win_check(dealer_hand, player_hand, value)
            
    
            else:
                clear_output()
                print("\nOpção invalida! Selecione Novamente!\n")
            
        print("Seu novo saldo é de {a}".format(a=bank))
        jn = str(input("Jogar Novamente? S ou N\n"))
        if jn.lower() == "s":
            jogarNovamente()
        else:
            print("Obrigado por Jogar")

Jogo()
