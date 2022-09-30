import pandas
import csv
import math

data = pandas.read_csv("five_number_summary_input.csv")

arr = data['A'].tolist()

#sort the Array
arr.sort()


def median(array,start,end):
    n = end - start +1
    if n%2==0:
        return (array[start + (n//2) -1]+array[start + (n//2) ])/2
    else:
        return array[start+ n//2]

n= len(arr)
Min_val = min(arr)
Max_val = max(arr)
Median_val = median(arr,0,n-1)
quartile_1 = median(arr,0,n//2-1)
quartile_3 = median(arr,n//2+1,n-1)
IQR = quartile_3-quartile_1
upper_outlinear = quartile_3 + 1.5*(IQR)
lower_outlinear = quartile_1 - 1.5*(IQR)

header = ['Min Value', 'Max Value', 'Median','Quartile 1','Quartile 3','Upper Quartile','Lower Outliner']

with open('five_number_summary_output.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write the data

    data = [Min_val,Max_val,Median_val,quartile_1,quartile_3,upper_outlinear,lower_outlinear]
    writer.writerow(data)