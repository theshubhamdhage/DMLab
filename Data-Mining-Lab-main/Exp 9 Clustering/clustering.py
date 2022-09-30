import math

X = [25,68,97,16]
Y = [56,12,36,45]
n = len(X)
x_mid = sum(X)/n
y_mid = sum(Y)/n

def dist(x1,y1,x2,y2):
    a = (x2-x1)*(x2-x1)
    b = (y2-y1)*(y2-y1)
    ans = math.sqrt(a+b)
    return ans

x = []
y = []
minimum = 1e9
x.append(x_mid)
y.append(y_mid)

for i in range(n):
    x.append(X[i])
    y.append(Y[i])

N = len(x)

mat = [[0 for _ in range(N)] for _ in range(N)]

for i in range(len(x)):
    for j in range(i+1,len(y)):
        mat[i][j]=dist(x[i],y[i],x[j],y[j])
        minimum= min(minimum,dist(x[i],y[i],x[j],y[j]))

for i in range(len(mat)):
    print(mat[i])


print("Minimum distance with centroid is {}" .format(minimum))