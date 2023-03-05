def opt1(pile):
    pile.sort()
    pile.pop(0)
    
def opt2(pile):
    for i,j in enumerate(pile):
        if i >= 2:
            x = i//2
            y = i-x
            pile.pop(i)
            pile.append(x)
            pile.append(y)
            pile.sort()
            break

t = int(input())
for k in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    while (len(a)!=0):
        winner  = "CHEF"
        opt2(a) or opt1(a)
        winner = "CHEFINA"
        
    print(winner)