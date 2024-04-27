from random import randrange as rand #imporación de randrange como rand

class card: #Creación de la clase carta
    def __init__(self, number, suit): #Se le asigna a la carta un numero y una pinta
        self.number = number
        self.suit = suit
    def __str__(self): #En caso de imprimir a la carta se entrega un texto el cual indica el numero y la pinta de la carta
        return f'{self.number} of {self.suit}'
    def number(self): #En caso de usar la función number() se devuelve solo el numero de la carta
        return self.number
    def suit(self): #En caso de usar la función suit() se devuelve solo la pinta de la carta
        return self.suit
    
class deck: #Creación de la clase baraja
    numbers = ["2","3","4","5", #Se define una lista con todos los posibles numeros como strings
              "6","7","8","9", 
              "10","Jack","Queen",
              "King","Ace"]
    suits = ["Hearts", "Clubs", #Se define una lista con todas las posibles pintas
            "Diamonds", "Spades"]
    deck = [] #Se crea una lista vacía para la baraja
    def __init__(self, numb=1): #Se asigna la cantidad de barajas que se añadiran a la gran baraja
        self.numb = numb
    def create_deck(self): #Se define una función para crear la baraja
        for g in range(self.numb): #Bucle para la cantidad de barajas añadidas a la gran baraja
            for i in self.numbers: #Bucle por todos los posibles numeros
                for e in self.suits: #Bucle por todos las posibles pintas
                    a = card(i,e) #variable a la que se le va reasignando todas las posibles convinaciones de cartas
                    self.deck.append(a) #Se añade cada carta a la baraja
        return print("Deck created") 
    def __str__(self): #Al imprimir la baraja se imprime un mensaje diciendo que esto es una baraja
        return f'This is a deck'
    def shuffle(self): #Función para mezclar una baraja ya creada
        new_deck = []
        N = len(self.deck) #Se crea una variable con la cantidad de cartas en la baraja
        for i in range(N): 
            n = len(self.deck)
            a = self.deck.pop(rand(0,n))
            new_deck.append(a)
        self.deck = new_deck
        return
    def take_card(self):
        a = self.deck.pop()
        return a
    def length_of_deck(self):
        N = len(self.deck)
        return N