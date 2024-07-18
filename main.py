import random
from decimal import Decimal, ROUND_HALF_UP

list = ["red", "blue", "green"]
car_color = random.choice(list)
wins = 0
attempts = 0
def picker():
    n = random.choice(list)
    return n
    
def problem():
    global wins
    choice = picker()
    new_list = ["red", "blue", "green"]
    
    new_list.remove(choice)
    try:
        new_list.remove(car_color)
    except ValueError:
        pass
        
    new_list_2 = ["red", "blue", "green"]
    
    
    if len(new_list) == 1:
        item = new_list[0]
        new_list_2.remove(item)
    else:
        item_2 = random.randint(0,1)
        new_list_2.remove(new_list[item_2])
    
 
    new_list_2.remove(choice)
    final_choice = new_list_2[0]
    if final_choice == car_color:
        wins += 1
        
while True:
    problem()
    attempts+=1
    if attempts == 10000000:
        break

wins /= attempts
wins *= 100

x = Decimal(wins).quantize(Decimal('0.000'), ROUND_HALF_UP)
print(f"win rate if you swapped doors = {x}%")
print(f"number of attempts = {attempts}")
