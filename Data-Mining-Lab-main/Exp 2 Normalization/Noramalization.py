from cmath import sqrt
import pandas
import math
import csv  

 
# reading data from csv file
data = pandas.read_csv('Normalization_Input.csv')
 
#Storing all elements in Array
arr = []

for row in data:
    arr.append(int(row))            #Type casting to integer as CSV gives files in String format

n = len(arr)                #length of Array
sum_array = sum(arr)        #Sum of all elements in Array
mean_array = sum_array/n    #Mean of Array
max_array = max(arr)        #Max of all elements in Array
min_array = min(arr)        #Min of all elements in Array

MinMaxNorm = []

# V = V' - mean(A)/max(A)-min(A)*(newMax-newMin)  newMax= 1 & newMin =0

for i in arr:
    tmp = (i-min_array)/(max_array-min_array)           #Min Max Normalization Formula
    MinMaxNorm.append(tmp)

# zScore = 

sum_of_square = 0

for i in arr:
    sum_of_square += (i-mean_array)*(i-mean_array)  #finding sum of Square of all elements in Array

standardDeviation = sqrt(sum_of_square/n)           #calculating Standard Deviation

ZscoreNorm = []

for i in arr:
    tmp = (i-mean_array)/standardDeviation
    ZscoreNorm.append(tmp)

print(ZscoreNorm)


header = ['Input', 'Min-Max Normalized Array', 'Zscore Normalized Array']

with open('Normalization_Output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data
    #writer.writerow(data)

    for i in range(len(ZscoreNorm)):
        data = [arr[i],MinMaxNorm[i],ZscoreNorm[i]]
        writer.writerow(data)