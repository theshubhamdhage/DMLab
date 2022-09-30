import pandas as pd
from sklearn.preprocessing import LabelEncoder
import collections
import math
import csv
Le = LabelEncoder()

Loan_Data = pd.read_csv('info_gain_loan_input.csv')


# entropy = - summation of pi log(pi) with base 2

def find_entropy(x,y,t):
    if x!=0 and y!=0:
        return -((x/t)*(math.log2((x/t)))+(y/t)*(math.log2((y/t))))
    else:
        return 0.0


Loan_Data['Maritial_status'] = Le.fit_transform(Loan_Data['Maritial_status'])
Loan_Data['Income'] = Le.fit_transform(Loan_Data['Income'])
Loan_Data['Home_loan_refund'] = Le.fit_transform(Loan_Data['Home_loan_refund'])
Loan_Data['Defaulter'] = Le.fit_transform(Loan_Data['Defaulter'])
frequencyLoan = collections.Counter(Loan_Data.Defaulter)
tot=Loan_Data.Defaulter.size


EntropyOfData=find_entropy(frequencyLoan[0],frequencyLoan[1],tot)
print("Total entropy is:"+str(EntropyOfData))

def infoGain(frequency,a,tot,cond):
    infogain = 0.0
    for i in frequency:
        cnt = 0
        for x in range(Loan_Data.Defaulter.size):
            if Loan_Data.Defaulter.get(x)==1 and a.get(x)==i:
                cnt=cnt+1
        infogain += (frequency[i]/tot)*find_entropy(frequency[i]-cnt,cnt,frequency[i])
    condition = cond
    infogain = EntropyOfData - infogain
    print("Information gain by {} is: {}" .format(condition,infogain))
    return infogain



header = ['Attribute', 'InfoGain']

with open('infogain_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    frequencyMart = collections.Counter(Loan_Data.Maritial_status)
    data=['Maritial_status',infoGain(frequencyMart,Loan_Data.Maritial_status,tot,'Maritial_status')]
    writer.writerow(data)
    frequencyIncome = collections.Counter(Loan_Data.Income)
    data = ['Income', infoGain(frequencyIncome,Loan_Data.Income,tot,'Income')]
    writer.writerow(data)
    frequencyHome_loan_refund = collections.Counter(Loan_Data.Home_loan_refund)
    data = ['Home_loan_refund',infoGain(frequencyHome_loan_refund,Loan_Data.Home_loan_refund,tot,'Home_loan_refund')]
    writer.writerow(data)



