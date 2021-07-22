import random 
from IPython.display import clear_output

bank = 500
class Deck(object):
    
    def __init__(self):
        self.cards = list(range(1,14))*4
    
    def switch_nums(self, card):
        card_letters = {1:"A", 11:"J", 12:"Q", 13:"K"}
        switched = card_letters.get(card, card)
        return switched
    
    def deal(self, qtd):
        hand = []
        for i in range(qtd):
            random.shuffle(self.cards)
            card = self.cards.pop()
            card = self.switch_nums(card)
            hand.append(card)
        return hand
    
    def add_card(self, hand):
        add_card = self.cards.pop()
        add_card = self.switch_nums(add_card)
        hand.append(add_card)
        return hand
    
    def total(self, hand):
        total = 0
        for card in hand:
            if card == "J" or card == "Q" or card == "K":
                total += 10
            elif card == "A":
                if total >= 11:
                    total+=1
                else:
                    total += 11
            else:
                total += card
        return total
    
    def is_blackjack(self, hand):
        
        if hand.__len__() == 2 and self.total(hand) == 21:
            print("\nBlackJack!! \n")
        
        
    
class Bank(object):
    
    global bank
    
    def __init__(self):
        self.cash = bank
        
    def show_bank(self):
        
        return self.cash
        
    def bet_value(self):
        if self.cash <= 0:
            print("Você quebrou a banca! Fim de jogo!")
            return True
        else:
            bet_verify = False
            while not bet_verify:
                print("Você possui %s" %(self.cash))
                try:
                    bet = int(input("Valor da aposta: "))
                    print("\n")
                    if bet > self.cash:
                        print("Saldo insuficiente")
                        bet_verify = False
                    else:
                        bet_verify = True
                except:
                    print("Valor invalido!")
                    bet_verify = False
            return bet
    
    def win_bet(self, bet):
        
        self.cash += bet
        return bank
    
    def lose_bet(self, bet):
        
        self.cash -= bet
        return bank
    
def win_check(dealer_hand, player_hand, bet, bank, deck):
    
    dealer_total = deck.total(dealer_hand)
    player_total = deck.total(player_hand)
    
    if dealer_total > 21:
        print("O Dealer passou dos 21 pontos! Você Ganhou!")
        bank.win_bet(bet)
        return True
    
    elif player_total > 21:
        print("Você passou dos 21 pontos! Vitoria do Dealer!")
        bank.lose_bet(bet)
        return True
    
    elif dealer_total > player_total and dealer_total <= 21:
        bank.lose_bet(bet)
        print("Vitoria do Dealer!")
        return True
    
    elif dealer_total < player_total and player_total <= 21:
        bank.win_bet(bet)
        print("Você Ganhou!")
        return True
    
    elif dealer_total == player_total:
        print("Empate")
        return True
    
    return None

def print_results(dealer_hand, player_hand, deck):
    print("\nO Dealer tem " + str(dealer_hand) + " e um total de " + str(deck.total(dealer_hand))+ " pontos")
    print("O Jogador tem " + str(player_hand) + " e um total de " + str(deck.total(player_hand))+ " pontos\n")
    
def jogar_novamente():
    clear_output()
    Jogo()
            
def Jogo():
    print("Bem Vindo ao BlackJack! \n")
    deck = Deck()
    bet = bank.bet_value()
    player_hand = deck.deal(2)
    dealer_hand = deck.deal(1)
    if bet is True:
        play = True
    else:
        play = False
        while not play:
            print_results(dealer_hand, player_hand, deck)
            deck.is_blackjack(player_hand)
            print("O que você deseja fazer?\n")
            op = str(input("(P)edir mais uma carta \n(E)ncerrar Aposta\n"))
            if op.lower() == "p":
                clear_output()
                deck.add_card(player_hand)
                deck.is_blackjack(player_hand)
                if deck.total(player_hand) > 21:
                    clear_output()
                    deck.add_card(dealer_hand)
                    deck.is_blackjack(dealer_hand)
                    print_results(dealer_hand, player_hand, deck)
                    play = win_check(dealer_hand, player_hand, bet, bank, deck)
            elif op.lower() == "e":
                deck.add_card(dealer_hand)
                if deck.total(dealer_hand) <= 21:
                    clear_output()
                    while deck.total(dealer_hand) <= deck.total(player_hand) and deck.total(dealer_hand) < 21:
                        deck.add_card(dealer_hand)
                    deck.is_blackjack(dealer_hand)
                    print_results(dealer_hand, player_hand, deck)
                    play = win_check(dealer_hand, player_hand, bet, bank, deck)
        
            else:
                  print("Opção Inválida!")
                

        print("\nSeu novo saldo é: {a}".format(a = bank.show_bank()))
        jn = str(input("Jogar Novamente? S ou N\n"))
        if jn.lower() == "s":
            jogar_novamente()
        else:
            print("Obrigado por Jogar")
    
bank = Bank()
Jogo()