#What's the probability of getting 22 heads in 30 tosses?
from random import randint
M = 0
for i in range(10000):
    trials = []
    for j in range(30):
        trials.append(randint(0,1))
    if(sum(trials) >= 22):
        M+=1
P = M/10000
print(P)