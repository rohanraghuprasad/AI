initial=[0,1,3,2]
state=initial.copy()
def hcost(st,a,b):
    curr=st.copy()
    curr[a],curr[b]=curr[b],curr[a]
    cost=0
    for i in range(4):
        for j in range(i+1,4):
            if (abs(curr[i]-curr[j])==abs((i)-(j))):
                cost+=1
    return cost
def lows(s):
    l1=[]
    for i in s:
        l1.append(i[1])
    return (min(l1),l1.index(min(l1)))
swap=[((0,1),hcost(state,0,1)),((0,2),hcost(state,0,2)),((0,3),hcost(state,0,3)),((1,2),hcost(state,1,2)),((1,3),hcost(state,1,3)),((2,3),hcost(state,2,3))]
print(swap)
print(lows(swap))
while(lows(swap)[0]!=0):
    switch=swap[lows(swap)][1]
    state[switch[0]],state[switch[1]]=state[switch[1]],state[switch[0]]
    swap=[((0,1),hcost(state,0,1)),((0,2),hcost(state,0,2)),((0,3),hcost(state,0,3)),((1,2),hcost(state,1,2)),((1,3),hcost(state,1,3)),((2,3),hcost(state,2,3))]
