import math
from itertools import combinations

def get_freq(s,items,transactions):
    freq=0
    for t in transactions:
        temp=1
        for item in s:
            temp*=t[items.index(item)]
        if temp==1:
            freq+=1  
    return freq


level = 2
support = 0.5
f = open('FrequentItemSet_input.csv')
lines = f.readlines()
transactions = []
items = lines[0].split(',')                                 
for line in lines[1:]:
    transactions.append(list(map(int,line.split(','))))     
data ={'items':items,'transactions':transactions}

print(data)

items = data['items']
transactions = data['transactions']
min_freq = math.ceil(support*len(transactions))
sets = list(combinations(items,level))                      
frequent_sets = []
for s in sets:
    freq=get_freq(s,items,transactions)
    if freq>=min_freq:
        frequent_sets.append(s)
print("Ans is : {} ".format(frequent_sets))