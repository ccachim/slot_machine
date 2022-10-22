import random

class Slot:
    def __init__(self):
        self.symbols = [
            ["#", 5, range(1,51)],
            ["$", 10, range(51,91)],
            ["%", 20, range(91,121)],
            ["&", 70, range(121,141)],
            ["@", 200, range(141,151)],
            ["€", 1000, range(151,156)],
            ["£", 100000, range(156,156)]
        ]

    def play(self):
        random_int = random.randint(1,156)
        for i in range(7):
            if random_int in self.symbols[i][2]:
                return self.symbols[i]

    def roll(self) -> tuple:
        results = []
        results_str = ""
        for i in range(3):
            input("Press 'Enter' to roll ...")
            results.append(self.play())
            results_str = results_str + results[i][0]
            print(results_str)

        jackpot = (results[0][0] == results[1][0] and results[1][0] == results[2][0])
        coeficiente = results[0][1]
        return (jackpot, coeficiente)

class Player:
    def __init__(self, name: str, credits: int):
        self.name = name
        self.credits = credits
        self.bet = 0
    
    def show_credits(self):
        print(f"You have {self.credits} credits.")

    def introduce(self):
        print(f"Hi {self.name}!")

    def won(self, value):
        self.credits += (value*self.bet)
        print(f"{self.name} you have won a Jackpot!!!")
    
    def lost(self):
        if self.credits == 0: print("Game over!")
        else: 
            print(f"{self.name} you are out of luck :(")

    def set_bet(self):
        bet = 0
        while True:
            bet = int(input("How much do you want to bet? "))
            if bet < 0 or bet > self.credits:
                print("Please enter a valid number of credits. ")
                continue
            else:
                print(f"You entered: {bet}")
                break
        self.bet = bet
        self.credits -= bet

    def continue_playing(self):
        while True:
            answer = input(f"{self.name} want to keep playing? (YES/NO) ")
            if answer != "YES" and answer != "NO":
                print("Please enter a valid answer. ")
                continue
            elif answer=="NO": return False
            else: return True

# initialize player
name = input("Hi! Whats your name? ")
credits = int(input("How many credits do you want to deposit: "))
player = Player(name, credits)
slot = Slot()
player.introduce()

# game loop
while True:
    # set bet
    player.set_bet()
    
    # check jackpot
    (jackpot, coeficiente) = slot.roll()

    if jackpot:
        player.won(coeficiente)
    else:
        player.lost()
    
    # ask to keep playing
    if player.credits==0: break
    if not player.continue_playing(): break
    player.show_credits()