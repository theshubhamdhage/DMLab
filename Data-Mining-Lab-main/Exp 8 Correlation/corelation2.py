import pandas

data = pandas.read_csv("corelation2_input.csv")

A = data['A'].tolist()
B = data['B'].tolist()
C = data['C'].tolist()

def corelation(A,B):
    n = len(A)

    prob_A = 0
    prob_B = 0
    prob_A_B =0

    for i in range(n):
        if  A[i] and B[i]:
            prob_A_B += 1
        
        if A[i]==1:
            prob_A += 1
        
        if B[i]==1:
            prob_B += 1
        
    ans = (prob_A_B)/(prob_A*prob_B)
    print(ans)
    return ans


corelation(A,B)
corelation(B,C)
corelation(A,C)