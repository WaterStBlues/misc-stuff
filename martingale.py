#Tests the martingale betting strategy

import random
initialCash = int(input("Enter starting cash: $"))
startbet = int(input("Enter starting bet: $"))
bankList = []

for i in range(100):
    
    bank = initialCash    
    bet = startbet
    playCount = 0
    loseStreak = 0
    
    while bank > bet and bank < initialCash*100: #stop if you can't afford the bet or walk away if big wins are made
        playCount+=1
        luck = random.randrange(0,2)
        if luck == 0:
            loseStreak += 1
            bank -= bet
            bet = bet * 2
        elif luck == 1:
            bank += bet
            bet = startbet
            if loseStreak > 0:
                loseStreak = 0
    bankList.append(bank)

print([i for i in bankList])
print("Average = " + str((sum(bankList)/len(bankList))))
