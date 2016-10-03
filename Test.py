h = 0
t = 0
for i in range(1,5001):
    from random import randint
    random_num = (randint(0,1))
    if random_num == 1:
        h = h+1
        Trump = "head"
    else:
        t = t+1
        Trump = "tail"
print "Throwing a coin...It's a",Trump,'Got',h,'head(s) so far and',t,'tail(s) so far'
