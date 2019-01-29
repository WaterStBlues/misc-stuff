# calculates results of two dice(random 1-6 rolls) over a number of iterations

import random
def roll_die():
    d1 = random.randrange(1,7)
    d2 = random.randrange(1,7)
    return d1+d2

add_dict = {}
total_rolls = 1000

for i in range(1,total_rolls):
    dice = roll_die()
    if dice in add_dict:
        add_dict[dice] += 1 #if the key exists already, +1 the value
    else:
        add_dict[dice] = 1 #otherwise create the value
        
expected_dict={}
expected_count = 0 #count number of rolls in expected calculation (every combination of 1-6 once)
for i in range(1,7):
    for j in range(1,7):
        expCalc = i + j #1+1, 1+2, 1+3... etc until 6+6
        expected_count += 1
        if expCalc in expected_dict: #see previous loop
            expected_dict[expCalc] += 1
        else:
            expected_dict[expCalc] = 1

sim_percents = {} #these two loops will contain percentages
exp_percents={}

for i in range(2,13): #this loop calcs amounts and adds to respective dictionaries
    simAmt = (add_dict[i] / total_rolls) * 100
    sim_percents[i] = round(simAmt,2)
    expAmt = (expected_dict[i] / expected_count) * 100
    exp_percents[i] = round(expAmt,1)
    
print("Total\tSimulated %\tExpected %")
for i in range(2,13):
    print(i, "\t", sim_percents[i], "\t\t", exp_percents[i])