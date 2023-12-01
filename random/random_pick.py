import random

Lottery_tickets_List= []
for i in range(100):
    Lottery_tickets_List.append(random.randrange(1000000000, 9999999999))
   
winners = random.sample(Lottery_tickets_List,2)  
print(f"Lucky 2 lottery tickets are {winners}")
    
