import numpy as np
import pandas as pd
import csv
data = pd.read_csv('Tweight_Dweight_Input.csv')

Location = data['Location'].tolist()
A = data['Veg'].tolist()
B = data['NonVeg'].tolist()    
Total = []
for i in range(len(A)):
    tmp = A[i]+B[i]
    Total.append(tmp)


A_T_wt = []
B_T_wt = []
A_D_wt = []
B_D_wt = []
verify=[]
sum_total = sum(Total)
A_total=sum(A)
B_total=sum(B)
for i in range(len(A)):
    A_T_wt.append(A[i]/Total[i])
    B_T_wt.append(B[i]/Total[i])
    A_D_wt.append(A[i]/A_total)
    B_D_wt.append(B[i]/B_total)
    verify.append(A_T_wt[i]+B_T_wt[i])
print("Veg d weight total -> {}".format(sum(A_D_wt)))
print("NonVeg d weight total -> {}".format(sum(B_D_wt)))
header = ['Location', 'Veg', 'NonVeg', 'Total' , 'Veg_T_wt','NonVeg_T_wt','verify t weight','Veg_D_wt','NonVeg_D_wt']



with open('Tweight_Dweight_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    for i in range(len(A)):
        data = [Location[i],A[i],B[i],Total[i],A_T_wt[i],B_T_wt[i],verify[i],A_D_wt[i],B_D_wt[i]]
        writer.writerow(data)